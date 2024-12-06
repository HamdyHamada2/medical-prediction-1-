from rest_framework.pagination import PageNumberPagination

# تحديد حجم الصفحة
class HealthDataPagination(PageNumberPagination):
    page_size = 1  # عدد السجلات في كل صفحة (يمكنك تعديله حسب حاجتك)
    page_size_query_param = 'page_size'  # يتيح للمستخدم تحديد عدد السجلات في كل صفحة من خلال استعلام GET
    max_page_size = 2  # الحد الأقصى لعدد السجلات في الصفحة
