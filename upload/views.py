from django.shortcuts import render

from rest_framework import status,views,response
from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import PhotoList,DocumentList
from .serializer import PhotoListSerializer,DocumentListSerializer

import magic

ALLOWED_MIME    = [ "application/pdf" ]


class PhotoView(views.APIView):
    def get(self, request, *args, **kwargs):

        data        = PhotoList.objects.all()
        context     = {"data":data}

        return render(request,"upload/image.html",context)

    def post(self, request, *args, **kwargs):

        serializer      = PhotoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data        = PhotoList.objects.all()
        context     = {"data":data}
        content_data_string     = render_to_string('upload/image_content.html', context ,request)
        json_data               = { "content" : content_data_string }

        return JsonResponse(json_data)

index   = PhotoView.as_view()


class DocumentView(views.APIView):

    def get(self, request, *args, **kwargs):

        data    = DocumentList.objects.all()
        context = { "data":data,
                    }

        return render(request,"upload/document.html",context)

    def post(self, request, *args, **kwargs):


        serializer      = DocumentListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mime_type       = magic.from_buffer(request.data["document"].read(1024) , mime=True)

        if mime_type in ALLOWED_MIME:
            serializer.save()
        else:
            print("このファイルは許可されていません。")

        data        = DocumentList.objects.all()
        context     = {"data":data}
        content_data_string     = render_to_string('upload/document_content.html', context ,request)
        json_data               = { "content" : content_data_string }

        return JsonResponse(json_data)

document    = DocumentView.as_view()
