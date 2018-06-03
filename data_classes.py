from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass(
    order=True  # Add ordering methods
)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)  # First field, so comparing starts with it
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)

    def __str__(self):
        return f'{self.suit}{self.rank}'


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass()
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


default_deck = Deck()
print(f'default_deck: {default_deck}')
sorted_deck = Deck(sorted(make_french_deck()))
print(f'sorted_deck: {sorted_deck}')


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


my_card = ImmutableCard(rank='A', suit='Spades')
try:
    my_card.suit = 'Hearts'
except Exception as ex:
    print(f'Error: {ex}')

print('-' * 40)


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, repr=False, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, repr=False, metadata={'unit': 'degrees'})

    def distance_to(self, other):
        """Calculate the distance between two positions by using the Haversine formula."""
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2) ** 2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))


for field_data in fields(Position):
    print(field_data)

oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
null_island = Position('Null Island')
print(f'null_island: name={null_island.name!r}, lon={null_island.lon}, lat={null_island.lat}')
print(f'Distance between Oslo and Vancouver: {oslo.distance_to(vancouver)}')


@dataclass
class Capital(Position):
    country: str = ''  # needs a default argument because previous fields have them


capital = Capital(name='A Capital')
print(f'{capital.name} - LonLat: {capital.lon}, {capital.lat}')

print('-' * 40)


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']

    name: str
    lon: float
    lat: float
