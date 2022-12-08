from django.db import models

class IpClientes(models.Model):
    ip_address = models.CharField(max_length=100,default='0.0.0.0')