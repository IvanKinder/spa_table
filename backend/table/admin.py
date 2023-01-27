from django.contrib import admin

from table.models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    model = Appeal
