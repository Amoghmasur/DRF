from watchlist_app.models import WatchList,StreamPlatform,Review
from rest_framework.response import Response
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from watchlist_app.api.permissions import AdminOrReadOnly
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        movie=WatchList.objects.get(pk=pk)

        serializer.save(watchlist=movie)




class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[AdminOrReadOnly]


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



class StreamPlatformVS(viewsets.ViewSet):

    def list(self,request):
        queryset=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(queryset,many=True)

        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset=StreamPlatform.objects.all()
        watchlist=get_object_or_404(queryset,pk=pk)
        serializer=StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

    def create(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)





class StreamPlatformAV(APIView):

    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True) #for hyperlinked use this ,context={'request': request}
        return Response(serializer.data)

    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WatchListAV(APIView):

    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








# @api_view(['GET','POST'])

# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):

#     if request.method=='GET':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)











