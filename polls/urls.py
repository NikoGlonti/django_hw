from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('triangle', views.hypotenuse_of_triangle, name='hypotenuse_of_triangle'),
    path('person', views.create_pers, name='create_pers'),
    path('person/<int:pk>', views.person_pk, name='person_pk'),
    path('send_mail/', views.text_mail, name='text_mail'),

]
