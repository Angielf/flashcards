from django.urls import path
from . import views


app_name='cards'
urlpatterns = [
    path('', views.home, name='home'),
    path('decks/create/', views.createDeck, name='createDeck'),
    path('decks/edit/<int:deck_id>', views.editDeck, name='editDeck'),
    path('decks/delete/<int:deck_id>', views.deleteDeck, name='deleteDeck'),
    path('decks/view/<int:deck_id>', views.viewDeck, name='viewDeck'),
    path('words/create/<int:deck_id>', views.createCard, name='createCard'),
    path('words/edit/<int:card_id>', views.editCard, name='editCard'),
    path('words/delete/<int:card_id>', views.deleteCard, name='deleteCard'),
]