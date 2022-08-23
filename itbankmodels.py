# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.AutoField(primary_key=True, blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.IntegerField(blank=True, null=True)
    new_type = models.IntegerField(blank=True, null=True)
    user_action = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.CharField()
    direccion_empleado_id = models.IntegerField(blank=True, null=True)
    direccion_cliente_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjeta(models.Model):
    marca_id = models.AutoField(primary_key=True)
    nombre_tarjeta = models.CharField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Movimientos(models.Model):
    movimiento = models.AutoField(primary_key=True)
    numerocuenta = models.IntegerField(db_column='numeroCuenta')  # Field name made lowercase.
    monto = models.IntegerField()
    tipooperacion = models.IntegerField(db_column='tipoOperacion')  # Field name made lowercase.
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero = models.TextField(unique=True)
    cvv = models.IntegerField()
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.CharField()
    tarjeta_marca = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, blank=True, null=True)
    tarjeta_cliente_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    description_id = models.CharField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    descripcion_cuenta = models.CharField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
