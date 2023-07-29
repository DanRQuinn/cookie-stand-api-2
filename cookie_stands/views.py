from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import CookieStandSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly

class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
    
class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
