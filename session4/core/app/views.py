from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .forms import SearchForm, VCardForm
from models.models import Employee, Position
import requests, xmltodict, qrcode
from django.db.models import Q
from core.settings import BASE_DIR

# Create your views here.


class MainView(TemplateView, ContextMixin):
    template_name = 'base.html'
    try:
        events = requests.get("http://127.0.0.1:4444/events").json()
        news = xmltodict.parse(requests.get("http://127.0.0.1:4444/news").text)["rss"]["channel"]["item"]
    except:
        events = []
        news = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        employees = Employee.objects.all()
        vcard_forms = [VCardForm(initial={"full_name": emp.username}) for emp in employees]

        context["form"] = SearchForm
        context["employees_and_forms"] = zip(employees, vcard_forms)
        context["events"] = self.events
        context["news"] = self.news
        return context

    def post(self, request):
        news = []
        events = []

        context = {}

        if "full_name" in request.POST:
            employees = Employee.objects.all()

            employee_obj = Employee.objects.get(username=request.POST["full_name"])

            qr_vcard_text = f'''BEGIN:VCARD
VERSION:3.0
N:{employee_obj.first_name}
FN:{employee_obj.last_name}
ORG:{employee_obj.organization}
TITLE:{employee_obj.position_id}
TEL;WORK;VOICE:{employee_obj.work_phone}
TEL;CELL:{employee_obj.work_phone}
EMAIL;WORK;INTERNET:{employee_obj.email}
END:VCARD
'''
            
            qr =  qrcode.make(qr_vcard_text)
            qr.save(f"{BASE_DIR}/media/qrcodes/{employee_obj.username}_vcard.png")
            context["qr_vcard_path"] = f"/media/qrcodes/{employee_obj.username}_vcard.png"
            context["events"] = self.events
            context["news"] = self.news

        elif "search" in request.POST:
            search_data = request.POST.get("search").strip()

            if search_data == "":
                return redirect("/")

            positions = Position.objects.filter(Q(title__contains=search_data))
            positions_id = []
            for position in positions:
                positions_id.append(position.pk)
            employees = Employee.objects.filter(Q(username__contains=search_data) | Q(email__contains=search_data) | Q(work_phone__contains=search_data) | Q(position_id__in=positions_id) | Q(birthday__contains=search_data))

            for event in self.events:
                if (str(search_data).lower() in event["title"].lower()) or (search_data.lower() in event["description"].lower()) or (search_data.lower() in event["author"].lower()):
                    events.append(event)

            for new in self.news:
                if (str(search_data).lower() in new["title"].lower()) or (search_data.lower() in new["description"].lower()) or (search_data.lower() in new["date"].lower()):
                    news.append(new)

            if len(employees) == 0 and len(events) == 0 and len(news) == 0:
                context["nothing"] = True

            context["events"] = events
            context["news"] = news

        vcard_forms = [VCardForm(initial={"full_name": emp.username}) for emp in employees]

        context["form"] = SearchForm(request.POST)
        context["employees_and_forms"] = zip(employees, vcard_forms)

        return render(request=request, template_name=self.template_name, context=context)