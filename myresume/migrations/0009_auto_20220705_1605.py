# Generated by Django 2.2.5 on 2022-07-05 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0008_section_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myresume.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subsection',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myresume.User'),
            preserve_default=False,
        ),
    ]
