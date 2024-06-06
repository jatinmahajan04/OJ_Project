from django.contrib import admin
from problems.models import Problem, Solution, Testcase

class ProblemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution)
admin.site.register(Testcase)