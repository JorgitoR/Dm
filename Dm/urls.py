from django.urls import path, re_path

from .views import (

	mensajes_privados,
	DetailMs,
	CanalDetailView
	

)

urlpatterns=[
	
	re_path(r'canal/(?P<pk>[\w-]+)', CanalDetailView.as_view()),
	path("dm/<str:username>", mensajes_privados),
	path("ms/<str:username>", DetailMs.as_view(), name="detailms"),

]