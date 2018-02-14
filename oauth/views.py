import simplejson as json

from api.decorators import authenticate_application

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


# class OauthRegisterCallbackConfigView(views.APIView):
#     permission_classes = []

#     @authenticate_application()
#     def post(self, request, *args, **kwargs):
#         """Register the configuration needed to send callbacks

#         Args:
#             request (request): the json request

#         Returns:
#             json: the parsed response
#         """
#         oauth_application = request.application
#         app_config = Application(self.request.body)

#         if app_config.is_valid():

#             oauth_application.callback_data = app_config.data
#             oauth_application.save()

#             return Response({
#                 "status": "PROCESSED",
#                 "data": {}}, status=status.HTTP_200_OK)

#         return Response({
#             'error_code': app_config.error_code,
#             'error': 'App configuration error'},
#             status=status.HTTP_400_BAD_REQUEST)
