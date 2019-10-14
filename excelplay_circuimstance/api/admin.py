from django.contrib import admin
from .models import(
    Level,
    CircuimstanceUser,
    AnswerLog,
    Hint,
)
# Register your models here.


class HintsInline(admin.StackedInline):
    model = Hint
    max_num = 30
    extra = 1


class LevelAdmin(admin.ModelAdmin):
    inlines = (HintsInline,)


admin.site.register(Level, LevelAdmin)
admin.site.register(CircuimstanceUser)
admin.site.register(AnswerLog)