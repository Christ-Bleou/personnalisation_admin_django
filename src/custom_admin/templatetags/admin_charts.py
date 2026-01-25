import json
from django import template
from django.apps import apps
from django.db.models import Count

register = template.Library()

@register.simple_tag
def get_chart_data(chart_config):
    try:
        Model = apps.get_model(chart_config.app_label, chart_config.model_name)
        queryset = Model.objects.all().annotate(total=Count("id"))
        labels = ["Total"]  # Simplifié pour test
        data = [queryset[0].total if queryset else 0]
        return json.dumps({
            "labels": labels,
            "datasets": [{"label": chart_config.title, "data": data, "backgroundColor": chart_config.background_color}]
        })
    except Exception as e:
        return json.dumps({"error": str(e)})
