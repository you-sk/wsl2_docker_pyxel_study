#!/usr/bin/env python3
import os
import subprocess

print("=== Display環境変数テスト ===")
print(f"DISPLAY: {os.environ.get('DISPLAY', 'Not set')}")
print(f"SDL_VIDEODRIVER: {os.environ.get('SDL_VIDEODRIVER', 'Not set')}")
print(f"SDL_AUDIODRIVER: {os.environ.get('SDL_AUDIODRIVER', 'Not set')}")

print("\n=== X11接続テスト ===")
try:
    result = subprocess.run(['xdpyinfo'], capture_output=True, text=True)
    if result.returncode == 0:
        print("X11サーバーに接続成功")
    else:
        print(f"X11サーバーに接続失敗: {result.stderr}")
except FileNotFoundError:
    print("xdpyinfoコマンドが見つかりません")

print("\n=== SDL2ライブラリ確認 ===")
try:
    result = subprocess.run(['ldd', '/usr/local/lib/python3.13/site-packages/pyxel/pyxel_platform.cpython-313-x86_64-linux-gnu.so'], capture_output=True, text=True)
    print(result.stdout)
except Exception as e:
    print(f"エラー: {e}")