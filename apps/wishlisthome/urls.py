from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="my_w_home" ),
    url(r'^ create$', views.create, name="my_w_create"),
    url(r'^ update$', views.update, name="my_w_update"),
    url(r'^ add_item//(?P<id>\d+)$', views.add, name="my_w_add"),
    url(r'^ remove_item//(?P<id>\d+)$', views.remove, name="my_w_remove"),
    url(r'^ delete_item//(?P<id>\d+)$', views.delete, name="my_w_delete"),
    url(r'^ view_item//(?P<id>\d+)$', views.view, name="my_w_view"),
    # url(r'^login$', views.login, name="my_login"),
    url(r'^ logout$', views.logout, name="my_w_logout"),
]
