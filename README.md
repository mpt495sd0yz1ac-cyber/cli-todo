# Python CLI TODO管理アプリ

## 概要
Pythonの基礎文法の理解を目的として、  
コマンドライン上で動作するTODO管理アプリを作成しました。  
標準ライブラリのみを使用し、環境依存のない構成にしています。

## 機能
- TODOの追加
- TODO一覧の表示
- TODOの完了／未完了の切り替え
- JSONファイルによるデータ保存

## 使用技術
- Python 3.x
- 標準ライブラリ（json, os）

## 実行環境
- Windows / macOS / Linux（Python 3.x）

## 実行方法

### 1. リポジトリのクローン
```bash
git clone https://github.com/mpt495sd0yz1ac-cyber/cli-todo.git
cd Desktop\business-python\cli-todo

2. プログラムの実行
python todo_list.py


- `1` : 
- `2` : 
- `3` : 
- `4` : 


3. 操作方法
起動後、以下のメニューが表示されます。
1:追加 2:表示 3:完了切替 4:終了
1 : Add a TODO(TODOを追加)
2 : Show TODO list(TODO一覧を表示)
3 : Toggle completion status(TODOの完了／未完了を切り替え)
4 : Exit program (data is automatically saved)プログラムを終了（データは自動保存）

**## 工夫した点**
- 処理ごとに関数を分け、可読性を意識しました
- JSON形式でデータを保存し、データの永続化を行いました
- 標準ライブラリのみで動作するよう設計しました

## 今後の改善点
- 入力値のエラーハンドリングの追加
- TODO削除機能の実装
- クラスを用いた設計への改善
