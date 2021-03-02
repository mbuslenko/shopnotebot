from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Profile, Item
from .serializers import ProfileSerializer, ItemSerializer
from rest_framework.generics import GenericAPIView


class ProfileList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        profile_id = self.request.query_params.get('profile')
        if profile_id:
            queryset = queryset.filter(profile=profile_id)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


