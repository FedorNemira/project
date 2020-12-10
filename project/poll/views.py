from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound 
from django.http import HttpResponse
from poll.models import Poll, Question, QuestionOption
from poll import serializers
import pprint
from copy import copy
from xml.sax.saxutils import escape
from rest_framework import permissions


class PollView(APIView):
    def get(self, request):
        print(request.role)
        if request.role == 'anonymous_user':   
            polls = Poll.objects.all()
            serializer = serializers.PollSerializer(polls, many=True)
            return Response({"polls": serializer.data})
        return HttpResponse("Only for registered users!")

    def post(self, request):
        print(request.role)
        if request.role == 'manager':    
            poll = request.data
            serializer = serializers.PollSerializer(data=poll)
            if serializer.is_valid(raise_exception=True):
                poll = serializer.save()
            return Response({"success": f"Poll {poll} created successfully"})
        return HttpResponse("Only for admin!")

    def delete(self, request):
        if request.role == 'manager':
            try:
                poll = Poll.objects.get(id=request.data.get('id'))
                poll.delete()
            except:
                raise NotFound()
            return Response({"message": f"Poll with id '{poll}' has been deleted."})
        return HttpResponse("Only for admin!")

    def patch(self, request):
        if request.role == 'manager':
            try:
                poll = Poll.objects.get(id=request.data.get('id'))
                poll.poll_name = request.data.get('poll_name')
                poll.save()
            except:
                raise NotFound()
            return Response({"message": f"Poll with id '{poll}' has been changed."})
        return HttpResponse("Only for admin!")



class QuestionView(APIView):
    def get(self, request):
        print(request.role)
        if request.role: 
            serialized_response = {}
            serialized_response['questions'] = []
            for question in Question.objects.all().prefetch_related('questionoption_set'): 
                serialized_response__question = {}
                serialized_response__question["question_text"] = escape(question.question_text)
                serialized_response__question["question_type"] = escape(question.question_type)
                serialized_response__question["question_options"] = []
                if question.question_type == "one_choice" or question.question_type == "multiple_choice":                   
                    for question_option in question.questionoption_set.all():
                        serialized_response__question__question_option = {}
                        serialized_response__question__question_option["question_option_name"] = escape(question_option.question_option_name)
                        serialized_response__question["question_options"].append(serialized_response__question__question_option)
                serialized_response['questions'].append(serialized_response__question)
            return Response(serialized_response)

        return HttpResponse("Only for registered users!")

    def post(self, request):
        print(request.role)
        if request.role:
            data = request.data 
            print(data)
            if 'question_text' in data:
                serializer = serializers.QuestionSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    question = serializer.save()
                    return Response({"success": f"Question {question} created successfully, question_id: {question.id}"})
            elif 'question_option_name' in data:
                serializer = serializers.QuestionOptionSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    question_option = serializer.save()
                    return Response({"success": f"Question option {question_option} created successfully, question_id: {question_option.id}"})
        return HttpResponse("Only for admin!")

    def patch(self, request):


        if request.role:
            data = request.data

            post_keys = list(data.keys())

            post_keys.remove('id')
            post_keys = set(post_keys)

            all_question_fields = set([str(x).split('.')[2] for x in Question._meta.fields])
            all_question_options_fields = set([str(x).split('.')[2] for x in QuestionOption._meta.fields])

            print(post_keys)
            print(all_question_fields)
            print(post_keys & all_question_fields)

            if post_keys & all_question_fields:
                question = Question.objects.get(id=request.data.get('id'))
                if data.get('question_text'):
                    question.question_text = data.get('question_text')
                if data.get('question_type'):
                    question.question_type = data.get('question_type')
                question.save()
                return Response({"message": f"Question with id '{question}' has been changed."})
                
            elif post_keys & all_question_options_fields:
                question = QuestionOption.objects.get(id=request.data.get('id'))
                if data.get('question_option_name'):
                    question.question_option_name = data.get('question_option_name')
                question.save()
                return Response({"message": f"Question with id '{question}' has been changed."})
        return HttpResponse("Only for admin!")


    def delete(self, request):
        if request.role == 'manager':
            try:
                poll = Poll.objects.get(id=request.data.get('id'))
                poll.delete()
            except:
                raise NotFound()
            return Response({"message": f"Poll with id '{poll}' has been deleted."})
        return HttpResponse("Only for admin!")

    