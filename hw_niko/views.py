from abc import ABC
from datetime import datetime, timedelta

from django.db.models import Avg, Count, Func
from django.shortcuts import redirect, render
from django.views import generic




# def text_mail(request):
#     if request.method == "POST":
#         form = TextEmail(request.POST)
#         if form.is_valid():
#             # result = f'Successfully added reminder on {form.cleaned_data["date_time"]}'
#             send_email.apply_async((form.cleaned_data['subject'],
#                                     form.cleaned_data['date_time'],
#                                     form.cleaned_data['text'],
#                                     ), eta=form.cleaned_data['date_time'])
#             return redirect("reminder-form")
#     else:
#         form = TextEmail(initial={
#             'date_time': f'{(datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")}'
#         })
#     return render(request, 'send_mail.html', {
#         'form': form,
#     })
