import logging

from .models import Entry
from api.decorators import authenticate_application
from api.validators import EntrySerializer
from api.validators import UpdateEntrySerializer
from clients.models import Client
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


class NewEntryView(views.APIView):

    @authenticate_application()
    def post(self, request, *args, **kwargs):
        """Create a new entry for an user

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        serializer = EntrySerializer(data=request.data)

        if serializer.is_valid():
            client = Client.objects.get(username=self.request.user.username)
            entry = Entry(
                user=client,
                order=request.data.get("order"),
                date=request.data.get("date"),
                value=request.data.get("value"),
                comment=request.data.get("comment"))
            entry.save()
            return Response({})
        else:
            return Response({
                "error_code": "INVALID_ENTRY",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ListEntriesView(views.APIView):

    @authenticate_application()
    def get(self, request, *args, **kwargs):
        """Get a client entries by year, month and day

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        year = self.kwargs.get("year", None)
        month = self.kwargs.get("month", None)
        day = self.kwargs.get("day", None)

        entries = Entry.objects.all()

        if year:
            entries = entries.filter(date__year=year)

        if month:
            entries = entries.filter(date__month=month)

        if day:
            entries = entries.filter(date__day=day)

        client = Client.objects.get(username=self.request.user.username)
        return Response({
            "year": year,
            "month": month,
            "day": day,
            "entries": [{
                "id": e.pk,
                "order": e.order,
                "date": e.date,
                "value": e.value,
                "comment": e.comment,
                "created_date": e.created_date,
                "modified_date": e.modified_date,
            } for e in entries]
        })


class UpdateEntryView(views.APIView):

    @authenticate_application()
    def put(self, request, *args, **kwargs):
        """Get a client entries by year, month and day

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        serializer = UpdateEntrySerializer(data=request.data)

        if serializer.is_valid():
            entry_id = self.kwargs.get("id", None)
            if entry_id:

                client = Client.objects.get(
                    username=self.request.user.username)
                entry = Entry.objects.filter(pk=entry_id, user=client).first()
                if entry:
                    entry.value = request.data.get("value")
                    entry.comment = request.data.get("comment")
                    entry.save()
                else:
                    return Response({
                        "error_code": "INVALID_UPDATE",
                        "errors": {
                            "entry": "This entry does not belongs to this user"
                        }
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({})
        else:
            return Response({
                "error_code": "INVALID_UPDATE",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
