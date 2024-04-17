from django.db import models

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=10, choices=[('occupied', 'Occupied'), ('free', 'Free')], default='free')