
"""UniAfrikaWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from uni import views
from uni.views import HomeView,ABOUT
app_name='uni'

urlpatterns = [
 
    path('', HomeView.as_view()),
   
    
    path('test/',views.test),
    path('about/',ABOUT.as_view()),
    path('report_table/',views.VIEWS_REPORT_TABLE),
    
    path('addForm/',views.AddForm),
    path('update/<int:update_id>/',views.UPDATE_REPORT),
    path('delete/<int:delete_id>/',views.DELETE_REPORT),
    path('report_table/',views.VIEWS_REPORT_TABLE),
    path('report_list/',views.REPORT_LIST),
    path('student_report/<int:student_id>/',views.STUDENT_REPORT),
    path('view/',views.VIEW),
    path('accounts/',include('allauth.urls'))

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
