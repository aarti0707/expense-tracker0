# Generated by Django 4.2.7 on 2023-11-29 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(default='A', max_length=200),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(),
        ),
    ]
