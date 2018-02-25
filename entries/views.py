import calendar
import datetime
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

            if request.data.get("value") == 0:
                return Response({})

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

        client = Client.objects.get(username=self.request.user.username)

        year = self.kwargs.get("year", None)
        month = self.kwargs.get("month", None)
        day = self.kwargs.get("day", None)

        entries = Entry.objects.all()
        balance = 0.00

        all_entries = entries

        if year:
            entries = entries.filter(date__year=year)

        if month:
            entries = entries.filter(date__month=month)

        if day:
            entries = entries.filter(date__day=day)

        record_list = []

        for e in entries:
            record_list.append({
                "id": e.pk,
                "order": e.order,
                "date": e.date,
                "value": e.value,
                "comment": e.comment,
                "created_date": e.created_date,
                "modified_date": e.modified_date,
            })

        if year:

            if month:
                current_date = datetime.date(int(year), int(month), 1)
            else:
                current_date = datetime.date(int(year), 1, 1)

            for e in all_entries:
                if e.date < current_date:
                    balance = balance + float(e.value)

            current_list = []

            for m in range(1, 13):

                if month and not m == int(month):
                    continue

                num_days = calendar.monthrange(int(year), int(m))[1]
                days = [datetime.date(int(year), int(m), day)
                        for day in range(1, num_days+1)]

                for d in days:
                    tmp_list = []
                    tmp_date = None
                    count = 1
                    for r in record_list:
                        if r.get("date") == d:
                            tmp_date = r.get("date")
                            tmp_list.append({
                                "id": r.get("id"),
                                "order": r.get("order"),
                                "date": r.get("date"),
                                "value": "-${}".format(
                                    r.get("value")*-1) if r.get(
                                    "value") < 0 else "${}".format(
                                    r.get("value")),
                                "naked_value": r.get("value"),
                                "comment": r.get("comment"),
                                "created_date": r.get("created_date"),
                                "modified_date": r.get("modified_date")
                            })
                            count += 1
                            balance = balance + float(r.get("value"))
                    while(len(tmp_list) < 4):
                        tmp_list.append({
                            "id": None,
                            "order": count,
                            "date": tmp_date,
                            "value": None,
                            "comment": None,
                            "created_date": None,
                            "modified_date": None
                        })
                        count += 1

                    current_list.append({
                        "day": str(d),
                        "records": tmp_list,
                        "balance": format(balance, '.2f'),
                        "credit": format(
                            balance + float(client.credit), '.2f'),
                        "savings": format(
                            balance + float(client.credit) + float(
                                client.savings), '.2f'),
                    })

            record_list = current_list

        return Response({
            "year": year,
            "month": month,
            "day": day,
            "entries": record_list
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
