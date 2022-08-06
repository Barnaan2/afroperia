from django.contrib import admin
from django.apps import apps

# Register your models here.
# all models that exists are registered.
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
