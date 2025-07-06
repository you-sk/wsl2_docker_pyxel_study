# Pyxel on WSL2 with Docker

WSL2環境でPyxelゲームエンジンを動作させるためのDockerプロジェクトです。  
グラフィックと音声の両方に対応しています。  
WSL2上にdockerがインストールされている前提です。  
windows版Docker Desktopによる動作は確認していません。  
サンプルプログラムの実行まで動作確認していますが、すべての環境での動作を保証するものではありません。

## 特徴

- 🎮 WSL2環境でPyxelアプリケーションを実行
- 🖼️ X11によるグラフィック表示対応
- 🔊 WSLgによる音声出力対応（Windows側への追加インストール不要）
- 🐳 Docker環境で依存関係を管理

## 必要な環境

- Windows 10/11 with WSL2
- WSLg（音声出力用）
  - `wsl --version`でWSLgバージョンが表示されることを確認
- WSL2内のDocker
- X11サーバー（WSLgに含まれる）

## セットアップ

1. **リポジトリのクローン**
   ```bash
   git clone https://github.com/you-sk/wsl2_docker_pyxel_study.git
   cd wsl2_docker_pyxel_study
   ```

2. **Dockerコンテナのビルドと起動**
   ```bash
   docker-compose up -d --build
   ```

## 使い方

### Pyxelアプリケーションの実行

```bash
# サンプルプログラムをコピー
docker-compose exec python pyxel copy_examples

# サンプルアプリケーションの実行例
（サンプルプログラムのコピー後）
docker-compose exec python python pyxel_examples/01_hello_pyxel.py
docker-compose exec python python pyxel_examples/02_jump_game.py
docker-compose exec python python pyxel_examples/03_draw_api.py
```

### Pyxelコマンドの使用

```bash
# Pyxelアプリケーションを実行
docker-compose exec python pyxel run your_app.py

# ファイル変更を監視して自動再実行
docker-compose exec python pyxel watch . your_app.py

# Pyxelエディタを起動（リソースファイルの編集）
docker-compose exec python pyxel edit

# アプリケーションをパッケージ化
docker-compose exec python pyxel package app_dir startup.py

# .pyxappファイルを実行
docker-compose exec python pyxel play your_app.pyxapp
```

### 独自のPyxelアプリケーション開発

1. プロジェクトルートに新しいPythonファイルを作成
2. Pyxelのインポートとアプリケーションコードを記述
3. 以下のコマンドで実行：
   ```bash
   docker-compose exec python python your_app.py
   ```

### コンテナ内でインタラクティブシェルを使用

```bash
docker-compose exec python bash
```

## トラブルシューティング

### グラフィックが表示されない場合

1. `$DISPLAY`環境変数を確認：
   ```bash
   echo $DISPLAY
   ```

2. X11の接続をテスト：
   ```bash
   docker-compose exec python python test_display.py
   ```

### 音声が出力されない場合

1. WSLgのバージョンを確認：
   ```bash
   wsl --version
   ```

2. 音声設定をテスト：
   ```bash
   docker-compose exec python python test_audio.py
   ```

3. 音声が不要な場合は、`docker-compose.yml`で`SDL_AUDIODRIVER=dummy`に設定

### SDL2初期化エラーが発生する場合

現在の設定はソフトウェアレンダリングを使用しています。これはWSL2環境での互換性を確保するためです。

## プロジェクト構成

```
pyxel_study/
├── docker-compose.yml      # Docker設定（WSLg対応）
├── Dockerfile             # Pyxel実行環境の定義
├── requirements.txt       # Pythonパッケージ
├── test_display.py        # ディスプレイ設定テスト
├── test_audio.py          # 音声設定テスト
└── README.md             # このファイル
```

## 技術詳細

### 環境変数

- `DISPLAY`: X11ディスプレイ設定
- `PULSE_SERVER`: WSLgのPulseAudioサーバー
- `SDL_VIDEODRIVER`: X11を使用
- `SDL_AUDIODRIVER`: PulseAudioを使用
- `LIBGL_ALWAYS_SOFTWARE`: ソフトウェアレンダリング有効化

### マウントポイント

- `/tmp/.X11-unix`: X11ソケット
- `/mnt/wslg`: WSLgの共有ディレクトリ（音声用）

## ライセンス

MITライセンスで公開しています。
