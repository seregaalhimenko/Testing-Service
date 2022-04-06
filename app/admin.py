from django.contrib import admin
from app import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 2


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = models.Question
    extra = 1


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class TestInline(admin.TabularInline):
    model = models.Test
    extra = 1


@admin.register(models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [TestInline]


admin.site.register(models.Choice)
