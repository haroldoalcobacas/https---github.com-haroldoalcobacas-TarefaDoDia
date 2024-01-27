from django.shortcuts import render, redirect,get_object_or_404
from .models import Tarefa
from .forms import AdicionarTarefa, EditarTarefa


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

def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_pendentes_list')


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')

def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)   
    if request.method == 'POST':
        form = EditarTarefa(request.Post)
        if form.is_valid():
            cd = form.cleaned_data 
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
        
        else:
            form = EditarTarefaForm(initial={'tarefa':tarefa.descricao,'categoria':tarefa.categoria})
        return render(request, 'tarefas/editar_tarefa.html', {'tarefa':tarefa, 'form':form})