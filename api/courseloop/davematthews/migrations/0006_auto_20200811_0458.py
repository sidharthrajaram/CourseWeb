# Generated by Django 3.1 on 2020-08-11 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('davematthews', '0005_submission_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='frq',
        ),
        migrations.CreateModel(
            name='FrqSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('content', models.TextField(default='-')),
                ('frq', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='davematthews.frqassignment')),
            ],
        ),
    ]
