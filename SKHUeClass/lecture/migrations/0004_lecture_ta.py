# Generated by Django 2.0.3 on 2018-06-11 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_student_ista'),
        ('lecture', '0003_lecturenotice'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='ta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ta_student', to='account.Student'),
        ),
    ]
