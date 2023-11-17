class TextManager:
    def __init__(self):
        self.text_queue = []

    def add_text(self, text):
        # テキストをキューに追加
        self.text_queue.append(text)

    def display_text(self):
        # キューにあるテキストを順次表示
        for text in self.text_queue:
            print(text)
        self.text_queue = []  # 表示後はキューをクリア
