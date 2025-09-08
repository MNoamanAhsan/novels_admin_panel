from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Novels, Categoryn
from .serializers import NovelSerializer, CategorySerializer
from django.db import models
from rest_framework.pagination import PageNumberPagination


class HomeView(APIView):
    def get(self,request):
        categories=Categoryn.objects.all()
        data={}
        for cat in categories:
            novels=NovelSerializer(cat.novels.all(),many=True).data
            data[f"Category: {cat.name}"]=novels
        return Response(data)
    

class LibraryPagination(PageNumberPagination):
    page_size=30
    page_size_query_param="page_size"
    max_page_size=100
        
class LibraryView(generics.ListAPIView):
    def get(self,request):
        novels=Novels.objects.all().order_by("-id")
        paginator=LibraryPagination()
        resultpage=paginator.paginate_queryset(novels,request)
        serializer=NovelSerializer(resultpage,many=True)
        return paginator.get_paginated_response(serializer.data)

    # queryset=Novels.objects.all()
    # serializer_class=NovelSerializer


class NovelSearchView(APIView):
    def get(self,request):
        query=request.GET.get("q","").strip()
        if not query:
            return Response({"error","Please Provide a search query."},status=400)
        novels=Novels.objects.filter(
            models.Q(title__icontains=query) | models.Q(category__name__icontains=query)
        )
        serializer=NovelSerializer(novels, many=True)
        return Response(serializer.data)

# class CategoryListView(generics.ListAPIView):
#     queryset = Categoryn.objects.all()
#     serializer_class = CategorySerializer

# class NovelListView(generics.ListAPIView):
#     queryset = Novels.objects.all()
#     serializer_class = NovelSerializer

# class TrendingNovelsView(generics.ListAPIView):
#     queryset = Novels.objects.filter(is_trending=True)
#     serializer_class = NovelSerializer

# class TopRatedNovelsView(generics.ListAPIView):
#     queryset = Novels.objects.filter(is_toptrend=True)
#     serializer_class = NovelSerializer

# class NovelSearchView(generics.ListAPIView):
#     serializer_class = NovelSerializer

#     def get_queryset(self):
#         query = self.request.query_params.get('q', '')
#         return Novels.objects.filter(title__icontains=query)

