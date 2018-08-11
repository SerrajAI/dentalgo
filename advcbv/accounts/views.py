
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)


from django.db.models import Q

from django.http import HttpResponseRedirect
from django.utils import translation

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#
from . import forms
from . import models
from accounts.models import Patient,Operation,Appointment
from accounts.forms import PatientCreateForm,AppointmentCreateForm,OperationCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from . import views
# Create your views here.



class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url= reverse_lazy('login')
    template_name = 'accounts/signup.html'



class PatientListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Patient

    paginate_by = 2  # if pagination is desired

    template_name = 'accounts/patient_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'patients'  # Default: object_list
    # queryset = Patient.objects.filter(id = current_user.id)  # Default: Model.objects.all()
    def get_queryset(self): # override this to get custom list of objects

        q = Patient.objects.filter(created_by=self.request.user)
        q.order_by('-fullname')
        return q




class PatientDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'login'
    context_object_name = 'patient_details'
    model = models.Patient
    template_name = 'accounts/patient_detail.html'





class PatientCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    form_class = PatientCreateForm
    # fields = "fullname","cin","civility","phone","assurance","profession","special","profile_picture"
    model = models.Patient
    success_url = reverse_lazy("accounts:list")
    # def form_valid(self, form):
    #     # # school = get_object_or_404(School, slug=self.kwargs['school'])
    #     # form.instance.school = request.user
    #     # return super(StudentCreateView, self).form_valid(form)
    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.created_by = self.request.user
        return super(PatientCreateView, self).form_valid(form)






class PatientUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    fields = ("fullname","cin","phone","assurance","profession")
    model = models.Patient
    success_url = reverse_lazy("accounts:list")


class PatientDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Patient
    success_url = reverse_lazy("accounts:list")

# def something(request):
#     context_instance = RequestContext(request)
#     template_name = 'your_template.html'
#     extra_context = { 'other_variable': 'some value' }
#     return render_to_response(template_name, extra_context, context_instance)



# @login_required(login_url="/accounts/login/")
def search(request):

    template_name='accounts/results.html'

    query=request.GET.get('q')
    if query:
        res= Patient.objects.filter(created_by=request.user)
        res= Patient.objects.filter(Q(fullname__icontains=query))

    else:
        res= Patient.objects.filter(created_by=request.user)

    result_list = res
    page = request.GET.get('page', 1)

    paginator = Paginator(result_list, 2)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)


    return render(request,template_name,{ 'results': results })




# class CBView(View):
#     def get(self,request):
#         return HttpResponse('Class Based Views are Cool!')

# ********************************************************************************APPOINTMENT VIEWS********************************************************************************************************


class AppointmentListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Appointment

    paginate_by = 10  # if pagination is desired

    template_name = 'accounts/appointment_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'appointments'  # Default: object_list

    def get_queryset(self): # override this to get custom list of objects

        q = Appointment.objects.filter(created_by=self.request.user)
        q.order_by('-day')
        q.order_by('-time')
        return q
    # queryset = Patient.objects.filter(id = current_user.id)  # Default: Model.objects.all()
    # def get_queryset(self): # override this to get custom list of objects
    #
    #     q = Appointment.objects.filter(doctor=self.request.user)
    #     q.order_by('-fullname')
    #     return q

    # def get_queryset(self): # override this to get custom list of objects
    #
    #     q = Patient.objects.filter(doctor=self.request.user)
    #     q.order_by('-fullname')
    #     return q


class AppointmentDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'login'
    context_object_name = 'appointment_details'
    model = models.Appointment
    template_name = 'accounts/appointment_detail.html'


class AppointmentCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'



    form_class = AppointmentCreateForm

    # fields = "fullname","cin","civility","phone","assurance","profession","special","profile_picture"
    model = models.Appointment
    success_url = reverse_lazy("accounts:listapp")



    def get_form(self, *args, **kwargs):                                                           # SO FKIN IMPORTANT HOLYSHIT WTF FILTER FOREIGN KEY SHIT BASED ON LOGGED IN USER
        form = super(AppointmentCreateView, self).get_form(*args, **kwargs)
        form.fields['patient'].queryset = Patient.objects.filter(created_by=self.request.user)
        return form



    # def get_form_kwargs(self):
    #     kwargs = super(AppointmentCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


    def form_valid(self, form): #by default the creator of the appointment is the current user
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.created_by = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

            # def form_valid(self, form):
            #     if form.is_valid():
            #         roote = restaurant.objects.filter(owner =self.request.user)
            #         instance = form.save(commit=False)
            #         instance.owner = self.request.user
            #     return super(ItemCreate, self).form_valid(form)

    # def form_valid(self, form):
    #     # # school = get_object_or_404(School, slug=self.kwargs['school'])
    #     # form.instance.school = request.user
    #     # return super(StudentCreateView, self).form_valid(form)
    # def form_valid(self, form):
    #     """
    #     Called if all forms are valid. Creates a Recipe instance along with
    #     associated Ingredients and Instructions and then redirects to a
    #     success page.
    #     """
    #     form.instance.doctor = self.request.user
    #     return super(PatientCreateView, self).form_valid(form)






class AppointmentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    fields = ("patient","day","time","special","position")
    model = models.Appointment
    success_url = reverse_lazy("accounts:listapp")

class AppointmentDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Appointment
    success_url = reverse_lazy("accounts:listapp")

# def something(request):
#     context_instance = RequestContext(request)
#     template_name = 'your_template.html'
#     extra_context = { 'other_variable': 'some value' }
#     return render_to_response(template_name, extra_context, context_instance)



# def search(request):
#
#     template_name='accounts/results.html'
#
#     query=request.GET.get('q')
#     if query:
#         res= Patient.objects.filter(doctor=request.user)
#         res= Patient.objects.filter(Q(fullname__icontains=query))
#
#     else:
#         res= Patient.objects.filter(doctor=request.user)
#
#     result_list = res
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(result_list, 10)
#     try:
#         results = paginator.page(page)
#     except PageNotAnInteger:
#         results = paginator.page(1)
#     except EmptyPage:
#         results = paginator.page(paginator.num_pages)
#
#
#     return render(request,template_name,{ 'results': results })
#
# # class CBView(View):
# #     def get(self,request):
# #         return HttpResponse('Class Based Views are Cool!')





# ************************************************************************************************** operation views*****************************************************************************



class OperationListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Operation

    paginate_by = 10  # if pagination is desired

    template_name = 'accounts/operation_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'operations'  # Default: object_list
    # queryset = Patient.objects.filter(id = current_user.id)  # Default: Model.objects.all()
    # def get_queryset(self): # override this to get custom list of objects
    #
    #     q = Appointment.objects.filter(doctor=self.request.user)
    #     q.order_by('-fullname')
    #     return q

    # def get_queryset(self): # override this to get custom list of objects
    #
    #     q = Patient.objects.filter(doctor=self.request.user)
    #     q.order_by('-fullname')
    #     return q
    def get_queryset(self): # override this to get custom list of objects

        q = Operation.objects.filter(created_by=self.request.user)
        q.order_by('-day')
        q.order_by('-time')
        return q

class OperationDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'login'
    context_object_name = 'operation_details'
    model = models.Operation
    template_name = 'accounts/operation_detail.html'


class OperationCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    form_class = OperationCreateForm
    # fields = "fullname","cin","civility","phone","assurance","profession","special","profile_picture"
    model = models.Operation
    success_url = reverse_lazy("accounts:listop")
    def get_form(self, *args, **kwargs):                                                           # SO FKIN IMPORTANT HOLYSHIT WTF FILTER FOREIGN KEY SHIT BASED ON LOGGED IN USER
        form = super(OperationCreateView, self).get_form(*args, **kwargs)
        form.fields['patient'].queryset = Patient.objects.filter(created_by=self.request.user)
        form.fields['appointment'].queryset = Appointment.objects.filter(created_by=self.request.user)

        return form

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.created_by = self.request.user
        return super(OperationCreateView, self).form_valid(form)
    # def form_valid(self, form):
    #     # # school = get_object_or_404(School, slug=self.kwargs['school'])
    #     # form.instance.school = request.user
    #     # return super(StudentCreateView, self).form_valid(form)
    # def form_valid(self, form):
    #     """
    #     Called if all forms are valid. Creates a Recipe instance along with
    #     associated Ingredients and Instructions and then redirects to a
    #     success page.
    #     """
    #     form.instance.doctor = self.request.user
    #     return super(PatientCreateView, self).form_valid(form)






class OperationUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    fields = ("fullname","patient","appointment","day","time","special","price","advance","rest",)
    model = models.Operation
    success_url = reverse_lazy("accounts:listop")

class OperationDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = models.Operation
    success_url = reverse_lazy("accounts:listop")

# def something(request):
#     context_instance = RequestContext(request)
#     template_name = 'your_template.html'
#     extra_context = { 'other_variable': 'some value' }
#     return render_to_response(template_name, extra_context, context_instance)



# def search(request):
#
#     template_name='accounts/results.html'
#
#     query=request.GET.get('q')
#     if query:
#         res= Patient.objects.filter(doctor=request.user)
#         res= Patient.objects.filter(Q(fullname__icontains=query))
#
#     else:
#         res= Patient.objects.filter(doctor=request.user)
#
#     result_list = res
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(result_list, 10)
#     try:
#         results = paginator.page(page)
#     except PageNotAnInteger:
#         results = paginator.page(1)
#     except EmptyPage:
#         results = paginator.page(paginator.num_pages)
#
#
#     return render(request,template_name,{ 'results': results })
#
# # class CBView(View):
# #     def get(self,request):
# #         return HttpResponse('Class Based Views are Cool!')
