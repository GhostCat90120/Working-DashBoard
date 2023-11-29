from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=100)
    inventory_produce = models.PositiveIntegerField()
    cost_produce = models.PositiveIntegerField()
    inventory_meat = models.PositiveIntegerField()
    cost_meat = models.PositiveIntegerField()
    inventory_miscellaneous = models.PositiveIntegerField()
    cost_miscellaneous = models.BigIntegerField()

    def __str__(self):
        return f'Inventory id {self.id} for month of {self.month}'

class PData(models.Model):
    customers = models.ForeignKey(User, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.customers.username} ordered {self.inventory.cost_produce}and {self.inventory.cost_meat}and{self.inventory.cost_miscellaneous} on {self.inventory.month}'
        