from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .forms import SearchForm
from models.models import Employee, Position
import requests, xmltodict
from django.db.models import Q

# Create your views here.


class MainView(TemplateView, ContextMixin):
    template_name = 'base.html'
    # try:
    #     events = requests.get("http://127.0.0.1:4444/events").json()
    #     news = xmltodict.parse(requests.get("http://127.0.0.1:4444/news").text)["rss"]["channel"]["item"]
    # except:
    events = []
    news = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm
        context["employees"] = Employee.objects.all()
        context["events"] = self.events
        context["news"] = self.news
        return context

    def post(self, request):
        search_data = request.POST.get("search").strip()

        print(search_data)

        if search_data == "":
            return redirect("/")

        positions = Position.objects.filter(Q(title__contains=search_data))
        positions_id = []
        for position in positions:
            positions_id.append(position.pk)
        employees = Employee.objects.filter(Q(username__contains=search_data) | Q(email__contains=search_data) | Q(work_phone__contains=search_data) | Q(position_id__in=positions_id) | Q(birthday__contains=search_data))

        events = []

        for event in self.events:
            if (str(search_data).lower() in event["title"].lower()) or (search_data.lower() in event["description"].lower()) or (search_data.lower() in event["author"].lower()):
                events.append(event)

        news = []

        for new in self.news:
            if (str(search_data).lower() in new["title"].lower()) or (search_data.lower() in new["description"].lower()) or (search_data.lower() in new["date"].lower()):
                news.append(new)

        context = {
            "form": SearchForm(request.POST),
            "employees": employees,
            "events": events,
            "news": news,
        }

        return render(request=request, template_name=self.template_name, context=context)