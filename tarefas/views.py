from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import AdicionarTarefa


def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()

    return render(request, 'tarefas/tarefas_pendentes.html',
                   {'tarefas_pendentes': tarefas_pendentes,
                    'form':form})







   
