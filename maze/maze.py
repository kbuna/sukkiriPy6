# 使用されてるBGM,効果音：魔王魂

import pygame
from pygame.locals import *
import sys, random
from tkinter import messagebox

# 変数の初期化
maze_w = 31  # 迷路の列数
maze_h = 23  # 迷路の行数
maze = []  # 迷路データ
tile_w = 16
px = 1  # プレイヤーの座標
py = 1

# BGM、SE用の定数と変数
BGM = pygame.mixer.music
move_se = None
goal_se = None

# 色を定義
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
brown = (115, 66, 41)
orange = (233, 168, 38)
maze_color = [white, brown, orange]


# 迷路を自動的に生成する
def make_maze():
    global maze, px, py
    px = 1
    py = 1
    tbl = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    # 全部を0(通路)で初期化
    maze = []
    for y in range(0, maze_h):
        row = []
        for x in range(0, maze_w):
            row.append(0)
        maze.append(row)
    # 周囲を1(壁)で初期化
    for x in range(0, maze_w):
        maze[0][x] = 1
        maze[maze_h - 1][x] = 1
    for y in range(0, maze_h):
        maze[y][0] = 1
        maze[y][maze_w - 1] = 1
    # 棒倒し法で迷路を生成
    for y in range(2, maze_h - 2):
        for x in range(2, maze_w - 2):
            if x % 2 == 0 and y % 2 == 0:
                r = random.randint(0, 3)
                maze[y][x] = 1
                maze[y + tbl[r][1]][x + tbl[r][0]] = 1
    # ゴールを右下に設定
    maze[maze_h - 2][maze_w - 2] = 2


# プレイヤーの移動を確認、音再生
def check_key(key):
    global px, py
    old_x, old_y = px, py
    # 移動操作
    if key == K_LEFT:
        px -= 1
    elif key == K_RIGHT:
        px += 1
    elif key == K_UP:
        py -= 1
    elif key == K_DOWN:
        py += 1
    # 音声関連
    if key == K_SPACE:
        switch_bgm()
    if key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
        move_se.play()

    if maze[py][px] == 2:  # ゴール?
        # メッセージダイアログ表示
        goal_se.play()
        messagebox.showinfo("ゴール", "宝を見つけた")
        make_maze()
    if maze[py][px] != 0:
        px, py = old_x, old_y


# BGMの再生、停止切替え
def switch_bgm():
    if BGM.get_busy():
        BGM.stop()
    else:
        BGM.play()


def main():
    # ゲームの初期化処理
    global px, py, move_se, goal_se
    pygame.init()
    pygame.display.set_caption("maze game")
    screen = pygame.display.set_mode((tile_w * maze_w, tile_w * maze_h))
    # 音声読み込み、音量設定、BGM再生開始
    try:
        # 音声ファイル読み込み
        BGM.load("bgm/maou_bgm_piano41.mp3")
        move_se = pygame.mixer.Sound("se/maou_se_system49.mp3")
        goal_se = pygame.mixer.Sound("se/maou_se_onepoint15.mp3")
        # 音量設定
        move_se.set_volume(0.05)
        goal_se.set_volume(0.2)
        pygame.mixer.music.set_volume(0.2)
        # BGM再生
        pygame.mixer.music.play()
    except:
        print("音声読み込みに失敗しました")
        return

    # 最初の迷路作成
    make_maze()

    # ゲームのメインループ
    while True:
        # 迷路を描画する
        screen.fill(black)
        for y in range(0, maze_h):
            for x in range(0, maze_w):
                v = maze[y][x]
                xx = tile_w * x
                yy = tile_w * y
                pygame.draw.rect(
                    screen, maze_color[v], (xx, yy, xx + tile_w, yy + tile_w)
                )
        # プレイヤーを円で描画する
        t2 = tile_w / 2
        pygame.draw.circle(screen, red, (px * tile_w + t2, py * tile_w + t2), t2)
        pygame.display.update()
        # イベントを処理する
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                check_key(event.key)


if __name__ == "__main__":
    main()