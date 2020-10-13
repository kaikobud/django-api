from django.contrib import admin
from .models import Company, Favourite


class CompanyAdmin(admin.ModelAdmin):
    model = Company


class FavouriteAdmin(admin.ModelAdmin):
    model = Favourite


admin.site.register(Company, CompanyAdmin)
admin.site.register(Favourite, FavouriteAdmin)
