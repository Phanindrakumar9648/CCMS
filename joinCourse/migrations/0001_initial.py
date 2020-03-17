# Generated by Django 2.0.1 on 2018-03-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('designation', models.CharField(choices=[('student', 'Student'), ('employee', 'Employee')], max_length=100)),
                ('college', models.CharField(max_length=500)),
                ('course', models.CharField(choices=[('c', 'C'), ('c++', 'C++'), ('python', 'Python'), ('c#', 'C#'), ('java', 'Java'), ('web', 'Web Technologies'), ('php', 'PHP')], max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('joined_date', models.DateTimeField()),
            ],
        ),
    ]