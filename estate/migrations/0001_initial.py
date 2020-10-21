# Generated by Django 3.1.2 on 2020-10-19 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import estate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('sq_fit', models.PositiveIntegerField(blank=True, null=True)),
                ('bedrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('display_img', models.ImageField(default='default.png', upload_to='display_img')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=estate.models.image_upload_to)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.properties')),
            ],
        ),
    ]