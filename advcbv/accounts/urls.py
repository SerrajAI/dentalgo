from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'accounts'

urlpatterns = [
    url(r'^$',views.PatientListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.PatientDetailView.as_view(),name='detail'),
    url(r'^results/(?P<pk>\d+)/$',views.PatientDetailView.as_view(),name='detail'),
    url(r'^create/$',views.PatientCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.PatientUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.PatientDeleteView.as_view(),name='delete'),


    #
    url(r'^app$',views.AppointmentListView.as_view(),name='listapp'),
    url(r'^app/(?P<pk>\d+)/$',views.AppointmentDetailView.as_view(),name='detailapp'),
    # url(r'^app/results/(?P<pk>\d+)/$',views.AppointmentDetailView.as_view(),name='detail'),
    url(r'^app/create/$',views.AppointmentCreateView.as_view(),name='createapp'),
    url(r'^app/update/(?P<pk>\d+)/$',views.AppointmentUpdateView.as_view(),name='updateapp'),
    url(r'^app/delete/(?P<pk>\d+)/$',views.AppointmentDeleteView.as_view(),name='deleteapp'),








url(r'^ops$',views.OperationListView.as_view(),name='listop'),
url(r'^op/(?P<pk>\d+)/$',views.OperationDetailView.as_view(),name='detailop'),
# url(r'^app/results/(?P<pk>\d+)/$',views.AppointmentDetailView.as_view(),name='detail'),
url(r'^op/create/$',views.OperationCreateView.as_view(),name='createop'),
url(r'^op/update/(?P<pk>\d+)/$',views.OperationUpdateView.as_view(),name='updateop'),
url(r'^op/delete/(?P<pk>\d+)/$',views.OperationDeleteView.as_view(),name='deleteop'),







    url(r"login/$",auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    # url(r"^$", views.PatientListView.as_view(), name="list"),
    url(r'^$',views.PatientListView.as_view(),name='list'),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r'^results/$',views.search,name='results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
