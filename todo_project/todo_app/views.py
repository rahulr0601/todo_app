from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'generic_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'generic_update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('cbvlist',kwargs={'pk':self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('/')


def home(request):
    all_task = Task.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        obj1 = Task(name=name,priority=priority,date=date)
        obj1.save()
        return redirect('/')
    return render(request,'home.html',{'tasks':all_task})


def delete(request, id1):
    if request.method == "POST":
        obj2 = Task.objects.get(id=id1)
        obj2.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id2):
        obj3 = Task.objects.get(id=id2)
        form = TaskForm(request.POST or None, instance=obj3)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'update.html', {'form':form,'obj3':obj3})
