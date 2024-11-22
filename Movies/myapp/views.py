from django.shortcuts import render,redirect
from myapp.models import Movies

def home(request):
    movies=Movies.objects.all()
    return render(request,'home.html',{'movies':movies})


def add_movies(request):
    if(request.method=='POST'):
        name=request.POST['name']
        year=request.POST['year']
        image=request.FILES['image']
        details=request.POST['details']
        m=Movies.objects.create(name=name,year=year,image=image,details=details)
        m.save()
        return redirect('home')
    
    return render(request,'add.html')



def details(request,pk):
    d=Movies.objects.get(id=pk)
    return render(request,'details.html',{'details':d})



def delete(request,pk):
    m=Movies.objects.get(id=pk).delete()
    return redirect('home')




def edit(request,pk):
    mo=Movies.objects.get(id=pk)
    if(request.method=='POST'):
        mo.name=request.POST['na']
        mo.year=request.POST['ye']
        mo.details=request.POST['de']
        if(request.FILES.get('im')==None):
            mo.save()
        else:
            mo.image=request.FILES.get('im')
        mo.save()
        return redirect('home') 

    return render(request,'edit.html',{'mov':mo})












# def edit(request,pk):

#     mo=Movies.objects.get(id=pk)
#     if (request.method=='POST'):
#         mo.name=request.POST['na']
#         mo.year=request.POST['ye']
#         mo.details=request.POST['de']
#         if (request.FILES.get('im')==None):
#             mo.save
#         else:
#             mo.image=request.FILES.get('im')
#         mo.save
#         return redirect('home')        


#     return render(request,'edit.html',{'movie':mo})



# def book_edit(request,pk):

#     book=Books.objects.get(id=pk) 

#     if (request.method=='POST'):
#         book.title=request.POST['t'] 
#         book.author=request.POST['a']
#         book.language=request.POST['l']
#         book.pages=request.POST['p']
#         book.price=request.POST['pr']
#         if (request.FILES.get('c')==None):
#             book.save()
#         else:
#             book.cover=request.FILES.get('c')
#         if (request.FILES.get('f')==None):
#             book.save
#         else:
#             book.pdf=request.FILES.get('f') 
#         book.save()     
#         return redirect('books:view')
    
#     return render(request,'books_edit.html',{'book':book})