from django.shortcuts import render,HttpResponseRedirect
from .forms import Todo
from .models import Todolist

# Create your views here.
# Add and Show Data
def Todo_Add(request):
    if request.method == 'POST':
        fm=Todo(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            reg=Todolist(name=nm)
            reg.save()
            fm=Todo()

    else:
        fm=Todo()
    stud=Todolist.objects.all()
    return render(request,'enroll/todo.html',{'form':fm,
    'stu':stud})

# Update User Data
def update_list(request,id):
    if request.method == 'POST':
        pi=Todolist.objects.get(pk=id)
        fm=Todo(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Todolist.objects.get(pk=id)
        fm=Todo(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})

# Delete Function
def delete_data(request,id):
    if request.method == 'POST':
        pi=Todolist.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')




