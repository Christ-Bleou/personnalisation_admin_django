from django.db import models

class AdminChart(models.Model):
    CHART_TYPES = [("bar", "Bar Chart"), ("line", "Line Chart"), ("pie", "Pie Chart")]
    title = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    chart_type = models.CharField(max_length=20, choices=CHART_TYPES, default="bar")
    background_color = models.CharField(max_length=20, default="rgba(54, 162, 235, 0.2)")
    border_color = models.CharField(max_length=20, default="rgba(54, 162, 235, 1)")

    def __str__(self):
        return self.title
