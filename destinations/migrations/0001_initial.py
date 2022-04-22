# Generated by Django 3.2 on 2022-04-19 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50, unique=True)),
                ('area_description', models.TextField()),
                ('friendly_area_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['area_name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
                ('friendly_district_name', models.CharField(blank=True, max_length=254, null=True)),
                ('area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.area')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=254, unique=True)),
                ('dest_description', models.TextField()),
                ('hotspot', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.area')),
                ('district_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinations.district')),
            ],
        ),
    ]