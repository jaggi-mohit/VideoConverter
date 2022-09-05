from django.apps import AppConfig


class EditappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'editapp'
    def ready(self):
        import editapp.signals