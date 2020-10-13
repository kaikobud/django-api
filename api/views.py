from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from allauth.account.admin import EmailAddress
from django.contrib.auth.models import User

from .models import Company, Favourite
from .serializers import CompanySerializer, FavouriteSerializer


class CompanyListSearchView(generics.ListAPIView):
    serializer_class = CompanySerializer

    def list(self, request):
        context = {
            "user_id": int(self.request.query_params['user_id']),
        }
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, context=context, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Company.objects.all()
            company_name = self.request.GET.get('q', None)
            if company_name is not None:
                queryset = queryset.filter(name__icontains=company_name)
            return queryset


class FavouriteCreateView(generics.ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


def is_email_verified(request, email):

    is_verified = EmailAddress.objects.filter(email=email, verified=True).exists()

    data = [{'is_verified': is_verified}]

    return JsonResponse(data, safe=False)

