from django.apps import AppConfig


class internships_appConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "internships_app"

    def ready(self):
        import internships_app.signals
