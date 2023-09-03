from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.models import Person
from decimal import Decimal


class DetailsUser(APIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserSerializer

    def get(self, request):
        get_data = User.objects.get(pk=request.user.pk)
        user_serializer = UserSerializer(get_data).data
        person_data = Person.objects.get(user_id=get_data.pk)
        saldo = person_data.saldo
        data = {
            'user':user_serializer,
            'saldo':saldo
        }
        return Response(data)
    
    def post(self, request):
        current_user = User.objects.get(pk=request.user.pk)
        email = request.data.get('email')
        password = request.data.get('password')
        current_user.username = email
        current_user.set_password(password)
        current_user.save()
        return Response({"message": "User update successfully"}, status=status.HTTP_201_CREATED)

 
class UpdateAmount(APIView):
    def post(self, request):
        id_user = request.data.get('user')
        amount = request.data.get('amount')
        debit = request.data.get('debit')
        if(debit == 'false'):
            try:
                amount_decimal = Decimal(amount)

                person = Person.objects.get(user_id=id_user)
                person.saldo = person.saldo + amount_decimal
                person.save()

                return Response({"message": "User updated successfully"}, status=status.HTTP_201_CREATED)
            except Person.DoesNotExist:
                return Response({"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            try:
                amount_decimal = Decimal(amount)
                person = Person.objects.get(user_id=id_user)
                person.saldo =  0.00
                person.save()
                return Response({"message": "User updated successfully"}, status=status.HTTP_201_CREATED)
            except Person.DoesNotExist:
                return Response({"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)