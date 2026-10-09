import math
from datetime import datetime, timedelta, timezone

def calculate_sm2(rating, repetitions, interval, ease_factor):
    """
    SuperMemo SM-2 Spaced Repetition Algorithm
    
    Args:
        rating (int): Rating from 1 to 4:
            1: Blackout / Completely Incorrect
            2: Hard / Difficult Recall
            3: Good / Normal Recall
            4: Easy / Perfect Recall
        repetitions (int): Consecutive successful reviews count
        interval (int): Current interval in days
        ease_factor (float): Current ease factor multiplier (starts at 2.5)

    Returns:
        tuple: (new_repetitions, new_interval_days, new_ease_factor, next_review_datetime)
    """
    rating = int(rating)
    
    # Rating 1 = Fail, Reset repetitions to 0 and interval to 1 day
    if rating < 2:
        new_repetitions = 0
        new_interval = 1
    else:
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = math.ceil(interval * ease_factor)
        new_repetitions = repetitions + 1

    # Map 1-4 scale to original SM2 0-5 scale for formula precision:
    # 1 -> 1 (Incorrect)
    # 2 -> 3 (Hard)
    # 3 -> 4 (Good)
    # 4 -> 5 (Perfect)
    quality_map = {1: 1, 2: 3, 3: 4, 4: 5}
    q = quality_map.get(rating, 3)

    # SM-2 Ease Factor calculation formula:
    # EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    new_ease_factor = ease_factor + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    
    # Minimum ease factor bound in SM-2 specification is 1.3
    if new_ease_factor < 1.3:
        new_ease_factor = 1.3

    next_review = datetime.now(timezone.utc) + timedelta(days=new_interval)
    
    return new_repetitions, new_interval, round(new_ease_factor, 2), next_review
