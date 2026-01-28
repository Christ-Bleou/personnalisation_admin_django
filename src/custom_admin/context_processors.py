from .models import AdminChart

def admin_dashboard_charts(request):
    """
    Injecte les configurations de graphiques dans le contexte de l'admin.
    """
    # On ne charge les données que si on est dans l'admin pour économiser des ressources
    if request.path.startswith('/admin/'):
        return {
            'chart_configs': AdminChart.objects.all()
        }
    return {}