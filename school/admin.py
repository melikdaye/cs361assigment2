from django.contrib import admin

# Register your models here.
from school.models import teacher, student, course

admin.site.register(teacher)
admin.site.register(student)
admin.site.register(course)
