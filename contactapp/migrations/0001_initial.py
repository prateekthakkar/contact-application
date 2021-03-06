# Generated by Django 2.1.7 on 2019-05-21 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contact_list',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='profile_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactapp.Country', verbose_name='Countery')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactapp.Country', verbose_name='Countery'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactapp.State', verbose_name='States'),
        ),
    ]
