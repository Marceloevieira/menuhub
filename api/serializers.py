from django.contrib.auth.models import User, Group
from rest_framework import serializers

from menus.models import MenuItem, Restaurant


class ResturantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        exclude = ('restaurant',)


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menuitens = MenuItemModelSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
