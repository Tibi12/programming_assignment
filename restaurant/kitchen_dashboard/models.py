from django.db import models

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=10, choices=[('occupied', 'Occupied'), ('free', 'Free')], default='free')

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('cooking', 'Cooking'), ('completed', 'Completed')], default='pending')
    order_type = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.menu_item.price
        super().save(*args, **kwargs)

class TableCart(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)