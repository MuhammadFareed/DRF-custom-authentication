from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .custom_permissions import MyPermissions
from .custom_auth import MyCustomAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [MyCustomAuthentication]
    permission_classes = [IsAuthenticated]


