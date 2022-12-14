# Generated by Django 4.1.3 on 2022-12-07 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('spec', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=500)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.department')),
            ],
        ),
    ]