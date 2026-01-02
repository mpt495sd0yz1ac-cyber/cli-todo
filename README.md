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
cd cli-todo
⚠️ Windows PowerShell を使う場合
日本語表示が文字化けすることがあります。その場合は英語メニューを使うか、PowerShellのコードページをUTF-8に変更してください：

powershell
コードをコピーする
chcp 65001
2. プログラムの実行
bash
コードをコピーする
python todo_list.py
3. 操作方法
起動後、以下のメニューが表示されます。

コードをコピーする
1: Add 2: Show 3: Toggle 4: Exit
----------------------------------------
1 : Add a TODO (TODOを追加)
2 : Show TODO list (TODO一覧を表示)
3 : Toggle completion status (TODOの完了／未完了を切り替え)
4 : Exit program (データは自動保存されます)

## 工夫した点
- 処理ごとに関数を分け、可読性を意識しました
- JSON形式でデータを保存し、データの永続化を行いました
- 標準ライブラリのみで動作するよう設計しました

## 今後の改善点
- 入力値のエラーハンドリングの追加
- TODO削除機能の実装
- クラスを用いた設計への改善
