# Generated by Django 3.2.12 on 2022-03-26 06:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
