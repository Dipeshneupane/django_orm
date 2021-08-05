# Generated by Django 3.2.6 on 2021-08-05 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_itema_itemb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('books_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.book')),
                ('ISBN', models.TextField()),
            ],
            bases=('students.book',),
        ),
    ]