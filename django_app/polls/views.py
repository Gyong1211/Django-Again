from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from polls.models import Question, Choice


def index(request):
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    # choice = Choice.object.all(question = question)
    context = {
        'question': question,
        'choices': choices,
    }

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question':question,
    }
    return render(request, 'polls/results.html',context)


def vote(request, question_id):
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes +=1
            choice.save()
            # return HttpResponse("You're voting {} on question {}.".format(select, question_id, ))
            return redirect('polls:results',question_id)
        except (KeyError,Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice"
            )
            return redirect('polls:detail',question_id)
    elif request.method == 'GET':
        return HttpResponse("You're not voting on question %s." % question_id)
