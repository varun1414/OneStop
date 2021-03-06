# Generated by Django 3.1.3 on 2020-11-12 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'general_customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loginc',
            fields=[
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('cust', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general.customer')),
            ],
            options={
                'db_table': 'loginc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('cust', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general.customer')),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=30)),
                ('amont', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.TextField()),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.IntegerField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=100)),
                ('address', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'seller',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general.seller')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'logins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('pro', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general.product')),
            ],
            options={
                'db_table': 'sells',
                'managed': False,
            },
        ),
    ]
