class SceneManager:
    def __init__(self):
        self.current_scene = None

    def change_scene(self, new_scene):
        # 現在のシーンを切り替える
        self.current_scene = new_scene

class Scene:
    def __init__(self, name):
        self.name = name

    def start(self):
        # シーンが開始されたときの処理
        pass

    def update(self):
        # シーンが更新されるときの処理
        pass

    def render(self):
        # シーンが描画されるときの処理
        pass
