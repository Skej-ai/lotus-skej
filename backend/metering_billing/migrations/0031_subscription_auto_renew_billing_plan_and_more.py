# Generated by Django 4.0.5 on 2022-10-04 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0030_alter_billingplan_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="auto_renew_billing_plan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="next_billing_plan",
                to="metering_billing.billingplan",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="billing_plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="current_billing_plan",
                to="metering_billing.billingplan",
            ),
        ),
    ]