from django.db import models

class alunoTreino(models.Model):

    STATUS = (
        ('done', 'DONE'),
        ('doing', 'DOING')
    )

    exercicio = models.CharField(max_length=256)
    repeticao = models.CharField(max_length=256)

    done = models.CharField(
        max_length=5,
        choices=STATUS

    )
    
    Created_at = models.DateField(auto_now_add=True)
    upptead_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.exercicio



# Create your models here.
