# from django.urls import path
# from . import views
#
# urlpatterns = [
#     # المسار لعرض البيانات الطبية
#     path ('health-data/', views.HealthDataAPIView.as_view (), name='health_data_list'),
#
#     # المسار للتنبؤ بالحالة الصحية
#     path ('health/', views.HealthPredictionAPIView.as_view (), name='health_prediction'),
# ]
#
# ------------------------------------------
# from django.urls import path
# from .views import HealthDataListCreateView, HealthPredictionAPIView
#
# urlpatterns = [
#     # المسار لعرض البيانات الطبية (GET) وإنشاء بيانات جديدة (POST)
#     path('health-data/', HealthDataListCreateView.as_view(), name='health-data-list-create'),
#     # path ('health-data/', views.health_data_list, name='health_data_list'),  # هذا المسار موجود
#     # المسار للتنبؤ بالحالة الصحية بناءً على البيانات المرسلة
#     path('health/', HealthPredictionAPIView.as_view(), name='health-prediction'),
# ]
# ---------------------------------------------------
# شغاللللللل
# from django.urls import path
# from .views import HealthDataListCreateView, HealthPredictionAPIView
#
# urlpatterns = [
#     # المسار لعرض البيانات الطبية (GET) وإنشاء بيانات جديدة (POST)
#     path ('health-data/', HealthDataListCreateView.as_view (), name='health-data-list-create'),
#     path ('health-data/', HealthDataListCreateView.as_view (), name='health_data_list'),  # تعديل الاسم هنا
#
#     # المسار للتنبؤ بالحالة الصحية بناءً على البيانات المرسلة
#     path ('health/predict/', HealthPredictionAPIView.as_view (), name='health-prediction'),
# ]
# --------------------333

# from django.urls import path
# from .views import HealthDataListCreateView, HealthPredictionAPIView, RegisterView, LoginView
#
# urlpatterns = [
#     path('health-data/', HealthDataListCreateView.as_view(), name='health_data_list_create'),
#     path('predict/', HealthPredictionAPIView.as_view(), name='health_prediction'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
# ]


# from django.urls import path
# from .views import HealthDataListCreateView, HealthPredictionAPIView, RegisterView, LoginView
#
# # تعريف app_name لتمكين استخدام namespace
# app_name = 'health'
#
# urlpatterns = [
#     path ('health-data/', HealthDataListCreateView.as_view (), name='health_data_list_create'),
#     path ('predict/', HealthPredictionAPIView.as_view (), name='health_prediction'),
#     path ('register/', RegisterView.as_view (), name='register'),
#     path ('login/', LoginView.as_view (), name='login'),
# ]


# from django.urls import path
# from .views import RegisterView, LoginView, HealthDataListCreateView, HealthPredictionAPIView
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('health-data/', HealthDataListCreateView.as_view(), name='health-data-list-create'),
#     path('predict-health/', HealthPredictionAPIView.as_view(), name='predict-health'),
# ]


# from django.urls import path
# from .views import RegisterView, LoginView, HealthDataListCreateView, HealthPredictionAPIView
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('health-data/', HealthDataListCreateView.as_view(), name='health-data-list-create'),
#     path('predict-health/', HealthPredictionAPIView.as_view(), name='predict-health'),
#     # path ('health-data/', views.health_data_list_create, name='health_data_list_create'),
#     # إضافة مسار alias جديد
#     path('data/', HealthDataListCreateView.as_view(), name='health-data-alias'),
# ]
# =============================================================================================
# اهم كود شغااااال
# from django.urls import path
# from .views import RegisterView, LoginView, HealthDataListCreateView, HealthPredictionAPIView
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('health-data/', HealthDataListCreateView.as_view(), name='health-data-list-create'),
#     path('predict-health/', HealthPredictionAPIView.as_view(), name='predict-health'),
#     path('data/', HealthDataListCreateView.as_view(), name='health-data-alias'),
# ]


# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import (
#     RegisterView,
#     LoginView,
#     HealthDataListCreateView,
#     HealthPredictionAPIView,
#     login_view,
#     home_view,
# )
#
# urlpatterns = [
#     # مسار تسجيل مستخدم جديد
#     path('register/', RegisterView.as_view(), name='register'),
#
#     # مسار تسجيل الدخول باستخدام API
#     path('login-api/', LoginView.as_view(), name='login_api'),
#
#     # مسار تسجيل الدخول باستخدام HTML Template
#     path('login/', login_view, name='login'),
#
#     # مسار تسجيل الخروج
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#
#     # مسار الصفحة الرئيسية بعد تسجيل الدخول
#     path('home/', home_view, name='home'),
#
#     # مسار عرض البيانات الصحية أو إضافتها
#     path('health-data/', HealthDataListCreateView.as_view(), name='health_data_list_create'),
#
#     # مسار إضافي لعرض البيانات الصحية (اختياري بناءً على الطلب)
#     path('data/', HealthDataListCreateView.as_view(), name='health_data_list_create_alt'),
#
#     # مسار التنبؤ بالحالات الصحية
#     path('predict/', HealthPredictionAPIView.as_view(), name='health_prediction'),
# ]
# ===================================================================================
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import (
#     get_health_data,
#     RegisterView,
#     LoginView,
#     HealthDataListCreateView,
#     HealthPredictionAPIView,
#     login_view,
#     home_view,
#     upload_files_view,
# )
#
# urlpatterns = [
#     # مسار تسجيل مستخدم جديد
#     path('register/', RegisterView.as_view(), name='register'),
#
#     # مسار تسجيل الدخول باستخدام API
#     path('login-api/', LoginView.as_view(), name='login_api'),
#
#     # مسار تسجيل الدخول باستخدام HTML Template
#     path('login/', login_view, name='login'),
#
#     # مسار تسجيل الخروج
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#
#     # مسار الصفحة الرئيسية بعد تسجيل الدخول
#     path('home/', home_view, name='home'),
#
#     # مسار عرض البيانات الصحية أو إضافتها
#     path('health-data/', HealthDataListCreateView.as_view(), name='health_data_list_create'),
#
#     # مسار إضافي لعرض البيانات الصحية (اختياري بناءً على الطلب)
#     path('data/', HealthDataListCreateView.as_view(), name='health_data_list_create_alt'),
#
#     # مسار استدعاء البيانات الصحية عبر دالة `get_health_data`
#     path('get-health-data/', get_health_data, name='get_health_data'),
#
#     # مسار التنبؤ بالحالات الصحية
#     path('predict/', HealthPredictionAPIView.as_view(), name='health_prediction'),
#
#     # مسار رفع الملفات من مجلد
#     path('upload/', upload_files_view, name='upload_file'),  # رفع الملف
# ]

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import (
#     import_data_from_airtable,
#     login_view,
#     HealthDataListCreateView,
#     HealthPredictionAPIView,
#     upload_files_view,
#     AiModelsAPIView,
#     get_health_data,
#     RegisterView,
#     LoginView,
#     home_view,
#     AIModelsListCreateView,  # لإدارة نموذج AIModels
#     AiModelsList,  # عرض قائمة النماذج
# )
#
# urlpatterns = [
#     # مسار تسجيل مستخدم جديد
#     path("register/", RegisterView.as_view(), name="register"),
#     # مسار تسجيل الدخول باستخدام API
#     path("login-api/", LoginView.as_view(), name="login_api"),
#     # مسار تسجيل الدخول باستخدام HTML Template
#     path("login/", login_view, name="login"),
#     # مسار تسجيل الخروج
#     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
#     # مسار الصفحة الرئيسية بعد تسجيل الدخول
#     path("home/", home_view, name="home"),
#     # مسار عرض البيانات الصحية أو إضافتها
#     path(
#         "health-data/",
#         HealthDataListCreateView.as_view(),
#         name="health_data_list_create",
#     ),
#     # مسار إضافي لعرض البيانات الصحية (اختياري بناءً على الطلب)
#     path(
#         "data/", HealthDataListCreateView.as_view(), name="health_data_list_create_alt"
#     ),
#     # مسار استدعاء البيانات الصحية عبر دالة `get_health_data`
#     path("get-health-data/", get_health_data, name="get_health_data"),
#     # مسار التنبؤ بالحالات الصحية
#     path("predict/", HealthPredictionAPIView.as_view(), name="health_prediction"),
#     # مسار رفع الملفات من مجلد
#     path("upload/", upload_files_view, name="upload_file"),
#     # مسار عرض أو إنشاء AIModels
#     path("ai-models/", AIModelsListCreateView.as_view(), name="ai_models_list_create"),
#     # مسار عرض النماذج AI
#     path("ai-models-list/", AiModelsList.as_view(), name="ai_models_list"),
#     # مسار استيراد البيانات من Airtable
#     path("import/", import_data_from_airtable, name="import_data"),
#     # مسار عرض التنبؤ باستخدام AIModels
#     path("ai-models/", AiModelsAPIView.as_view(), name="ai_models"),
# ]


from django.urls import path
from django.contrib.auth import views as auth_views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProtectedDataView
from .views import (
    get_health_data,
    RegisterView,
    LoginView,
    HealthDataListCreateView,
    HealthPredictionAPIView,
    login_view,
    home_view,
)
from . import views  # استيراد views من نفس التطبيق

urlpatterns = [

    # path ('api/token/', TokenObtainPairView.as_view (), name='token_obtain_pair'),
    # path ('api/token/refresh/', TokenRefreshView.as_view (), name='token_refresh'),
    path ('api/protected-data/', ProtectedDataView.as_view (), name='protected-data'),
    # مسارات الصفحة الرئيسية و البيانات الديناميكية
    path('home/', views.home_view, name='home'),

    # مسار تسجيل مستخدم جديد
    path('register/', RegisterView.as_view(), name='register'),

    # مسار تسجيل الدخول باستخدام API
    path('login-api/', LoginView.as_view(), name='login_api'),

    # مسار تسجيل الدخول باستخدام HTML Template
    path('login/', login_view, name='login'),

    # مسار تسجيل الخروج
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # مسار الصفحة الرئيسية بعد تسجيل الدخول
    path('home/', home_view, name='home'),

    # مسار عرض البيانات الصحية أو إضافتها
    path('health-data/', HealthDataListCreateView.as_view(), name='health_data_list_create'),

    # مسار إضافي لعرض البيانات الصحية (اختياري بناءً على الطلب)
    path('data/', HealthDataListCreateView.as_view(), name='health_data_list_create_alt'),

    # مسار استدعاء البيانات الصحية عبر دالة `get_health_data`
    path('get-health-data/', get_health_data, name='get_health_data'),

    # مسار التنبؤ بالحالات الصحية
    path('predict/', HealthPredictionAPIView.as_view(), name='health_prediction'),

]
