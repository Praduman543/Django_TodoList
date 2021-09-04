from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False, 'name': "Praduman"}
    if request.method == "POST":
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskDesc)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html',context)

# This function will  delete task

def delete_data(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return redirect('tasks')