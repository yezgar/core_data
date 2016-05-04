from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^userData/$', views.userData, name='userData'),
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#    url(r'^(?P<user_profile>[0-9]+)/userData/$', views.userData, name='userData'),
#   http://localhost:8000/tyquy/userData/123/
    url(r'^userData/(?P<facebook_profile_id>[0-9]+)/$', views.userData, name='userData'),
#   http://localhost:8000/tyquy/createUser/7179401/Yezid/Alejandro/Garcia/YAG/    
    url(r'^createUser/(?P<facebook_profile_id>(\w+))/(?P<first_name>(\w+))/(?P<middle_name>(\w+))/(?P<last_name>(\w+))/(?P<full_name>(\w+))/', views.createUser, name='createUser'),
#   http://localhost:8000/tyquy/createComment/123/Aquimico/Chevere/
    url(r'^createComment/(?P<user_id>(\w+))/(?P<application>(\w+))/(?P<description>(\w+))/', views.createComment, name='createComment'),       
    url(r'^saveUserSession/(?P<user_id>(\w+))/(?P<session_id>(\w+))/(?P<feedback_level>(\w+))/(?P<feedback>(\w+))/', views.saveUserSession, name='saveUserSession'),
    
]