from django import template
from comments.models import Comment

register = template.Library()

@register.filter
def get_comment(value):
	return len(Comment.objects.all().filter(model_id=value))
