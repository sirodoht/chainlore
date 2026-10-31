from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from submissions import views
from submissions.review import dashboard

urlpatterns = [
    path('submit/all/', views.submission_list, name='submission-list'),
    path('submit/track/<uuid:reference>/', views.submission_detail, name='submission-detail'),
    path('submit/', views.index, name='submission-index'),
    path('submit/received/<uuid:reference>/', views.received, name='submission-received'),
    path('submit/<str:kind>/', views.submit, name='submission-form'),
    path('admin/review/', admin.site.admin_view(dashboard), name='review-dashboard'),
    path('admin/', admin.site.urls),
    path('_service/health/', views.health, name='service-health'),
]
if settings.DEBUG:
    urlpatterns += static('/assets/', document_root=settings.SITE_ROOT / 'assets')
    urlpatterns += [re_path(r'^(?P<path>.*)$', views.development_site)]
