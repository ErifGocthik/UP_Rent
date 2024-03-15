import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from rent_app.forms import RequestCreateForm, PropertyCreateForm
from rent_app.models import Property, Request, Renter


def root_view(request):
    user = User
    return render(request, 'root.html', {'user': user})


class PropertyListView(ListView):
    paginate_by = 9
    model = Property
    context_object_name = 'property'
    template_name = 'main.html'

    def form_valid(self, request):
        cd = request.POST['search-field']
        model = Property.objects.filter(address__contains=cd)
        context = {'property': model}
        return context


    def post(self, request):
        return render(request, self.template_name, self.form_valid(request))


class PropertyDetailView(DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'property_detail.html'


class RequestFormView(CreateView):
    model = Property
    form_class = RequestCreateForm
    template_name = 'request_form.html'

    def get_context_data(self, pk: int):
        property = get_object_or_404(Property, pk=pk)
        form = self.form_class()
        return {'property': property, 'form': form}

    def get(self, request, pk: int):
        return render(request, self.template_name, self.get_context_data(pk))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        property = get_object_or_404(Property, pk=self.kwargs['pk'])
        request = form.save(commit=False)
        request.property = property
        request.user = self.request.user
        request.save()

        return redirect(reverse_lazy('rent_app:main'))


class RequestsListView(ListView):
    model = Request
    template_name = 'moderator/request.html'
    context_object_name = 'requests'

    def get_context_data(self, **kwargs):
        self_requests = self.model.objects.filter(property__renter__director=self.request.user)
        return {'requests': self_requests}


class RequestDetailView(DetailView):
    model = Request
    template_name = 'moderator/request-detail.html'
    context_object_name = 'request'

    def get_context_data(self, **kwargs):
        model = get_object_or_404(Request, pk=self.kwargs['pk'])
        context = {'user': model.user.username,
                   'name': model.name,
                   'surname': model.surname,
                   'patronymic': model.patronymic,
                   'phone_number': model.phone_number,
                   'email': model.email,
                   'created_at': model.created_at}
        return context

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_context_data())


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyCreateForm
    template_name = 'property_creation_form.html'
    success_url = reverse_lazy('rent_app:main')

    def get_context_data(self, **kwargs):
        form = self.get_form()
        return {'form': form}

    def get(self, request):
        if not self.request.user.is_authenticated:
            return redirect(reverse_lazy('auth:sign_in'))
        else:
            return render(request, self.template_name, self.get_context_data())

    def form_valid(self, form):
        renter = get_object_or_404(Renter, director=self.request.user.id)
        form = self.get_form()
        form = form.save(commit=False)
        form.renter = renter
        form.save()

        return redirect(reverse_lazy('rent_app:main'))

def request_denied_view(request, pk):
    model = get_object_or_404(Request, pk=pk)
    model.status = 0
    model.save()
    return redirect(reverse_lazy('rent_app:requests'))


def request_accept_view(request, pk):
    model = get_object_or_404(Request, pk=pk)
    model.status = 2
    model.save()
    return redirect(reverse_lazy('rent_app:requests'))


class RentersListView(ListView):
    model = Renter
    context_object_name = 'renters'
    template_name = 'personal/renters.html'