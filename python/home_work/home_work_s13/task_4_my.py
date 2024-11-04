class ScoreLimitExceededError(Exception):
    def __str__(self):
        return f'Input value less of 1000!'

class GameScore:
    def __init__(self):
        self.total_score = 0

    def add_score(self, user_score):
        self.total_score += user_score
        if self.total_score >= 1000:
            raise ScoreLimitExceededError

    def minus_score(self, user_score):
        self.total_score -= user_score
        if self.total_score < 0:
            raise ValueError("Еррррррор")

a = GameScore()
b = GameScore()
try:
    a.add_score(900)
    a.add_score(100)
    b.minus_score(100)
except Exception as e:
    print(e)




















