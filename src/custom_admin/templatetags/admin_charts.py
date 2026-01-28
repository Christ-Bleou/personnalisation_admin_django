import json
from django import template
from django.apps import apps
from django.db.models import Count
from django.db.models.functions import TruncMonth # Pour grouper par mois

register = template.Library()

@register.simple_tag
def get_chart_data(chart_config):
    try:
        # Récupération dynamique du modèle
        Model = apps.get_model(chart_config.app_label, chart_config.model_name)
        
        # On tente de grouper par date de création (champ standard 'date_joined' pour User)
        # Si le champ n'existe pas, on fait un simple compte total
        try:
            queryset = (
                Model.objects.annotate(month=TruncMonth('date_joined'))
                .values('month')
                .annotate(total=Count('id'))
                .order_by('month')
            )
            labels = [obj['month'].strftime('%b %Y') for obj in queryset]
            data = [obj['total'] for obj in queryset]
        except:
            # Fallback si pas de champ de date
            count = Model.objects.count()
            labels = ["Total"]
            data = [count]

        return json.dumps({
            "labels": labels,
            "datasets": [{
                "label": chart_config.title,
                "data": data,
                "backgroundColor": chart_config.background_color,
                "borderColor": chart_config.border_color,
                "borderWidth": 1
            }]
        })
    except Exception as e:
        return json.dumps({"error": str(e)})