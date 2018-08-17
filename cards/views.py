from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .models import Deck, Card
from .forms import DeckForm, CardForm


def home(request):
    qs = Deck.objects.order_by('title').filter(is_active=True)
    context = {'decks': qs}
    return render(request, 'cards/home.html', context)


def createDeck(request):
    if request.method == 'POST':
        form= DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cards:home'))
    else:
        form = DeckForm()
    context = {'form': form}
    return render(request, 'cards/createDeck.html', context)


def editDeck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        form= DeckForm(request.POST, instance=deck_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cards:home'))
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form, 'edit_mode':True, 'deck_obj':deck_obj}
    return render(request, 'cards/createDeck.html', context)


def deleteDeck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    deck_obj.delete()
    return HttpResponseRedirect(reverse('cards:home'))


def viewDeck(request, deck_id):
    '''
    :return: первую карточку из БД если не указан deck_id
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    card_obj = card_list.first()
    if request.method == 'GET' and 'card' in request.GET:
        card_obj = get_object_or_404(Card, id=request.GET['card'])
    context = {'deck_obj': deck_obj, 'card_obj': card_obj}
    return render(request, 'cards/viewDeck.html', context)


def createCard(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cards:viewDeck', args=[deck_obj.id]))
    else:
        form = CardForm(initial={'parentDeck': deck_obj})
    context = {'form':form}
    return render(request, 'cards/createCard.html', context)


def editCard(request, card_id):
    card_obj = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cards:home'))
    else:
        form = CardForm(instance=card_obj)
    context = {'form': form, 'edit_mode': True, 'card_obj':card_obj}
    return render(request, 'cards/createCard.html', context)


def deleteCard(request, card_id):
    card_obj = get_object_or_404(Card, id=card_id)
    card_obj.delete()
    return HttpResponseRedirect(reverse('cards:home'))
