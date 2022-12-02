def count_rate(reviews: list) -> float:
    """Вовзращает средний рейтинг товара (если обзоров нет, то 0)"""
    rate_sum = 0
    if len(reviews) == 0:
        return 0
    for review in reviews:
        rate_sum += review.rating
    return rate_sum/len(reviews)

