# discord-onenight-werewolf

## Abstract
- Discordでワンナイト人狼を遊ぶことができます。
- ワンナイトではない人狼には対応していません。
- ボットは、プレイヤーから受け取ったコマンドをトリガーに動作します。
- エラー処理はガバガバです。

## Preparetion
1. `Docker`を使用可能な状態にします。
2. Discordでボットを登録し、`Token`を控えます。
3. このリポジトリを`git clone`します。
4. 2.で控えた`Token`を登録します

```
$ cd discord-onenight-werewolf`
$ echo "[Token]" >> key
```

5. `Docker`でコンテナを作成し、コンテナ上でボットを走らせて準備完了です。

```
$ docker image build -t dow .
$ docker-compose up -d
$ docker exec -d dow_container python run.py
```

## How to play
1. ゲームマスター的な人を決めておきます(ゲームマスターもゲームには参加可能です)。
2. ボットへ、DiscordのIMで`/getm`コマンドを送信し、Discordのチャンネル全員のリストを取得します。
3. ワンナイト人狼へ参加するプレイヤーのIDを確認し、`/setp [ID] ...`でプレイヤーを登録します(IDは、`/getm`で表示されたプレイヤー名の左端の数字です)。
4. 使用する役職を決め、`/setj [jobname] ...`で役職を登録します。役職名は、`villager`, `werewolf`, `seer`, `thief`, `madman`, `suisider`があります。それぞれ、村人、人狼、占い師、怪盗、狂人、吊人(てるてる)です。
5. `/getp`, `/getj`で、登録したプレイヤーと役職に間違いがないことを確認します。間違っていた場合、もう一度`/setp`, `/setj`コマンドで登録できます。
6. `/start`でゲームを開始します。ゲームを開始すると、各プレイヤーのIMへ、役割が配布されます。
7. あとは画面の指示通りに遊びます。
8. ゲーム終了後、もう一度同じプレイヤー、役職で遊びたい場合は`/start`で開始できます。変更したい場合は、3.へ戻ります。

## Appendix
- 役職を増やしたい場合は、`job/`下へ、`Job`を継承した`class`を作成します。その`class`では、`setName()`, `setDisplayName()`, `IamWerewolf()`の設定が必須です。役職の挙動は、`management/Master.py`に記述します。
