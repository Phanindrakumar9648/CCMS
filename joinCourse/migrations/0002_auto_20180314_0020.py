# Generated by Django 2.0.1 on 2018-03-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joinCourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='course',
            field=models.CharField(choices=[('c', 'C'), ('c++', 'C++'), ('python', 'Python Programming'), ('c#', 'C#'), ('java', 'Java'), ('web', 'Web Technologies'), ('php', 'PHP')], max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='joined_date',
            field=models.DateField(),
        ),
    ]
