# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=70)
    contact = models.IntegerField()
    email = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GeneralCustomer(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'general_customer'


class Loginc(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    cust = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'loginc'


class Logins(models.Model):
    seller = models.OneToOneField('Seller', models.DO_NOTHING, primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'logins'
    
    @property
    def passw(self):
        return self.password


class Orders(models.Model):
    cust = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    pro = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('cust', 'pro'),)


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    payment_type = models.CharField(max_length=30)
    amont = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.TextField()
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)
    address = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'seller'


class Sells(models.Model):
    pro = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)
    seller = models.ForeignKey(Seller, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sells'
        unique_together = (('pro', 'seller'),)
