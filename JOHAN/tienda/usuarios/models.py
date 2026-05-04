from django.db import models

# Create your models here.


from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username