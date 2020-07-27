from django.db import models


TIPOS_TESTE =[
    ('RT-PCR', 'RT-PCR'),
    ('Sorologia', 'Sorologia'),
    ('Teste Rápido - Antígenos', 'Teste Rápido - Antígenos'),
    ('Teste Rápido - Anticorpos', 'Teste Rápido - Anticorpos'),
]
TIPOS_RESULTADO = [(False, 'Negativo'), (True, 'Positivo')]




class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    unasc = models.DateField(blank= True)
    uteste = models.CharField(max_length=100, choices=TIPOS_TESTE, default='RT-PCR')
    uresultado = models.BooleanField(choices=TIPOS_RESULTADO)

    class Meta:
        db_table = "user"