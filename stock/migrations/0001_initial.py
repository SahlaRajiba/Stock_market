# Generated by Django 3.2.18 on 2023-04-10 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=90)),
                ('place', models.CharField(max_length=90)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=90)),
                ('place', models.CharField(max_length=90)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=90)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.login')),
            ],
        ),
        migrations.CreateModel(
            name='tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.expert')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.expert')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.user')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificaion', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.expert')),
            ],
        ),
        migrations.AddField(
            model_name='expert',
            name='lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.login'),
        ),
        migrations.CreateModel(
            name='doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubt', models.CharField(max_length=90)),
                ('reply', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.expert')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.user')),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificaion', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=90)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.user')),
            ],
        ),
    ]
