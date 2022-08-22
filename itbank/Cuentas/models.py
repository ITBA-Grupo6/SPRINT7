from django.db import models

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, blank=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'