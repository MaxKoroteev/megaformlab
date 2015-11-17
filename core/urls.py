from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$',   TemplateView.as_view(template_name='projects.html'), name='projects'),
    url(r'^x/$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^applications/$', TemplateView.as_view(template_name='application_list.html'),       name='application_list'),
    url(r'^application/$',  TemplateView.as_view(template_name='application_detail.html'),     name='application_detail'),
    url(r'^profile/$',      TemplateView.as_view(template_name='profile.html'),                name='profile'),
    url(r'^profile_edit/$', TemplateView.as_view(template_name='profile_edit.html'),           name='profile_edit'),
    url(r'^address/$',      TemplateView.as_view(template_name='address.html'),                name='address'),

    url(r'^lessons/$', TemplateView.as_view(template_name='lessons.html'),                     name='lessons'),
    url(r'^lessons2/$', TemplateView.as_view(template_name='lessons2.html'),                   name='lessons2'),
    url(r'^lessons3/$', TemplateView.as_view(template_name='lessons3.html'),                   name='lessons3'),
    url(r'^lesson/$', TemplateView.as_view(template_name='lesson.html'),                       name='lesson'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'),                         name='login'),
    url(r'^registration/$', TemplateView.as_view(template_name='registration.html'),           name='registration'),
    url(r'^rregistration/$', TemplateView.as_view(template_name='rregistration.html'),         name='rregistration'),
    url(r'^remember_password/$', TemplateView.as_view(template_name='remember_password.html'), name='remember_password'),
    url(r'^settings/$', TemplateView.as_view(template_name='settings.html'), name='settings'),
    url(r'^cards/$', TemplateView.as_view(template_name='cards.html'), name='cards'),
    url(r'^finances/$', TemplateView.as_view(template_name='finances.html'), name='finances'),

    url(r'^new_account/$',  TemplateView.as_view(template_name='new_account.html'),        name='new_account'),
    url(r'^family/$',       TemplateView.as_view(template_name='family.html'),             name='family'),

    url(r'^tutors/$', TemplateView.as_view(template_name='tutor_list.html'),   name='tutor_list'),
    url(r'^tutor/$',  TemplateView.as_view(template_name='tutor_detail.html'), name='tutor_detail'),

    url(r'^dialogs/$',  TemplateView.as_view(template_name='dialog_list.html'), name='dialog_list'),
    url(r'^dialog/$',  TemplateView.as_view(template_name='dialog_detail.html'), name='dialog_detail'),

    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    url(r'^dashboard2/$', TemplateView.as_view(template_name='dashboard2.html'), name='dashboard2'),
    url(r'^dashboard3/$', TemplateView.as_view(template_name='dashboard3.html'), name='dashboard3'),
    url(r'^dashboard4/$', TemplateView.as_view(template_name='dashboard4.html'), name='dashboard4'),
    url(r'^dashboard5/$', TemplateView.as_view(template_name='dashboard5.html'), name='dashboard5'),
    url(r'^dashboard_repetitor/$', TemplateView.as_view(template_name='dashboard_repetitor.html'), name='dashboard_repetitor'),
    url(r'^dashboard_client/$', TemplateView.as_view(template_name='dashboard_client.html'), name='dashboard_client'),
    url(r'^notifications/$', TemplateView.as_view(template_name='notifications.html'), name='notifications'),
    url(r'^my_applications/$', TemplateView.as_view(template_name='my_applications.html'), name='my_applications'),
    url(r'^my_auto/$', TemplateView.as_view(template_name='my_auto.html'), name='my_auto'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hidden/$',    TemplateView.as_view(template_name='back/hidden.html'),    name='area'),

    url(r'^test/$',              TemplateView.as_view(template_name='test.html'),              name='test'),

    # back
    url(r'^b/$',                 TemplateView.as_view(template_name='back/feedback.html'),          name='back'),
    url(r'^colleges/$',          TemplateView.as_view(template_name='back/colleges.html'),          name='colleges'),
    url(r'^college/$',           TemplateView.as_view(template_name='back/college.html'),           name='college'),
    url(r'^schools/$',           TemplateView.as_view(template_name='back/schools.html'),           name='schools'),
    url(r'^subjects/$',          TemplateView.as_view(template_name='back/subjects.html'),          name='subjects'),
    url(r'^subjects2/$',         TemplateView.as_view(template_name='back/subjects2.html'),         name='subjects2'),
    url(r'^divisions/$',         TemplateView.as_view(template_name='back/divisions.html'),         name='divisions'),
    url(r'^additions/$',         TemplateView.as_view(template_name='back/additions.html'),         name='additions'),
    url(r'^areas/$',             TemplateView.as_view(template_name='back/areas.html'),             name='areas'),
    url(r'^area/$',              TemplateView.as_view(template_name='back/area.html'),              name='area'),
    url(r'^repetitor/$',         TemplateView.as_view(template_name='back/repetitor.html'),         name='repetitor'),

    url(r'^repetitor_tasks/$',   TemplateView.as_view(template_name='back/repetitor_tasks.html'),   name='repetitor_tasks'),
    url(r'^repetitor_orders/$',  TemplateView.as_view(template_name='back/repetitor_orders.html'),  name='repetitor_orders'),
    url(r'^repetitor_history/$', TemplateView.as_view(template_name='back/repetitor_history.html'), name='repetitor_history'),
    url(r'^repetitor_calls/$',   TemplateView.as_view(template_name='back/repetitor_calls.html'),   name='repetitor_calls'),
    url(r'^repetitor_view/$',    TemplateView.as_view(template_name='back/repetitor_view.html'),    name='repetitor_view'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
