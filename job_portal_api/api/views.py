# api/views.py
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Job, Candidate,Internship ,Course,UserProfile,Coupon,Bookmark
from .serializers import JobSerializer, CandidateSerializer, UserSerializer,InternshipSerializer,CourseSerializer,UserProfileSerializer,CouponSerializer,BookmarkSerializer
from rest_framework.response import Response
from django.utils import timezone


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        # Filter jobs based on location (if provided in the query params)
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(location=location)

        # Filter jobs based on job type (if provided in the query params)
        job_type = self.request.query_params.get('job_type', None)
        if job_type is not None:
            queryset = queryset.filter(job_type=job_type)

        # Search jobs based on title (if provided in the query params)
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JobRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InternshipListCreateView(generics.ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        # Filter internships based on location (if provided in the query params)
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(location=location)

        # Search internships based on title (if provided in the query params)
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset


class InternshipRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CouponListCreateView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated]


class CouponRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseApplyCouponView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        coupon_code = request.data.get('coupon_code', None)

        try:
            coupon = Coupon.objects.get(code=coupon_code)
            if coupon.valid_from <= timezone.now() and coupon.valid_to >= timezone.now():
                course.is_discounted = True
                course.discount_percent = coupon.discount_percent
                course.save()
                return Response({'message': 'Coupon applied successfully.'})
            else:
                return Response({'error': 'Coupon is not valid at this time.'}, status=400)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code.'}, status=400)


class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookmarkListCreateView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]
