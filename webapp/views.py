from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

def index_view(request, *args, **kwargs):
    if request.method == "POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
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

    return render(request, 'task_view.html', context)