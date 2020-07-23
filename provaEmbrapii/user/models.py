from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    unasc = models.CharField(max_length=100)
    uteste = models.CharField(max_length=100)
    uresultado = models.BooleanField()
    class Meta:
        db_table = "user"