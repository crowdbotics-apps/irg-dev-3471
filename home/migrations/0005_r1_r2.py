# Generated by Django 2.2.12 on 2020-05-01 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_r2"),
    ]

    operations = [
        migrations.AddField(
            model_name="r1",
            name="r2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="r1_r2",
                to="home.CustomText",
            ),
        ),
    ]
