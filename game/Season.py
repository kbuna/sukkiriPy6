class Season:
    def __init__(self, name, consumer_preferences):
        self.name = name
        self.consumer_preferences = consumer_preferences

# 季節ごとの効果や変動を設定
seasons = [
    Season("Spring", {"fashion": 1.2, "food": 0.8}),
    Season("Summer", {"technology": 1.3, "sports": 1.1}),
    # ...
]

def apply_seasonal_effect(consumer, current_season):
    for interest, multiplier in current_season.consumer_preferences.items():
        if interest in consumer.attributes["interests"]:
            # 消費者の好みに基づいて効果を適用
            consumer.attributes["interests"][interest] *= multiplier