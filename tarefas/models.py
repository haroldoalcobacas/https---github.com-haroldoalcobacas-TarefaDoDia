from django.db import models

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

