from rest_framework import serializers
from .models import Company, Favourite


class CompanySerializer(serializers.ModelSerializer):
    favourite = serializers.SerializerMethodField()
    key = serializers.IntegerField(source='id')

    def get_favourite(self, obj):
        favs = obj.favourite_set.filter(user=self.context['user_id'])
        response = FavouriteSerializer(favs, many=True).data
        if response:
            fav_id = favs.first().pk
            return fav_id
        else:
            return 0


    class Meta:
        model = Company
        fields = ('key', 'name', 'email', 'address', 'employee_size', 'phone', 'website', 'favourite')


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
