import math
from datetime import datetime, timedelta
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import LegsOfTriangle, PersonForm, TextEmail
from .models import Choice, Person, Question
from .tasks import send_email


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def hypotenuse_of_triangle(request):
    if request.method == 'POST':
        form = LegsOfTriangle(request.POST)
        if form.is_valid():
            legs_1 = form.cleaned_data["legs_1"]
            legs_2 = form.cleaned_data["legs_2"]
            hypotenuse = (legs_1 ** 2) + (legs_2 ** 2)
            hypotenuse = math.sqrt(hypotenuse)
            return render(request, 'triangle.html', {'hypotenuse': hypotenuse})
    else:
        form = LegsOfTriangle(request.POST)

    return render(request, 'triangle.html', {
        'form': form,
    })


def create_pers(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/polls")
    else:
        form = PersonForm(request.POST)
    return render(request, 'person.html', {
        'form': form,
    })


def person_pk(request, pk):
    if request.method == 'POST':
        person_p = get_object_or_404(Person, pk=pk)
        form = PersonForm(request.POST, instance=person_p)
        if form.is_valid():
            form.save()
            return redirect("/polls")
    else:
        form = PersonForm(request.POST)
    return render(request, 'person.html', {
        'form': form,
    })


def text_mail(request):
    if request.method == "POST":
        form = TextEmail(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            date_time = form.cleaned_data['date_time']
            send_email.apply_async((text, email), eta=date_time)
            messages.success(request, 'Remind is created')
            return redirect("polls:index")
    else:
        form = TextEmail(initial={
            'date_time': f'{(datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")}'
        })
    return render(request, 'send_mail.html', {
        'form': form,
    })
