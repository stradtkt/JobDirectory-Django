import django_filters
from .models import Job

LENGTH_CHOICES = (
    (1, '1'),
    (3, '3'),
    (6, '6'),
    (12, '12'),
)
BUDGET_CHOICES = (
    (100, '100'),
    (500, '500'),
    (1000, '1,000'),
    (2000, '2,000'),
    (5000, '5,000'),
    (10000, '10,000'),
    (20000, '20,000'),
    (30000, '30,000'),
    (40000, '40,000'),
    (50000, '50,000'),
    (60000, '60,000'),
    (70000, '70,000'),
    (80000, '80,000'),
    (90000, '90,000'),
    (100000, '100,000'),
)
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    skill_level = django_filters.CharFilter(field_name="skill_level", lookup_expr="icontains")
    area = django_filters.CharFilter(field_name="area", lookup_expr="icontains")
    length = django_filters.ChoiceFilter(choices=LENGTH_CHOICES)
    budget = django_filters.ChoiceFilter(choices=BUDGET_CHOICES)
    class Meta:
        model = Job
        fields = ['title', 'skill_level', 'pay_type', 'area', 'budget', 'length',]

        # form = form
        # filter_overrides = {
        #     models.CharField: {
        #         'filter_class': django_filters.CharFilter,
        #         'extra': lambda f: {
        #             'lookup_expr': 'icontains'
        #         },
        #     },
        # }