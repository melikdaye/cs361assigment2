from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Template, Context
from school.models import teacher


def school(request):
    teachers=teacher.objects.all()
    t = Template("{% for t in teacher %} {{ t.first_name }} {{ t.last_name }}<br> {% endfor %}")
    c = Context({'teacher': teachers})
    html = t.render(c)

    return HttpResponse(html)