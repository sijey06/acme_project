from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday')


# Регистрация модели Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')  # Укажите, какие поля хотите отображать
    search_fields = ('tag',)       # Добавление поиска по полю tag