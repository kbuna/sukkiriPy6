class Competitor:
    def __init__(self, reputation):
        self.reputation = reputation

def update_competitor_reputation(competitor, events):
    # 競合他社の評判を更新
    for event in events:
        if event == "Negative":
            competitor.reputation *= 0.9
        elif event == "Positive":
            competitor.reputation *= 1.1