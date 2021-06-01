from django import template
from ..models import Student

register = template.Library()


@register.simple_tag
def urlparam(current_user):
    group_id = Student.objects.get(user_id=current_user).student_group_id
    return group_id
