from django.contrib import admin
from blog.models import Recette, Categorie, Member, Ingredient, Commentaire

# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'quantite', 'unit', 'recette')
    list_filter = ('nom', 'recette')
    ordering = ('recette',)
    search_fields = ('nom',)

admin.site.register(Categorie)
admin.site.register(Recette)
admin.site.register(Member)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Commentaire)


# class IngredientInline(admin.TabularInline):
#     model = Ingredient  
    
# @admin.register(Recette)

# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [IngredientInline, ]