# Generated by Django 3.0.6 on 2020-05-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0012_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]