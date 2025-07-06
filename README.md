# Python Docker環境

このプロジェクトは、DockerコンテナでPythonを実行するための環境です。

## セットアップ

### 必要なもの
- Docker
- Docker Compose

### ビルドと起動

```bash
# コンテナのビルドと起動
docker-compose up -d --build

# コンテナの停止
docker-compose down
```

## 使い方

### Pythonインタラクティブシェル
```bash
docker-compose exec python python
```

### Pythonスクリプトの実行
```bash
docker-compose exec python python ファイル名.py
```

## サンプルプログラム

### 1. hello.py
基本的な動作確認用プログラム
- Pythonバージョンの表示
- 簡単な計算処理
- 文字列操作のデモ

```bash
docker-compose exec python python hello.py
```

### 2. data_analysis.py
データ分析のサンプル
- 30日分のサンプルデータ（売上、訪問者数、気温）を生成
- データの統計情報を計算（合計、平均、最大、最小）
- 結果をJSONファイルに保存

```bash
docker-compose exec python python data_analysis.py
```

### 3. file_processor.py
ファイル処理のサンプル
- テキストファイルの単語数、行数、文字数をカウント
- サンプルテキストファイルを自動生成
- コマンドライン引数で複数ファイルの処理に対応

```bash
# 基本的な使い方
docker-compose exec python python file_processor.py

# 複数ファイルを処理
docker-compose exec python python file_processor.py file1.txt file2.txt
```

## ファイル構成

```
.
├── Dockerfile           # Python環境の定義
├── docker-compose.yml   # Docker Compose設定
├── requirements.txt     # Pythonパッケージの依存関係
├── .dockerignore       # Dockerビルド時の除外設定
├── README.md           # このファイル
├── hello.py            # サンプル: 基本動作確認
├── data_analysis.py    # サンプル: データ分析
└── file_processor.py   # サンプル: ファイル処理
```

## カスタマイズ

### Pythonパッケージの追加
`requirements.txt`に必要なパッケージを追加してください：

```txt
numpy==1.24.3
pandas==2.0.3
requests==2.31.0
```

追加後、コンテナを再ビルドしてください：
```bash
docker-compose up -d --build
```

### Pythonバージョンの変更
`Dockerfile`の1行目を編集してバージョンを変更できます：
```dockerfile
FROM python:3.11-slim  # 3.11を他のバージョンに変更
```

## トラブルシューティング

### コンテナが起動しない場合
```bash
# ログを確認
docker-compose logs

# コンテナの状態を確認
docker-compose ps
```

### ファイルの変更が反映されない場合
ボリュームマウントにより、ローカルの変更は自動的にコンテナ内に反映されます。
Pythonパッケージを追加した場合のみ、再ビルドが必要です。