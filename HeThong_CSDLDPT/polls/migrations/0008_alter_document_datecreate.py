# Generated by Django 4.0.2 on 2022-04-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_document_datecreate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='datecreate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
