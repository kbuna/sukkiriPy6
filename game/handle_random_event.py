def handle_random_event(consumer, events):
    # ランダムイベントによる影響を処理
    for event in events:
        if event == "SuddenDiscount":
            consumer.attributes["budget"] *= 0.8
        elif event == "NewTrend":
            consumer.attributes["interests"].append("trendy")