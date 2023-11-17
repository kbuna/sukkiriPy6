class Consumer:
    def __init__(self, attributes):
        self.attributes = attributes  # 属性として辞書型データを保持

def generate_consumer():
    # ランダムな属性を生成
    attributes = {
        "age": random.choice(["young", "middle-aged", "elderly"]),
        "gender": random.choice(["male", "female"]),
        "interests": random.sample(["fashion", "technology", "sports", "food"], k=random.randint(1, 3))
    }
    return Consumer(attributes)

def generate_purchase_text(self, product_name):
    # 消費者の個性に合った購入時のテキストを生成
    if self.personality == "enthusiastic":
        return f"{self.name}: これは最高の{product_name}だね！"
    elif self.personality == "practical":
        return f"{self.name}: {product_name}、コストパフォーマンスがいいね。"
    # 他のパーソナリティに対する条件分岐

"""
# 使用例
consumer = Consumer("Alice", "enthusiastic")
purchase_text = consumer.generate_purchase_text("新製品")
"""