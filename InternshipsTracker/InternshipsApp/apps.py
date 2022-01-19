from django.apps import AppConfig


class InternshipsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "InternshipsApp"

    def ready(self):
        import InternshipsApp.signals
