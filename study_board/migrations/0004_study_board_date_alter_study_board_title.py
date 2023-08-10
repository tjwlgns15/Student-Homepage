# Generated by Django 4.2 on 2023-04-28 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("study_board", "0003_delete_member_remove_study_board_writer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="study_board",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="study_board",
            name="title",
            field=models.CharField(max_length=40, null=True),
        ),
    ]
