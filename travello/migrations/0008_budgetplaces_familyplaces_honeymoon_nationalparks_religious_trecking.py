# Generated by Django 3.0.6 on 2020-05-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0007_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='budgetplaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='familyplaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='honeymoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='nationalparks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='religious',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='trecking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('small_desc', models.TextField(blank=True, null=True)),
                ('big_desc', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('sittayma', models.BooleanField(default=True)),
                ('video', models.URLField(max_length=500, null=True)),
            ],
        ),
    ]
