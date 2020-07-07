from .models import MainCourseCategory, MainCourseCategoryAssign, SubCourseCategory, SubCourseCategoryAssign
from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


def my_tag(context):
    context.write("hello world")
    return ''


def main_course_category(self, request_id, course_id):

    try:
        main_cat = MainCourseCategoryAssign.objects.filter(category=request_id, course_id=course_id).count()
    except ObjectDoesNotExist:
        main_cat = None

    return main_cat

def sub_course_category(self, request_id, course_id):

    try:
        sub_cat = SubCourseCategoryAssign.objects.filter(category=request_id, course_id=course_id).count()
    except ObjectDoesNotExist:
        sub_cat = None

    return sub_cat
    #
    # if main_cat:
    #     return main_cat
    # else:
    #     return main_cat

# class MainCourseCategoryView(ListView):
#     model = MainCourseCategoryAssign
#     context_object_name = 'main_course_category_assign'
#     print("aaaaaaaaaaaa")
#     print (context_object_name.__dict__())
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         print("bbbbbbbbbbbbbb")
#         return context
