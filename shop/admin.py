from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.

admin.site.site_header = "Tech-Shop en ligne"
admin.site.site_title = "Tech-Shop"
admin.site.index_title = "Manageur"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_category', 'date_added')  # Utiliser 'get_category'
    search_fields = ('title',)

    def get_category(self, obj):
        return obj.category.name  # Remplacez 'category' par le nom réel de votre champ de catégorie

    get_category.short_description = 'Category'  # Libellé de l'en-tête dans l'interface admin

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'tel', 'ville', 'pays', 'total', 'date_commande')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
