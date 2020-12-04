from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound 
from poll.models import Poll
from poll import serializers
import pprint


class PollView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = serializers.PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})

    def post(self, request):
        pprint.pprint(request.data)
        poll = request.data
        serializer = serializers.PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll = serializer.save()
        return Response({"success": f"Poll {poll} created successfully"})

    def delete(self, request):
        try:
            poll = Poll.objects.get(id=request.data.get('id'))
            poll.delete()
        except:
            raise NotFound()

        return Response({"message": f"Poll with id '{poll}' has been deleted."})

    def patch(self, request):
        try:
            poll = Poll.objects.get(id=request.data.get('id'))
            poll.poll_name = request.data.get('poll_name')
            poll.save()
        except:
            raise NotFound()

        return Response({"message": f"Poll with id '{poll}' has been changed."})
