from django.test import TestCase
from .models import Card, Deck


class CardTestCase(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None

    def setUp(self):
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(parentDeck=self.deck,
                                         front='front_of_card_1',
                                         back = 'back_of_card_1')
        self.card2 = Card.objects.create(parentDeck=self.deck,
                                         front='front_of_card_2',
                                         back='back_of_card_2')
        self.card3 = Card.objects.create(parentDeck=self.deck,
                                         front='front_of_card_3',
                                         back='back_of_card_3')


    def test_starting_conditions(self):
        '''
        Проверяет существование раздела и карточек
        '''
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertIsInstance(self.card2, Card)
        self.assertIsInstance(self.card3, Card)


    def test_card_has_previous(self):
        '''
        Первая карточка не имеет предыдущей. Остальные имеют
        '''
        self.assertFalse(self.card1.has_prev_card())
        self.assertTrue(self.card2.has_prev_card())
        self.assertTrue(self.card3.has_prev_card())


    def test_card_has_next(self):
        '''
        Первая карточка не имеет предыдущей. Остальные имеют
        '''
        self.assertTrue(self.card1.has_next_card())
        self.assertTrue(self.card2.has_next_card())
        self.assertFalse(self.card3.has_next_card())

    def test_get_prev_card(self):
        '''
        Последняя карточка возвращает None. Остальные возвращают следующую карточку
        '''
        self.assertIsNone(self.card1.get_prev_card())
        self.assertEqual(self.card1, self.card2.get_prev_card())
        self.assertEqual(self.card2, self.card3.get_prev_card())


    def test_get_next_card(self):
        '''
        Последняя карточка возвращает None. Остальные возвращают следующую карточку
        '''
        self.assertIsNone(self.card3.get_next_card())
        self.assertEqual(self.card3, self.card2.get_next_card())
        self.assertEqual(self.card2, self.card1.get_next_card())


    def test_random_card_from_deck(self):
        '''
        Вызывает deck.get_random_card 100 раз
        '''
        for _ in range(100):
            self.assertIn(self.deck.get_random_card(), [self.card1, self.card2, self.card3])