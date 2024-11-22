from django.shortcuts import render,redirect
from shop.models import Products

from cart.models import Cart,Payment,order_details
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
# Create your views here.

def addto_cart(request,pk):
    p=Products.objects.get(id=pk)
    u=request.user
    try:                           #if the product is already in the cart of the same user
        c=Cart.objects.get(product=p,user=u)
        c.quantity+=1  #increase the quantity inside the record
        p.stock-=1
        p.save()          
        c.save()
    except:                         #if not present
        c=Cart.objects.create(product=p,user=u,quantity=1)     #add a new record with quantity=1
        p.stock-=1
        p.save()
        c.save() 
    return redirect('cart:cart_view')   
    



def cart_view(request):
    u=request.user
    c=Cart.objects.filter(user=u)

    #to calculate sub total
    total=0
    for i in c:
        total+=i.product.price * i.quantity  

      

    return render(request,'addto_cart.html',{'cart':c,'total':total})




def cart_minus(request,pk):
    u=request.user
    p=Products.objects.get(id=pk)
    try:
        c=Cart.objects.get(user=u,product=p)
        if(c.quantity>1):
            c.quantity-=1
            c.save()
            p.stock+=1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save() 
    except:
        pass         
    return redirect('cart:cart_view')  



def cart_delete(request,pk):
    u=request.user
    p=Products.objects.get(id=pk)
    try:
        c=Cart.objects.get(user=u,product=p)
        c.delete()
        p.stock+=c.quantity
        p.save()
    except:
        pass    

    return redirect('cart:cart_view')



def place_order(request):

    if(request.method=='POST'):
        a=request.POST['ad']
        ph=request.POST['ph']
        pin=request.POST['pi']

        

        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.product.price * i.quantity
        #print(total)  


        #razorpay connection
        client=razorpay.Client(auth=('rzp_test_FlS15ifJjCvzOY','fjfunQkcVFf6zv9AkMZCrmYr')) 

        #razorpay order creation
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        #print(response_payment)
         
        order_id=response_payment['id']
        status=response_payment['status']

        if (status=='created'):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()


            for i in c:
                o=order_details.objects.create(product=i.product,user=i.user,phone=ph,address=a,pin=pin,order_id=order_id,no_of_items=i.quantity)
                o.save()



            return render(request,'payment.html',{'payment':response_payment,'name':u.username})


    return render(request,'place_order.html')
    





@csrf_exempt
def payment_status(request,pk):

    user=User.objects.get(username=pk)  #to retrieve user object to stay logged in
    login(request,user)


    response=request.POST
    #print(response)

    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],        #for checking the payment details, we pass param dict to
                                                                        #verify_payment_signature function
        'razorpay_payment_id':response['razorpay_payment_id'],

        'razorpay_signature':response['razorpay_signature']
              }
    
    client=razorpay.Client(auth=('rzp_test_FlS15ifJjCvzOY','fjfunQkcVFf6zv9AkMZCrmYr'))
    try:
        status=client.utility.verify_payment_signature(param_dict)                                                                                     
        print(status)

        p=Payment.objects.get(order_id=response['razorpay_order_id'])
        p.razopay_payment_id=response['razorpay_payment_id']
        p.paid=True
        p.save()

        o=order_details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status='completed'
            i.save()


        #to remove the cart items after successfull payment
        c=Cart.objects.filter(user=user) 
        c.delete()   


    except:
        pass


    return render(request,'payment_status.html')







def your_orders(request):
    u=request.user
    o=order_details.objects.filter(user=u,payment_status='completed')

    return render(request,'your_orders.html',{'orders':o})

