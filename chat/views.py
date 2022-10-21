from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Group, Chat

# Create your views here.


class IndexView(TemplateView):
    template_name = 'chat/index.html'


class ChatView(View):
    template_name = 'chat/index.html'


    def get(self, request):
        group_name = request.GET.get('group-name')

        group_obj, created = Group.objects.get_or_create(name=group_name)

        if created == True:
            old_messages = Chat.objects.none()
        else:
            old_messages = Chat.objects.filter(group=group_obj)

        context = {
            'group_name': group_name,
            'old_messages': old_messages
        }

        return render(request, self.template_name, context)
