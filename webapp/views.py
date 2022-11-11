from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy

def index_view(request, *args, **kwargs):
    if request.method == "POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('index')
    tasks = Task.objects.all()
    # url = reverse('index', kwargs={tasks})
    # print(url)
    # return HttpResponseRedirect(url)
    return render(request, 'index.html', {'tasks': tasks})

def create_task(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        details = request.POST.get('details')
        deadline = request.POST.get('deadline')
        if not deadline:
            deadline = None
        new_task = Task.objects.create(title=title, status=status, details=details, deadline=deadline)
        # url = reverse('task_view', kwargs={'pk':new_task.pk})
        # return HttpResponseRedirect(url)
        # return HttpResponseRedirect(f'/task/{new_task.pk}/')
        # return render(request, 'task_view.html', {'task': new_task})
        return redirect('task_view', pk=new_task.pk)

def task_view(request, pk):
    # task_id = kwargs.get('pk')
    # try:
    #     task = Task.objects.get(pk=pk)
    # except Task.DoesNotExist:
    #     # return HttpResponseNotFound('Not Found')
    #     raise Http404
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    # return HttpResponseRedirect(f'/task?id={task.pk}')
    return render(request, 'task_view.html', {'task': task})

# class ItemDelete(delete_view):
#     model=
# def remove(request, pk):
#     # task_id = request.GET.get('id')
#     task = Task.objects.get(pk=pk)
#     task.delete()
#     return redirect('index', pk=task.pk)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.details = request.POST.get('details')
        task.deadline = request.POST.get('deadline')
        if not task.deadline:
            task.deadline = None
        task.save()
        return redirect('task_view', pk=task.pk)

def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method =="GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method =="POST":
        task.delete()
        return redirect('index')

