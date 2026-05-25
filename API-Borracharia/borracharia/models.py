from django.db import models

class user(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    celular = models.CharField(max_length = 14)
    tipo_usuario = models.CharField(max_length = 15)
    def __str__(self):
        return self.nome

class ticket(models.Model):
    STATUS = (
        ('R', 'Recebido'),
        ('A', 'A Caminho'),
        ('C', 'Concluído'),
    )
    cliente_id = models.ForeignKey(user,on_delete = models.CASCADE)
    localizacao = models.CharField(max_length = 200)
    codigo = models.CharField(max_length=10)
    descricao_servico = models.CharField(max_length = 100)
    status = models.CharField(max_length = 1, choices = STATUS, blank = False, null = False)
    data = models.DateField()

    def __str__(self):
        return self.codigo

class lista(models.Model):
    user = models.ForeignKey(user,on_delete = models.CASCADE)
    ticket = models.ForeignKey(ticket,on_delete = models.CASCADE)