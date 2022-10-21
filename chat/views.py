from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

# Create your views here.


class IndexView(TemplateView):
    template_name = 'chat/index.html'


class ChatView(View):
    template_name = 'chat/index.html'


    def get(self, request):
        group_name = request.GET.get('group-name')
        print(group_name)
        context = {'group_name': group_name}

        return render(request, self.template_name, context)
