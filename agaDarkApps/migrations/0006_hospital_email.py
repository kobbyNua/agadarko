# Generated by Django 3.2.4 on 2023-01-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agaDarkApps', '0005_auto_20221215_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.EmailField(default='info@example.com', max_length=255),
        ),
    ]
