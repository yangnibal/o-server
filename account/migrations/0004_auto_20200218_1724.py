# Generated by Django 3.0.3 on 2020-02-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
        ('account', '0003_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wrong_probs',
            field=models.ManyToManyField(default=None, to='problems.Problems'),
        ),
    ]
