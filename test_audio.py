#!/usr/bin/env python3
import os
import subprocess

print("=== PulseAudio環境変数テスト ===")
print(f"PULSE_SERVER: {os.environ.get('PULSE_SERVER', 'Not set')}")
print(f"SDL_AUDIODRIVER: {os.environ.get('SDL_AUDIODRIVER', 'Not set')}")

print("\n=== PulseAudioサーバー接続テスト ===")
try:
    result = subprocess.run(['pactl', 'info'], capture_output=True, text=True)
    if result.returncode == 0:
        print("PulseAudioサーバーに接続成功")
        print(result.stdout)
    else:
        print(f"PulseAudioサーバーに接続失敗: {result.stderr}")
except FileNotFoundError:
    print("pactlコマンドが見つかりません")

print("\n=== 音声デバイス一覧 ===")
try:
    result = subprocess.run(['pactl', 'list', 'short', 'sinks'], capture_output=True, text=True)
    if result.returncode == 0:
        print("利用可能な音声出力デバイス:")
        print(result.stdout)
    else:
        print(f"デバイス一覧取得失敗: {result.stderr}")
except FileNotFoundError:
    pass