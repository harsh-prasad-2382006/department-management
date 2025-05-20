from django.shortcuts import render,redirect
from .models import Department
# Create your views here.
def index(request):
    search_query = request.GET.get('q', '')
    if search_query:
        departments = Department.objects.filter(dept_name__icontains=search_query)
    else:
        departments = Department.objects.all()
    
    context = {
        'departments': departments,
    }
    return render(request, 'index.html', context)


def create_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        
        dept =Department.objects.create(dept_name = name,description = description)
        dept.save()
        return redirect('index')
    return render(request,'create_department.html')

def update_department(request,id):
    department = Department.objects.get(dept_id = id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        dept = Department.objects.filter(dept_id = id).update(dept_name = name,description = description)
        return redirect('index')
    context = {
        'departments':department
    }
    return render(request,'update_department.html',context)

def delete_department(request,id):
    department = Department.objects.get(dept_id = id)
    var = request.GET.get('q')
    if var == "0":
        
        department.status = False
    else:
        department.status = True
    
    department.save()
    return redirect('index')