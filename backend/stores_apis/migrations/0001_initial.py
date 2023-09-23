# Generated by Django 4.2.5 on 2023-09-20 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('url', models.TextField()),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_access', to='store.store')),
            ],
        ),
    ]