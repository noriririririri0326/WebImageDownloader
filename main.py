"""画像を一括保存するスクリプト"""

import os
import time

import requests  # type: ignore
from bs4 import BeautifulSoup

URL: str = ""  # 画像をDLするサイトURL
DL_DIR: str = r""  # dl先rootディレクトリ
IS_URL_TEXT_SAVE: bool = True


class BsContllorer:
    """BeautifulSoupを操作するクラス
    """

    def __init__(self):
        """コンストラクタ。指定されたURLをbs4に渡す。
        """
        self.req = requests.get(URL, timeout=100)
        self.soup = BeautifulSoup(self.req.text, "html.parser")

    def get_title(self) -> str:
        """ページタイトル(titleタグではない)を取得

        Returns:
            str: 取得したページタイトル文字列
        """
        return self.soup.select_one("#hoge-data > h1").get_text()

    def get_image_urls(self) -> list[str]:
        """画像のURL文字列を取得する。

        Returns:
            list[str]: 取得した画像のURL文字列
        """
        return [
            srcs.get("src") for srcs in self.soup.select("#hoge-data > img")
        ]

    def img_download(self, title_dir: str, srcs: list[str]) -> bool:
        """画像を保存する。

        Args:
            title_dir (str): 保存先フォルダ
            srcs (list[str]): 画像のURL

        Returns:
            bool: True:成功 False:失敗
        """
        res: bool = False

        count: int = 0

        for i, src in enumerate(srcs, 1):
            img = requests.get(src, stream=True, timeout=100)
            
            # ↓ファイル名どっちで保存するか。片方コメントアウトすること。
            # 素のファイル名で保存。
            file_name: str = os.path.basename(src)
            
            #連番に変換して保存。
            # _, ext = os.path.splitext(src)
            # file_name: str = f"{i:03}{ext}"
            
            save_path: str = os.path.join(title_dir, file_name)

            with open(save_path, "wb") as f:
                f.write(img.content)
                print(f"saved: {save_path}")
            count += 1
            time.sleep(1)

        print(f"{count} 枚保存しました。")

        res = True
        return res


def main():
    bc = BsContllorer()

    title = bc.get_title()

    title_dir = os.path.join(DL_DIR, title)

    # ダウンロードディレクトリ確認
    if not os.path.exists(title_dir):
        print(f"{title} フォルダを作成してよろしいですか？")
        print("y or n >")
        if input() == "y":
            os.mkdir(title_dir)
        else:
            print("キャンセルしました。")
            return False
    else:
        print(f"すでに {title} フォルダが存在します。")
        print("処理を中断します。")
        return False

    bc.img_download(title_dir, bc.get_image_urls())

    if IS_URL_TEXT_SAVE:
        text_path: str = os.path.join(title_dir, "url.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(URL)

    return True


if __name__ == "__main__":
    main()
