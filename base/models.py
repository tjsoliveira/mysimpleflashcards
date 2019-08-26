from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date


class Disciplina(models.Model):

    nome = models.CharField(max_length=50, null=False)

    class Meta:
            verbose_name = 'Disciplina'
            verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome

class Baralho(models.Model):

    tema = models.CharField(max_length=50, null=False)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} --> {}'.format(self.tema, self.disciplina)

class Carta(models.Model):

    baralho = models.ForeignKey(Baralho, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=False)
    frente = RichTextField(null=False)
    verso = models.CharField(max_length=50, null=False)
    visto_quando = models.DateField(null=False, default=date.today)
    sera_visto_em = models.DateField(null=False, default=date.today)

    def __str__(self):
        return '{} - {}'.format(self.id, self.titulo)