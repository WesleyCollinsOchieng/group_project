from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<book_id>[0-9]+)/', views.details, name="details"),
    path('authors', views.authors, name="authors"),
    path('best_books', views.best_books, name="best_books"),
    path('categories', views.categories, name="categories"),
    path('library', views.library, name="library"),
    path('notifications', views.notifications, name="notifications"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)