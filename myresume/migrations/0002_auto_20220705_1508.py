# Generated by Django 2.2.5 on 2022-07-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=30)),
                ('section_name_eng', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.CharField(max_length=100, verbose_name='Github账号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='联系方式'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, verbose_name='中文名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username_eng',
            field=models.CharField(max_length=60, verbose_name='英文名'),
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection_name', models.CharField(max_length=100)),
                ('subsection_name_eng', models.CharField(max_length=100)),
                ('by_section', models.ForeignKey(on_delete='CASCADE', to='myresume.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=30)),
                ('by_subsection', models.ForeignKey(on_delete='CASCADE', to='myresume.Subsection')),
            ],
        ),
    ]
