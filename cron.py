from django_cron import CronJobBase, Schedule

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .tarefas.models import Tarefa

class AtualizarDiasRestantesJob(CronJobBase):
    RUN_EVERY_MIDNIGHT = Schedule(run_at_times=['00:00'])

    def do(self):
        # Atualizar dias restantes para todas as tarefas
        tarefas = Tarefa.objects.all()
        for tarefa in tarefas:
            tarefa.calcular_dia_restante()
            tarefa.save()