# api/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    JobListCreateView,
    JobRetrieveUpdateDeleteView,
    CandidateListCreateView,
    CandidateRetrieveUpdateDeleteView,
    UserListCreateView,
    UserRetrieveUpdateDeleteView,
    InternshipListCreateView,
    InternshipRetrieveUpdateDeleteView,
    CourseListCreateView,
    CourseRetrieveUpdateDeleteView,
    UserProfileListCreateView,
    UserProfileRetrieveUpdateDeleteView,
    CouponListCreateView,
    CouponRetrieveUpdateDeleteView,
    CourseApplyCouponView,
    BookmarkListCreateView,
    BookmarkRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDeleteView.as_view(),
         name='job-retrieve-update-delete'),
    path('candidates/', CandidateListCreateView.as_view(),
         name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateRetrieveUpdateDeleteView.as_view(),
         name='candidate-retrieve-update-delete'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(),
         name='user-retrieve-update-delete'),

    path('internships/', InternshipListCreateView.as_view(),
         name='internship-list-create'),
    path('internships/<int:pk>/', InternshipRetrieveUpdateDeleteView.as_view(),
         name='internship-retrieve-update-delete'),

    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDeleteView.as_view(),
         name='course-retrieve-update-delete'),
    path('userprofiles/', UserProfileListCreateView.as_view(),
         name='userprofile-list-create'),
    path('userprofiles/<int:pk>/', UserProfileRetrieveUpdateDeleteView.as_view(),
         name='userprofile-retrieve-update-delete'),

    path('coupons/', CouponListCreateView.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponRetrieveUpdateDeleteView.as_view(),
         name='coupon-retrieve-update-delete'),
    path('courses/<int:pk>/apply-coupon/',
         CourseApplyCouponView.as_view(), name='course-apply-coupon'),

    path('bookmarks/', BookmarkListCreateView.as_view(),
         name='bookmark-list-create'),
    path('bookmarks/<int:pk>/', BookmarkRetrieveUpdateDeleteView.as_view(),
         name='bookmark-retrieve-update-delete'),
]
