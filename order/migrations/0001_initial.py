# Generated by Django 3.1.2 on 2020-10-10 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(blank=True, max_length=100)),
                ('item_name', models.CharField(blank=True, max_length=100)),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_time', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.PositiveIntegerField(blank=True, default=0)),
                ('destination', models.CharField(blank=True, max_length=100)),
                ('items', models.ManyToManyField(blank=True, to='order.Item')),
                ('normal_user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
