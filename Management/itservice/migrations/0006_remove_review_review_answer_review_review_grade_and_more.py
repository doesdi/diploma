# Generated by Django 4.2 on 2023-05-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itservice', '0005_application_application_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_answer',
        ),
        migrations.AddField(
            model_name='review',
            name='review_grade',
            field=models.CharField(choices=[('Отлично!', 'Отлично!'), ('Очень хорошо', 'Очень хорошо'), ('Хорошо', 'Хорошо'), ('Плохо', 'Плохо'), ('Очень плохо', 'Очень плохо')], default='Мужчина', max_length=15, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
    ]
