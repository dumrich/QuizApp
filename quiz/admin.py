from django.contrib import admin
from .models import Quiz, Question, UserAnswer, SaveUserInstance


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'author', 'created',)
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'author', 'created',)
    raw_id_fields = ('author',)
    ordering = ('created',)
    fields = ('name', 'description', 'author', 'slug')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'answer', 'quiz',)
    list_filter = ('quiz', 'question_type',)
    search_fields = ('questions', 'question_type', 'quiz',)


admin.site.register(UserAnswer)


@admin.register(SaveUserInstance)
class SaveUserInstanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'attempt', 'score')
    list_filter = ('user', 'quiz', 'score')
    fields = ('user', 'quiz', 'UserAnswer', 'score')

