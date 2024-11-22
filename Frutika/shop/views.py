from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.db.models import Q
# Create your views here.


def categories(request):
    c=Category.objects.all()
    return render(request,'categories.html',{'cat':c})



def products(request,pk):
    c=Category.objects.get(id=pk)
    p=Products.objects.filter(category_object=c)
    return render(request,'products.html',{'cat':c,'pro':p})



def product_details(request,pk):
    pr=Products.objects.get(id=pk)
    return render(request,'pro_details.html',{'p':pr})



def add_category(request):    

    if (request.method=='POST'):

        n=request.POST['na']
        d=request.POST['de']
        i=request.FILES['im']
       
        b=Category.objects.create(name=n,desc=d,image=i)
        b.save()

        return redirect('shop:categories')
    
    return render(request,'add_category.html')





def add_products(request):
    if (request.method=='POST'):

        n=request.POST['na']
        d=request.POST['de']
        i=request.FILES['im']
        p=request.POST['pr']
        s=request.POST['st']
        c=request.POST['ca']   #to get the category name only
        cat=Category.objects.get(name=c)  #to get the full category model details
        p=Products.objects.create(name=n,desc=d,image=i,price=p,stock=s,category_object=cat)
        p.save()
        return redirect('shop:categories')
    
    return render(request,'add_products.html')




def add_stock(request,pk):
    p=Products.objects.get(id=pk)
    if(request.method=='POST'):
        p.stock=request.POST['st']
        p.save()
        return redirect('shop:details',pk)
    

    return render(request,'add_stock.html',{'pro':p})




def search(request):

    p=None
    search=''
    if(request.method=='POST'):
        search=request.POST['se']
        if(search):
            p=Products.objects.filter(Q(name__icontains=search) | Q(desc__icontains=search))

    return render(request,'search.html',{'products':p,'search':search})




    