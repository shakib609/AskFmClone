from django.contrib import admin

from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionInline(admin.StackedInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    fieldsets = [
        (None, {'fields': ['text', 'anonymous']}),
        ('Related Users', {'fields': ['asked_by', 'asked_to']}),
    ]
    list_filter = ('time', 'asked_by', 'asked_to')
    search_fields = ('text',)
    list_display = ('text', 'time', 'asked_by', 'asked_to',)


class AnswerAdmin(admin.ModelAdmin):
    # inlines = [QuestionInline],
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Question', {'fields': ['question']}),
    ]
    list_display = ('text', 'answered_at', 'question_id')
    search_fields = ('text',)
    list_filter = ('answered_at',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
