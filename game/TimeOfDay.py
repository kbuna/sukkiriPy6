class TimeOfDay:
    def __init__(self, name, demand_multiplier):
        self.name = name
        self.demand_multiplier = demand_multiplier

# 時間帯ごとの効果を設定
time_of_day_effects = [
    TimeOfDay("Morning", 1.2),
    TimeOfDay("Afternoon", 1.0),
    TimeOfDay("Evening", 1.5)
]

def apply_time_of_day_effect(consumer, current_time_of_day):
    # 時間帯による効果を適用
    consumer.attributes["time_of_day_preference"] = current_time_of_day.demand_multiplier