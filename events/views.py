from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Event, Interest
from .forms import EventForm

def home(request):
    latest_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:6]
    return render(request, 'events/home.html', {'latest_events': latest_events})

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    interests = Interest.objects.all()
    
    selected_interest = request.GET.get('interest')
    if selected_interest:
        events = events.filter(interests__id=selected_interest)
    
    return render(request, 'events/event_list.html', {
        'events': events,
        'interests': interests,
        'selected_interest': selected_interest
    })

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            form.save_m2m()  # İlgi alanlarını kaydet
            messages.success(request, 'Etkinlik başarıyla oluşturuldu!')
            return redirect('event_detail', event.id)
    else:
        form = EventForm()
    
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Etkinlik Oluştur'})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    is_participant = request.user.is_authenticated and event.participants.filter(id=request.user.id).exists()
    
    return render(request, 'events/event_detail.html', {
        'event': event,
        'is_participant': is_participant
    })

@login_required
def event_join(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if event.max_participants and event.participants.count() >= event.max_participants:
        messages.error(request, 'Bu etkinlik maksimum katılımcı sayısına ulaşmış!')
    else:
        event.participants.add(request.user)
        messages.success(request, 'Etkinliğe başarıyla katıldınız!')
    
    return redirect('event_detail', pk=pk)

@login_required
def event_leave(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.participants.remove(request.user)
    messages.success(request, 'Etkinlikten ayrıldınız.')
    return redirect('event_detail', pk=pk)
