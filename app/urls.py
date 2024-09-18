from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('homenagem/<int:artigo_id>/', views.homenagem, name='homenagem'),
    path('ceo', views.ceo, name='ceo'),
    path('profissionais', views.profissionais, name='profissionais'),
    path('old_profissionais', views.old_profissionais, name='old_profissionais'),
    path('alunos', views.alunos, name='alunos'),
    path('visualizar_certificado', views.visualizar_certificado, name='visualizar_certificado'),
    path('visualizar_certificado_en', views.visualizar_certificado_en, name='visualizar_certificado_en'),
    re_path(r'^.*$', views.index, name='catch_all'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
