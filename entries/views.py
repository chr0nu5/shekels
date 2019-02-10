import calendar
import calendar
import datetime
import logging

from .models import Entry
from .models import Recurrent
from api.decorators import authenticate_application
from api.validators import EntrySerializer
from api.validators import RecurrentSerializer
from api.validators import UpdateEntrySerializer
from clients.models import Client
from dateutil.relativedelta import relativedelta
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


class NewRecurrentEntryView(views.APIView):

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

        serializer = RecurrentSerializer(data=request.data)

        if serializer.is_valid():
            client = Client.objects.get(username=self.request.user.username)

            if request.data.get("value") == 0:
                return Response({})

            times = int(request.data.get("times"))
            day = request.data.get("day")
            value = request.data.get("value")
            description = request.data.get("description")

            if times == 0:
                times = 1200
                total = ""
            else:
                total = "/{}".format(times)

            current_date = datetime.datetime.strptime(
                day, '%m/%d/%Y').date()
            max_times = times + 1

            recurrent_entry = Recurrent(
                user=client,
                times=times,
                day=current_date.day,
                value=value,
                description=description)
            recurrent_entry.save()

            while times > 0:

                entry = Entry(
                    user=client,
                    order=1,
                    date=current_date,
                    value=value,
                    comment="{} {}{}".format(
                        description, max_times - times, total),
                    recurrent=recurrent_entry)
                entry.save()

                current_date = current_date + relativedelta(months=1)
                times = times - 1

            return Response({})
        else:
            return Response({
                "error_code": "INVALID_ENTRY",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


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


class ListRecurrentEntriesView(views.APIView):

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
        entries = Recurrent.objects.filter(user=client, active=True)

        record_list = []
        for e in entries:
            record_list.append({
                "id": e.pk,
                "times": e.times,
                "day": e.day,
                "value": e.value,
                "description": e.description,
                "created_date": e.created_date,
                "modified_date": e.modified_date,
            })

        return Response({
            "entries": record_list
        })


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

        entries = Entry.objects.filter(user=client)
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
                        for day in range(1, num_days + 1)]

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
                                    r.get("value") * -1) if r.get(
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
                            "naked_value": 0,
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

        # TODO
        # filter by year

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
                            "entry": "This entry does not belong to this user"
                        }
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({})
        else:
            return Response({
                "error_code": "INVALID_UPDATE",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateRecurrentEntryView(views.APIView):

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

        serializer = RecurrentSerializer(data=request.data)

        if serializer.is_valid():
            entry_id = self.kwargs.get("id", None)
            if entry_id:

                client = Client.objects.get(
                    username=self.request.user.username)
                recurrent_entry = Recurrent.objects.filter(
                    pk=entry_id, user=client).first()
                if entry:
                    recurrent_entry.value = request.data.get("value")
                    recurrent_entry.times = request.data.get("times")
                    recurrent_entry.comment = request.data.get("comment")
                    recurrent_entry.save()

                else:
                    return Response({
                        "error_code": "INVALID_UPDATE",
                        "errors": {
                            "recurrent_entry":
                            "This recurrent entry does not belong to this user"
                        }
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({})
        else:
            return Response({
                "error_code": "INVALID_UPDATE",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteRecurrentEntryView(views.APIView):

    @authenticate_application()
    def delete(self, request, *args, **kwargs):
        """Delete a client entry by id

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        entry_id = self.kwargs.get("id", None)
        if entry_id:

            client = Client.objects.get(
                username=self.request.user.username)
            recurrent_entry = Recurrent.objects.filter(
                pk=entry_id, user=client).first()
            if recurrent_entry:
                recurrent_entry.active = False
                recurrent_entry.save()

                Entry.objects.filter(
                    recurrent=recurrent_entry,
                    date__gte=datetime.datetime.now()).delete()

            else:
                return Response({
                    "error_code": "INVALID_DELETE",
                    "errors": {
                        "entry": "This entry does not belongs to this user"
                    }
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({})

        else:
            return Response({
                "error_code": "INVALID_DELETE",
                "errors": {
                    "entry": "This entry is invalid"
                }
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteEntryView(views.APIView):

    @authenticate_application()
    def delete(self, request, *args, **kwargs):
        """Delete a client entry by id

        Args:
            request (TYPE): Description
            *args: Description
            **kwargs: Description

        Returns:
            JSON: response
        """

        entry_id = self.kwargs.get("id", None)
        if entry_id:

            client = Client.objects.get(
                username=self.request.user.username)
            entry = Entry.objects.filter(pk=entry_id, user=client).first()
            if entry:
                entry.delete()
            else:
                return Response({
                    "error_code": "INVALID_DELETE",
                    "errors": {
                        "entry": "This entry does not belongs to this user"
                    }
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({})

        else:
            return Response({
                "error_code": "INVALID_DELETE",
                "errors": {
                    "entry": "This entry is invalid"
                }
            }, status=status.HTTP_400_BAD_REQUEST)
