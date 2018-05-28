from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen1 = DataClassCard('Q', 'Hearts')
print(f'queen1: {queen1} | queen1.rank: {queen1.rank}')
queen2 = DataClassCard(rank='Q', suit='Hearts')
print(f'queen1 == queen2: {queen1 == queen2}')
