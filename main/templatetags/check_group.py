from django import template
from ..models import Student

register = template.Library()


@register.simple_tag
def check_group(current_user):
    if Student.objects.get(user_id=current_user).student_group_id is None:
        return False
    else:
        return True
