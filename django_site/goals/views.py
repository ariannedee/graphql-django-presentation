from django.shortcuts import render_to_response

# Create your views here.
from goals.models import User, Goal


def index(request, template_name='main.html'):
    user = User.objects.get(id=request.user.id)
    objectives = Goal.objects.filter(owner=user)
    context = {'user':user, 'objectives': objectives}

    return render_to_response(template_name, context)