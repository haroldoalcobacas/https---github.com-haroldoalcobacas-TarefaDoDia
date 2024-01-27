from django.db import models

class Tarefa(models.Model):
    Opcoes_Status = (
        ('concluído', 'Concluído',),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
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

