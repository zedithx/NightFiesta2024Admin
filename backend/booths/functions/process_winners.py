import numpy as np
import pandas as pd
from booths.models import Player

POOL_NUMBER = 6
WINNER_NUMBER = 3


def process_winners():
    """Get top 30 winners """
    players = Player.objects.all()
    players = players.order_by('-score')[:POOL_NUMBER]
    players = players.values('id', 'name', 'score')
    df = pd.DataFrame.from_records(players)
    total_score = np.sum(df['score'])
    df['weight'] = df['score'] / total_score
    print(df)
    return np.random.choice(df['name'], WINNER_NUMBER, p=df['weight'], replace=False)


