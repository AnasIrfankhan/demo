from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# from .views import CustomTokenObtainPairView


from . import views

# # from views import StudentModelViewSet


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('Students/',views.StudentModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('User/',views.userviews),
    path('role/',views.role_view),
    path('User2/',views.User_View),
    path('Emp/',views.Employer_view),
    path('Manager/',views.Manager_view),
    path('user/',views.UserModelViewSet.as_view({'get': 'list'})),
    path('Password/',views.changed_password),
    path('send_otp/',views.reset_password),
    path('reset_Password/',views.forgot_Password),






    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('Refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),


]





# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet, obtain_token

# router = DefaultRouter()
# router.register(r'students', StudentViewSet, basename='student')

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Add admin URL here
#     path('api/', include(router.urls)),
#     path('api/token/', obtain_token, name='token_obtain_pair'),
# ]






 