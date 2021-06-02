from django import template
from ..models import Student

register = template.Library()


@register.simple_tag
def urlparam(current_user):
    """
    Returns id of the student group of the current student user.
    Args: current_user: the id of the current student user.
    """
    group_id = Student.objects.get(user_id=current_user).student_group_id
    return group_id
