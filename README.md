# 画像一括保存するやーつ

自分用

## 前準備

pipで以下インスコ

```bash
>pip install requests
>pip install beautifulsoup4
```

9行目にURLを入力

```py
URL: str = "https://************"  # 画像をDLするサイトURL
```

10行目にDL先フォルダを入力

```py
DL_DIR: str = r"C:\hoge\fuga"  # dl先rootディレクトリ
```

## 使い方

1. 実行
2. 〇〇フォルダを作成うんぬんかんぬん →ターミナルに```y```入力で実行。```y```以外入力でキャンセル。
3. おしり。

## その他

適宜23行目```def get_title(self)```や31行目```def get_image_urls(self)```の中身を書き換えること
