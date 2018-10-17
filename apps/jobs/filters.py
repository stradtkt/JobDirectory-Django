import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    
    class Meta:
        model = Job
        fields = ['title', 'skill_level', 'pay_type', 'area', 'budget', 'length',]