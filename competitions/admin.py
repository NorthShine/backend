from django.contrib import admin
from competitions.models import Competency, CompetencyLevel


@admin.register(CompetencyLevel)
class CompetencyLevelAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name', )


@admin.register(Competency)
class CompetencyAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
