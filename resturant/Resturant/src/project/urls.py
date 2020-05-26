from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('meals/', include('meals.urls')),
    path('blog/', include('blog.urls')),
    path('reserve_table/', include('reservation.urls')),
    path('about/', include('about.urls')),
    path('contactus/', include('contact.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Restaurant AdminPanel"
admin.site.site_title = "Restaurant App Admin "
admin.site.site_index_title = "Welcome to Restaurant AdminPanel "