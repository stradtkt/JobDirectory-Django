import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    skill_level = django_filters.CharFilter(field_name="skill_level", lookup_expr="icontains")
    area = django_filters.CharFilter(field_name="area", lookup_expr="icontains")
    length_gt = django_filters.NumberFilter(name="length", lookup_expr="gt")
    length_lt = django_filters.NumberFilter(name="length", lookup_expr="lt")
    class Meta:
        model = Job
        fields = ['title', 'skill_level', 'pay_type', 'area', 'budget', 'length',]