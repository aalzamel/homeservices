# Generated by Django 2.0.1 on 2018-01-24 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=3)),
                ('street', models.CharField(max_length=120)),
                ('avenue', models.PositiveIntegerField(blank=True, null=True)),
                ('building_number', models.PositiveIntegerField()),
                ('floor', models.CharField(blank=True, max_length=3, null=True)),
                ('apartment', models.CharField(blank=True, max_length=5, null=True)),
                ('extra_directions', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('area', models.ForeignKey(on_delete='PROTECT', to='services.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(on_delete='PROTECT', to='services.Unit'),
        ),
        migrations.AddField(
            model_name='address',
            name='area',
            field=models.ForeignKey(on_delete='PROTECT', to='services.Area'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete='PROTECT', to=settings.AUTH_USER_MODEL),
        ),
    ]