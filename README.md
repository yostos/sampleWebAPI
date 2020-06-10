# これは何？

検証で Web APIのサーバーが必要だったので、急遽作ったなんちゃってAPIサーバー。

SinatraとFlask の２つのパターンで実装しています。

## Sinatra の実行方法

```sh
$ bundle exec ruby app.rb
```

ポートは 4567 を使います。

## Flask

- 必要に応じて virutalenvなどで環境を作成ください。

```sh
$ pip install -r requirements.txt
$ ./hello.sh
```

ポートは 5000 を使います。


## 確認方法

curlで検証する場合は、以下の通り

```sh
$  curl http://localhost:4567/api -X POST -H "Content-Type: application/json" --data '{"userid" : "0990909090"}'
{"user":{"age":29,"company":"White Company","gender":"male","id":"0990909090","name":"山田太郎"}}
```

Siegeを使う場合は以下の通り。

以下では、同時接続数 129接続、5秒間テストを実行する。

```sh
$ siege -c 129 -t 5s -b -T "application/json" 'http://localhost:4567/api POST {"userid":"1234567890"}'
```
