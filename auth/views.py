import jwt
from django.conf import settings
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from inventory.serializer import ( LoginSerializer, UserSerializer, 
                                   RegisterSerializer, 
                                   EmailVerificationSerializer, 
                                   RequestPasswordResetSerializer, 
                                   SetNewPasswordSerializer
                                 )
from models import User
from auth.utils import Utils
from inventory.renderers import UserRenderer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(GenericAPIView):
    """
    API endpoint that allows users to be registered.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)

        if serializer.is_valid():
            serializer.save()

            user_data = serializer.data

            user = User.objects.get(email=user_data['email'])
            refresh = RefreshToken.for_user(user)
            current_site = get_current_site(request)
            relative_link = reverse('email-verification')

            absolute_url = 'http://' + \
                str(current_site.domain) + relative_link + \
                '?token=' + str(refresh.access_token)
            body = 'Hello' + user.username + ',\n\n' + \
                'Please click on the link below to verify your email:\n\n' + \
                absolute_url + '\n\n' + 'Thank you!'

            data = {
                'email_body': body,
                'email_subject': 'Email Verification',
                'email_to': user.email
            }

            Utils.send_email(data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(GenericAPIView):
    """
    API endpoint that allows users to verify their email.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=data['id'])
            user.is_vealid = True
            user.save()

            return Response({'email': 'activation succeful'},
                            status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Expired Signature', 'message': str(e)},
                            status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist as e:
            return Response({'error': 'User Does Not Exist', 'message': str(e)},
                            status=status.HTTP_404_NOT_FOUND)
        except jwt.DecodeError as e:
            return Response({'error': 'Fail to Decode', 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError as e:
            return Response({'error': 'Invalid Token', 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.data['email'])
            if user.is_vealid:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh.access_token),
                                 'access': str(refresh.access_token)},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Email not verified'},
                                status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(GenericAPIView):
    serializer_class = RequestPasswordResetSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data={'request':request, 'data':request.data}
        serializer = self.serializer_class(data=data)
        
        email=request.data.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            
            current_site = get_current_site(request=request)
            relative_link = reverse('password-reset', kwargs={'uidb64':uidb64, 'token':token})
            absolute_url = 'http://' + str(current_site.domain) + relative_link

            body = 'Hello' + user.username + ',\n\n' + \
                'Please click on the link below to reset your password: \n\n' + \
                absolute_url + '\n\n' + 'Thank you!'

            data = {
                'email_body': body,
                'email_subject': 'Password Reset',
                'email_to': user.email
            }

            Utils.send_email(data)
        
        # Sending the same confimation response to prevent the user to check if emails exist in database
        message={'Success': 'We\'ve sent you a resetation email for your password'}        
        return Response(message, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(GenericAPIView):
    def get(self, request, uidb64, token):
        try: 
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                message={'Error': 'Token Invalid, request a new token'}        
            
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)

            message={'Success': True, 'Message': 'Token Acepted successfully', 'uidb64': uidb64, 'token': token}
            return Response(message, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            message={'Error': 'Token Invalid, request a new token'}        
            
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            message = {'Success': True, 'Message': 'Password Reseted successfully'}
            return Response(message, status=status.HTTP_200_OK)

        message = {'Success': False, 'Message': 'Password not changed'}

        return Response(message, status=status.HTTP_401_UNAUTHORIZED)
        