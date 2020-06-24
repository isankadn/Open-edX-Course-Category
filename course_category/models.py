from django.conf import settings
from django.db import models
from django.utils import timezone


class MainCourseCategory(models.Model):
    name = models.CharField(verbose_name="Main Category Name", max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Main Course Category'
        verbose_name_plural = 'Main Course Categories'

    def __str__(self):
        return self.name


class SubCourseCategory(models.Model):
    name = models.CharField(verbose_name="Sub Category Name", max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Sub Course Category'
        verbose_name_plural = 'Sub Course Categories'

    def __str__(self):
        return self.name


class MainCourseCategoryAssign(models.Model):
    course_id = models.CharField(verbose_name="Main Category Name", max_length=100, null=True)
    category = models.ForeignKey(MainCourseCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course_id', 'category')

    def __str__(self):
        return self.course_id


class SubCourseCategoryAssign(models.Model):
    course_id = models.CharField(verbose_name="Sub Category Name", max_length=100, null=True)
    category = models.ForeignKey(SubCourseCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course_id', 'category')

    def __str__(self):
        return self.course_id
