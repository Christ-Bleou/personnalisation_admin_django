from django.contrib import admin
from .models import AdminChart

@admin.register(AdminChart)
class AdminChartAdmin(admin.ModelAdmin):
    list_display = ("title", "app_label", "model_name", "chart_type")
    list_filter = ("chart_type", "app_label")
    fieldsets = (
        ("Configuration de base", {"fields": ("title", "chart_type")}),
        ("Source des données", {"fields": ("app_label", "model_name")}),
        ("Apparence", {"fields": ("background_color", "border_color"), "classes": ("collapse",)}),
    )
