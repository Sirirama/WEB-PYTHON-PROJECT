from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     #     context = {
#     #         'question': question
#     #     }
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')

#     question = get_object_or_404(Question, pk = question_id)
#     context = {
#         'question': question
#     }

#     return render(request, 'polls/detail.html', context)

#     # return HttpResponse("<h2>You're looking at question number <i>{}</i>.</h2>".format(question_id))

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     # return HttpResponse("<h2>You're looking at the result of question number <i>%s</i>." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }

#     return render(request, 'polls/results.html', context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    # response = "<h2>You're voting on question <i>%s</i></h2>"
    # return HttpResponse(response % question.id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))