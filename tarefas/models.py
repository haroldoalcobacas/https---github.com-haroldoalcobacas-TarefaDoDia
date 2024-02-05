from django.db import models
from django.utils import timezone




class Tarefa(models.Model):
    Opcoes_Status = (
        ('concluída', 'Concluída',),
        ('pendente', 'Pendente'),
        ('adiada', 'Adiada'),
    )
    Opcoes_Categoria = (
        ('urgente','Urgente'),
        ('importante', 'Importante'),
        ('comum', 'Comum'),
    )

    descricao = models.CharField(max_length=200)
    criacao = models.DateTimeField(auto_now_add = True)
    categoria = models.CharField(max_length=25, choices=Opcoes_Categoria, default = 'comum')
    status = models.CharField(max_length=25, choices = Opcoes_Status, default='pendente')
    conclusao = models.DateTimeField(null=True, blank=True)
    prazo = models.DateTimeField(null=True, blank=True)
    dia_restante = models.IntegerField(null=True, blank=True)

    def calcular_dia_restante(self):
        if self.prazo:
            data_atual = timezone.now().date()
            data_prazo = self.prazo.date()
            dias_restantes = (data_prazo - data_atual).days
            return dias_restantes
        else:
            return None

    def save(self, *args, **kwargs):
        self.dia_restante = self.calcular_dia_restante()
        super().save(*args, **kwargs)