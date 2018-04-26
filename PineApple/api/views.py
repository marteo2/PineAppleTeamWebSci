# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from btcdata.getbtcdata import find_data_json


@api_view(['GET'])
def data_list(request, start_time, end_time):
    """
    create a json contain the data in request date range
    :param end_time: time_stamp
    :param start_time: time_stamp
    :param request:
    :return: json
    """
    data = find_data_json(start_time / 1000.0, end_time / 1000.0)
    return Response(data, status=status.HTTP_201_CREATED)
