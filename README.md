## ソースコードの構成

- mdのプレビューで見ると、壊れてしまう。

.
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
│   └── __init__.py
├── README.md
└── requirements.txt


## ソースコードの概要

fastAPIにより、RESTAPIを実装。pytestによりユニットテストを実装。

app/main.py：フィボナッチ数列を返す関数の実装および"/fib"エンドポイントでの動作を実装。

- フィボナッチ数列は、遅い再帰的な処理でもOverflawするまで問題なく動作すると考えられたので、再帰的な実装となっている。

- "/fib"エンドポイントの実装は、validation（PositiveInt）によって実装することを考えていたが、エラーハンドリングによるメッセージの定形化（{
 "status": 400,
 "message": "Bad request."
}）を優先して、validation無しでの実装となっている。

tests/test_main.py：app/main.pyで実装した"/fib"エンドポイントでの動作を確認するユニットテスト。

- GET以外のメソッドでのアクセスや、"/fib"以外へのアクセスは、この課題では扱っていないと考えた。fastAPIがデフォルトのエラーハンドリングを行っていることを確認した後コメントアウトしている。


## local環境

- ローカルホストの実行：app/ディレクトリに移動して、以下コマンド

$ uvicorn main:app --reload

- ユニットテストの実行：tests/ディレクトリに移動して、以下コマンド

$ pytest

