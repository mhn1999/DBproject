from django.urls import path
from . import views

urlpatterns = [
#	path('', views.apiOverview, name="api-overview"),
	path('child-list/', views.AllChildList.as_view(), name="child-list"),
	path('child-information/<str:pk>/', views.ChildInformation.as_view(), name="child-information"),
    path('person-list/', views.AllParentList.as_view(), name="child-list"),
	path('person-information/<str:pk>/', views.ParentInformation.as_view(), name="child-information"),
    path('class-list/', views.AllClassList.as_view(), name="child-list"),
	path('class-information/<str:pk>/', views.ClassInformation.as_view(), name="child-information"),
	path('teacher-list/', views.AllTeacherList.as_view(), name="child-list"),
	path('teacher-information/<str:pk>/', views.TeacherInformation.as_view(), name="child-information"),
	path('child-create/', views.ChildCreate.as_view(), name="child-create"),
	path('class-update/<str:pk>/', views.ClassUpdate.as_view(), name="class-update"),
	path('class-create/', views.ClassCreate.as_view(), name="book-delete"),
]