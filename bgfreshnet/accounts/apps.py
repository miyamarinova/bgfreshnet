from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bgfreshnet.accounts'

    def ready(self):
        import bgfreshnet.accounts.signals