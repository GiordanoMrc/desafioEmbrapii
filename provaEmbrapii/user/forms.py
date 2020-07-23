from django import forms
from user.models import User
TIPOS_TESTE =[
    ('RT-PCR', 'RT-PCR'),
    ('Sorologia', 'Sorologia'),
    ('Teste Rápido - Antígenos', 'Teste Rápido - Antígenos'),
    ('Teste Rápido - Anticorpos', 'Teste Rápido - Anticorpos'),
]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"