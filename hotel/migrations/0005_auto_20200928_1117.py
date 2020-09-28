# Generated by Django 3.1.1 on 2020-09-28 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20200928_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealselection',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='mealselection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='serviceselection',
            name='service',
        ),
        migrations.RemoveField(
            model_name='serviceselection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='serviceselection',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='MealSelection',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceSelection',
        ),
    ]