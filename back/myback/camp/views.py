from django.shortcuts import render, redirect
from django.conf import settings
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework import generics, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt

import cloudinary
import cloudinary.uploader
cloud_name = "dqjru6fzb",
file_extension = 'jpg'


@permission_classes([IsAuthenticated])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})


# Disable CSRF for this view in development; tighten this up for production.
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        cloudinary_response = cloudinary.uploader.upload(uploaded_file)
        public_id = cloudinary_response['public_id']
        image_url = f'https://res.cloudinary.com/{cloud_name}/image/upload/{public_id}.{file_extension}'

        return JsonResponse({'message': 'File uploaded to Cloudinary successfully', 'public_id': public_id, 'image_url': image_url, 'cloudname': cloud_name, 'file_extension': file_extension}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.data)  # Use request.data for POST data

        if form.is_valid():
            form.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(serializer.data)  # Print the serialized data

    return Response(serializer.data)


@api_view(['PUT'])
def edit_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    # Add a print statement to display the product_id
    print(f'Editing product with ID: {product_id}')

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
