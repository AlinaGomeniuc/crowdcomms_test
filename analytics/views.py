import pytz
from django.utils import timezone
from .models import UserVisit
from datetime import datetime, timedelta
from django.db.models import Sum

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    """
    Basic 'Hello World' view. Show our current API version, the current time, the number of recent visitors
    in the last 1 hour, and the total number of visitors and page visits
    """

    def get(self, request):
        now = datetime(2020, 6, 6, 9, tzinfo=pytz.UTC)
        data = {
            'version': 1.0,
            'time': now,
            'recent_visitors': UserVisit.objects.filter(last_seen__gte=now-timedelta(hours=1)).count(),
            'all_visitors': UserVisit.objects.count(),
            'all_visits': UserVisit.objects.aggregate(total_visits=Sum('visits'))['total_visits']
        }
        return Response(data)

