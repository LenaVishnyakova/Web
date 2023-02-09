from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
import datetime

from users.models import Note
from users.forms import NoteForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


def prof(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.data = datetime.date.today()
            note.save()
    else:
        form = NoteForm()

    notes_all = Note.objects.filter(user=request.user)

    context = {
        'form': form,
        'notes_all': notes_all,
    }

    return render(request, 'users/profile.html', context)
