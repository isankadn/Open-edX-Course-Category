from django.contrib import admin
from .models import MainCourseCategory, SubCourseCategory, MainCourseCategoryAssign, SubCourseCategoryAssign


class MainCourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SubCourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MainCourseCategoryAssignAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'category',)


class SubCourseCategoryAssignAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'category',)


admin.site.register(MainCourseCategory, MainCourseCategoryAdmin)
admin.site.register(SubCourseCategory, SubCourseCategoryAdmin)
admin.site.register(MainCourseCategoryAssign, MainCourseCategoryAssignAdmin)
admin.site.register(SubCourseCategoryAssign, SubCourseCategoryAssignAdmin)