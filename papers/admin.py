from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from .models import Paper


class PaperResource(resources.ModelResource):
    microsoft_pid = Field(
        attribute='microsoft_pid',
        column_name='Microsoft Academic Paper ID'
    )
    coevidence = Field(attribute='coevidence', column_name='WHO #Covidence')

    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = Paper


@admin.register(Paper)
class PaperAdmin(ImportExportModelAdmin):
    resource_class = PaperResource
