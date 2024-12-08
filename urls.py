# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
# from rest_framework.schemas import get_schema_view
# from rest_framework.permissions import AllowAny
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     # مسار تطبيق health
#     path('health-data/', include('health.urls')),  # تضمين مسارات تطبيق health
#
#     # مسار مخطط OpenAPI
#     path('schema/', get_schema_view(
#         permission_classes=[AllowAny],
#     ), name='openapi-schema'),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health-data
#     path('', lambda request: redirect('health_data_list')),  # إعادة توجيه الصفحة الرئيسية إلى health_data_list
#     # path ('', lambda request: redirect (reverse ('health_data_list'))),  # إعادة التوجيه إلى health_data_list
#
# ]
# -------------------------------------------------------------------
#
# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     path ('health/', include ('health.urls')),  # تأكد أن 'health' هو اسم تطبيقك
#
#     # مسار تطبيق health مع تعريف namespace
#     path('health/', include(('health.urls', 'health'), namespace='health')),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#     path('', lambda request: redirect('health:health_data_list_create')),
#
# ]

# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#                   # مسار لوحة التحكم
#                   path ('admin/', admin.site.urls),
#
#                   # مسار تطبيق health
#                   path ('health/', include (('health.urls', 'health'), namespace='health')),
#                   path ('health/', include ('health.urls')),  # التأكد من تضمين تطبيق health
#
#                   # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#                   path ('', lambda request: redirect ('health:health_data_list_create')),
#               ] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from health import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

if settings.DEBUG:
    import debug_toolbar
urlpatterns = [
    path ('__debug__/', include (debug_toolbar.urls)),

    path ('api/token/', TokenObtainPairView.as_view (), name='token_obtain_pair'),
    # مسار لتحديث التوكن
    path ('api/token/refresh/', TokenRefreshView.as_view (), name='token_refresh'),
    # مسار لوحة التحكم
    path ("admin/", admin.site.urls),
    path ('', include ('health.urls')),  # تأكد من تضمين URLs تطبيق health
    path ('health/', include ('health.urls')),  # ربط تطبيق health بملف URLs الخاص به

    # تضمين urls الخاص بـ health مرة واحدة فقط
    path ("health/", include (("health.urls", "health"), namespace="health")),  # تأكد من تضمين تطبيق health

    # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create (تأكد من أن هذه المسار موجود)
    path ("", lambda request: redirect ("health:health_data_list_create")),  # تأكد من وجود هذا المسار في health.urls

]

# إذا كان التطبيق في وضع التطوير (DEBUG=True)، يمكنك تقديم الملفات الوسائطية
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path, include
# from django.contrib import admin
# from django.shortcuts import redirect
#
# urlpatterns = [
#     # مسار لوحة التحكم
#     path('admin/', admin.site.urls),
#
#     # مسار تطبيق health مع تعريف namespace
#     path('health/', include(('health.urls', 'health'), namespace='health')),
#
#     # إعادة توجيه الصفحة الرئيسية إلى health_data_list_create
#     path('', lambda request: redirect('health:health_data_list_create')),
# ]
