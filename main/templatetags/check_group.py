from django import template
from ..models import Student

register = template.Library()


@register.simple_tag
def check_group(current_user):
    """
    Checks if the current student user belongs to a student group.
    Args: current_user: the id of the current student user.
    """
    if Student.objects.get(user_id=current_user).student_group_id is None:
        return False
    else:
        return True
