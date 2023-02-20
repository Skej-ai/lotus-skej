# Generated by Django 4.0.5 on 2023-02-18 21:22

from django.db import migrations


def refresh_mat_views(apps, schema_editor):
    Metric = apps.get_model("metering_billing", "Metric")
    from metering_billing.aggregation.billable_metrics import METRIC_HANDLER_MAP

    for metric in Metric.objects.all():
        handler = METRIC_HANDLER_MAP[metric.metric_type]
        handler.archive_metric(metric)
        metric.mat_views_provisioned = False
        metric.save()

        ## INITADMIN WILL TAKE CARE OF REFRESHING THE VIEWS


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0191_fill_new_uuidfields"),
    ]

    operations = [
        migrations.RunPython(refresh_mat_views, reverse_code=migrations.RunPython.noop),
    ]