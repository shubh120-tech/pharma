# Generated by Django 3.0.5 on 2020-05-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedicineName', models.CharField(max_length=50)),
                ('describe', models.CharField(default='', max_length=400)),
                ('date', models.DateField()),
                ('picture', models.ImageField(default='', upload_to='MathuraMed/Images')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
