# Generated by Django 3.1 on 2020-08-13 03:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('davematthews', '0010_auto_20200811_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frqassignment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('85a72442-927f-4e46-a42b-841e1c3b7c9d')),
        ),
        migrations.AlterField(
            model_name='frqsubmission',
            name='frq',
            field=models.ForeignKey(blank=True, default=13, on_delete=django.db.models.deletion.CASCADE, to='davematthews.frqassignment'),
        ),
        migrations.AlterField(
            model_name='frqsubmission',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('238365f3-2687-437f-a1d3-674d447ada83')),
        ),
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8fb33a89-88e9-49b8-b2fd-fecad4466548')),
        ),
        migrations.AlterField(
            model_name='submission',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8f3b5021-1124-48fe-96d8-c284eb16c976')),
        ),
        migrations.AlterField(
            model_name='submission',
            name='ws',
            field=models.ForeignKey(blank=True, default=10, on_delete=django.db.models.deletion.CASCADE, to='davematthews.wsassignment'),
        ),
        migrations.AlterField(
            model_name='wsassignment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('15dd627b-553d-40b1-968e-db40f66fb19c')),
        ),
    ]
