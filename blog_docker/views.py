from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Glass
from .serializers import PostSerializer

# Create your views here.


class PostsList(ListCreateAPIView):
    queryset = Glass.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Glass.objects.all()
    serializer_class = PostSerializer
    