# Generated by Django 2.1.1 on 2019-11-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20181112_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('8:00 - 8:50', '8:00 - 8:50'), ('8:50 - 9:40', '8:50 - 9:40'), ('8:50 - 9:40', '9.40 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('1:30 - 2:20', '1:30 - 2:20'), ('2:50 - 3:40', '2:50 - 3:40'), ('3;40 - 5:00', '3;40 - 5:00')], default='11:00 - 11:50', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2019-04-24'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]
