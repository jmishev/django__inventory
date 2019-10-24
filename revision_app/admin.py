from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Goods


class ViewAdmin(ImportExportMixin):
    class Meta:
        model = Goods


admin.site.register(Goods)


