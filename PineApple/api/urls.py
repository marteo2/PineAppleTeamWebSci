from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('<int:start_time>/<int:end_time>', views.data_list, name='api'),
]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
