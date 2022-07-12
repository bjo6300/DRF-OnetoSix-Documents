
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetViewSet(viewsets.ModelViewSet):
    """
    이 viewset은 `list`, `create`, `retrive`, `update`, `destroy`
    액션을 자동으로 제공한다
    
    추가적으로 highlight 액션만 따로 적어주었다
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from django.contrib.auth.models import User


from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    이 viewset은 `list` 와 `retrieve` 액션을 자동으로 제공한다
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer