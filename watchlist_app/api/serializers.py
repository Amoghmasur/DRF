from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform



class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model=StreamPlatform
        fields='__all__'


class WatchListSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()

    class Meta:
        model=WatchList
        fields=['id','name','description']


    def get_len_name(self,object):
        length=len(object.name)
        return length

    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError('title and desc cannot be same')
        else:
            return data


    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("name is too short")
        return value




# def name_length(value):
#         if len(value)<2:
#             raise serializers.ValidationError('name is too short')

# class MovieSerializer(serializers.Serializer):

#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError('title and desc cannot be same')
#         else:
#             return data


#     def validate_name(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError("name is too short")
#         return value








