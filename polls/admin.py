# -*- coding: utf-8 -*-
from polls.models import Poll
from django.contrib import admin
from polls.models import Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): # табличное отображеие данных для уменьшения места на экране
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question"]
    fieldsets = [
        (None,                  {"fields": ["question"]}),
        ("Date information",    {"fields": ["pub_date"], "classes": ["collapse"]}),
        #("Question field",      {"fields": ["question"]}), #именнованое поле question после даты
    ]
    inlines = [ChoiceInline] # подключаем элементы choice

    #отображение элемента Polls
    list_display = ("question", "pub_date", "was_published_today")
    list_filter = ["pub_date"]
    search_fields = ["question"]
    date_hierarchy = "pub_date"



admin.site.register(Poll, PollAdmin)

