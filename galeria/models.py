from datetime import datetime
from django.db import models

from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALAXIA", "Galáxia"),
        ("PLANETA" , "Planeta"),
        ("ESTRELA", "Estrela"),
        
    ]

    nome = models.CharField(max_length=255, null = False, blank = False)
    legenda = models.CharField(max_length=150, null = False, blank = False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null = False, blank = False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank = True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        null=True,
        blank=False,
        on_delete= models.SET_NULL,
        related_name="user"
    )

    def __str__(self):
        return self.nome
    
    