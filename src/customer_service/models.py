from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='expéditeur')
    read = models.BooleanField(default=False, verbose_name='lu')
    name = models.CharField(max_length=128, default='inconu', verbose_name="nom de l'éxpediteur")
    email = models.EmailField(verbose_name='adresse mail')
    subject = models.CharField(max_length=1024, blank=True, verbose_name='sujet')
    content = models.TextField(max_length=128000, verbose_name='contenu du message')
    sending_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'

    def __str__(self):
        return self.name
