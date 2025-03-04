from django.urls import path

from api.result_processing.course.views import CourseListCreateView, CourseDetailView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list-create'),
    path('<str:course_id>/', CourseDetailView.as_view(), name='course-detail'),
]
