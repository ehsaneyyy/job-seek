from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from web.models import Job,Apply
from .serializers import JobSerializer,ApplySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email=request.data.get("email")
    password=request.data.get("password")
    user=authenticate(request,username=email,password=password)

    if user is not None:
        refresh=RefreshToken.for_user(user)

        response_data={
            "status_code":200,
            "status":"success",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "message":"login successful"
        }
        return Response(response_data)
    else:
         response_data={
            "status_code":400,
            "status":"error",
            "message":"login unsuccess"
        }
         return Response(response_data)


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    first_name=request.data.get("first_name")
    last_name=request.data.get("last_name")
    email=request.data.get("email")
    password=request.data.get("password")

    if User.objects.filter(email=email).exists():
         response_data={
         "status_code":400,
         "status":"error",
         "message":"user with this email already exists"
         }
         return Response(response_data)
    else:
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        response_data={
         "status_code":201,
         "status":"success",
         "message":"user registered succusfully"
        }
        return Response(response_data)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def jobs(request):
    jobs=Job.objects.all()
    serializer=JobSerializer(jobs,many=True)
    return Response({
        "status_code":200,
        "data":serializer.data
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_job(request):
    serializer=JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response({
            "status_code":201,
            "data":serializer.data
        })
    return Response(serializer.errors,status=400)

@api_view(["PUT","PATCH"])
@permission_classes([IsAuthenticated])
def edit_job(request,id):
    job=get_object_or_404(Job,id=id,owner=request.user)
    serializer=JobSerializer(job,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status_code":200,
            "data":serializer.data,
        })
    return Response(serializer.errors,status=400)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_job(request,id):
    job=get_object_or_404(Job,id=id,owner=request.user)
    job.delete()
    return Response({
        "status_code":200,
        "message":"job deleted"
    })



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply(request):
    serializer=ApplySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(applier=request.user)
        return Response({
            "status_code":201,
            "data":serializer.data
        })
    return Response(serializer.errors,status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_apply(request, id):
    applier=request.user
    job=get_object_or_404(Job,id=id)
    context={
        "request":request
    }
    serializer=ApplySerializer(data=request.data,context=context)
   
    if serializer.is_valid():
        serializer.save(applier=applier, job=job)

        return Response({
            "status_code":201,
            "data":serializer.data
        })
    return Response(serializer.errors,status=400)
    


@api_view(["PUT","PATCH"])
@permission_classes([IsAuthenticated])
def edit_apply(request,id):
    applications=get_object_or_404(
        Apply,
        id=id,
        applier=request.user
    )
    serializer=ApplySerializer(applications,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status_code":200,
            "data":serializer.data
        })
    return Response(serializer.errors,status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_apply(request,id):
    applications=get_object_or_404(
        Apply,
        id=id,
        applier=request.user
    )
    applications.delete()
    return Response({
        "status_code":200,
        "message":"application deleted"
    })




