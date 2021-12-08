
from django.shortcuts import redirect, render
from empapp.forms import AddEmployeeForm,UpdateEmployeeForm
from empapp.models import Employee
# Create your views here.
def home(request):
    return render(request,'empapp/home.html')

def add_employee(request):
    print(request.POST) 
    
    if request.method == 'POST':
        form=AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read/')
    context ={
        'form':AddEmployeeForm()
        }        
    return render(request,'empapp/add.html',context)

def read_employee(request):
    context={
        'employees':Employee.objects.all()
    }
    return render(request,'empapp/read.html',context)

def detail_employee(request , id):
    print(id)
    context={
        'obj':Employee.objects.get(pk=id)
    }
    return render(request,'empapp/detail.html',context)

def update_employee(request,id):
    obj = Employee.objects.get(pk=id)
    print(request.POST)
    if request.method =="POST":
        form = UpdateEmployeeForm(request.POST,instance=obj)
        if form.is_valid(): 
            form.save()
            return redirect('/read/')

    context ={ 
        'form':UpdateEmployeeForm(instance=obj)
        }        

    return render (request , 'empapp/update.html' , context) 

def delete_employee(request,id):
    print(id)
    obj=Employee.objects.get(pk=id)
    if request.method =='POST':
        obj.delete()
        return redirect('/read/')    
    context={
        'obj':Employee.objects.get(pk=id)
    }
    return render(request,'empapp/delete.html',context)


def search(request):
    return render(request,'empapp/search.html')

def search_result(request):
    if request.method=="GET":
        query=request.GET.get('query')
        if query:
            employees=Employee.objects.filter(employee_name__icontains=query)
            return render(request,'empapp/searchresult.html',{'employees':employees})
        else:
            print("no information to show")
            return render(request,'empapp/searchresult.html',{})