from django.apps import AppConfig


class QalogConfig(AppConfig):
    name = 'qalog'

    def ready(self):
        from autoproc import scheduler
        scheduler.start()
