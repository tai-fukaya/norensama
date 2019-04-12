# のれん様プログラム
## 残タスク
x 人感センサーのチューニング
x 実際使用するMacでのテスト
x 加速度センサーのチューニング
x ツイッターに対するレスポンス
x 天気情報の取得
x 天気情報に対するレスポンス
x 各種ふるまいの制作
セリフを言うタイミングのチューニング
１時間で、どれだけパケット消費するかのチェック
起動終了のマニュアルの作成
ウェブソケットがIPを指定しないと通信できないので、治す→引数に指定する

x Twitterを別スレッドに
x ファイル名のタイポを治す
強制アクションの仕組み
x 音声ファイルの再生開始をできるだけ早く

## 余裕が出たら
人力AIのUIのブラッシュアップ
ツイッター画面に対して、加工する

## Sensor
センサーにデータが欲しいと伝える
センサーから、データを受け取る
x Serial
x obniz
espのみ
raspberry pi

https://qiita.com/ie4/items/ae850cdb2c617f3fd6af
https://qiita.com/juosugi/items/66f25cc60734d17bc7f0
http://arakaze.ready.jp/archives/4278
https://www.slideshare.net/lemiyachi/espwroom02
→よくわからん

### obniz
x 受け取ったセンサー情報をOSCでサーバーに送信する

## Speaker
x 指定されたファイルを再生する

## Tweet
x 指定された文言を投稿する
RTがあったら、教える

## IFTTT
インスタグラムの投稿があったら
ツイッターでフォローされたら
ツイッターでRTされたら
ツイッターでメンションされたら
フォロワーの数はできる？

## Weather
一定期間ごとに、天気予報を見に行く
https://qiita.com/Barbara/items/93ae7969691164c7c2bc

## HumanIntelligence
x サーバーに強制実行するものがないか見に行く

## StatusManager
x 時間を教える
x センサー情報を教える
天気情報を教える
x 強制実行するセリフを教える

## Action
x 起動する条件にあったら、セリフとツイートをする
x 起動したら、しばらく休む

## NorenSama
x 定期的にStatusManagerに情報を教えてもらう
x 定期的にActionに起動するかどうか聞いて回る
x 起動したものがあれば、しばらく休む
RTがあったときに、起動中のActionが終わるのを待って、チロリンと鳴らす

# ディスプレイプログラム
## Updater
x ツイートの更新を取得する
x 取得したら、再描画

# 人力AI
x pythonでサーバーを立ち上げる
x POSTにデータを入れて、セリフを実行する

## ForceSerif
x アクションを指定せずに、喋る文章を選ぶ、サーバーに送る

# 音声合成APIについて
http://voicetext.jp/

# ポケットWifiの設定
プライバシーセパレーターはOFFにすること

https://qiita.com/makaishi2/items/ae83828a711d0d946011
https://qiita.com/makaishi2/items/ed9d4412331d7d65fde5
https://qiita.com/makaishi2/items/5c7b1b6a72b6938cf3d2

Exception in thread Thread-3:
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/Users/owner/Documents/norensama/python/status/twitter_manager.py", line 63, in update
    self._mention_messages.extend(self._twitter.get_mention_timeline())
TypeError: 'NoneType' object is not iterable


Exception in thread Thread-3:
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/Users/owner/Documents/norensama/python/status/twitter_manager.py", line 59, in update
    hashtags = self._twitter.get_hashtags("のれんさま")
  File "/Users/owner/Documents/norensama/python/twitter.py", line 127, in get_hashtags
    self.old_hashtag_created_at = tweets['statuses'][0]['created_at']

events.js:183
      throw er; // Unhandled 'error' event
      ^

Error: connect ETIMEDOUT 192.168.128.196:80
    at Object._errnoException (util.js:1022:11)
    at _exceptionWithHostPort (util.js:1044:20)
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1182:14)
WARNING:websocket_server.websocket_server:Client must always be mas

Exception in thread Thread-3:
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/Users/owner/Documents/norensama/python/status/twitter_manager.py", line 55, in update
    self._has_follower = self._has_follower or self._twitter.has_follower()
  File "/Users/owner/Documents/norensama/python/twitter.py", line 90, in has_follower
    res = self._session.get(USER_PROFILE_URL, params = params)
  File "/Users/owner/Library/Python/2.7/lib/python/site-packages/requests/sessions.py", line 525, in get
    return self.request('GET', url, **kwargs)
  File "/Users/owner/Library/Python/2.7/lib/python/site-packages/requests/sessions.py", line 512, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/owner/Library/Python/2.7/lib/python/site-packages/requests/sessions.py", line 622, in send
    r = adapter.send(request, **kwargs)
  File "/Users/owner/Library/Python/2.7/lib/python/site-packages/requests/adapters.py", line 495, in send
    raise ConnectionError(err, request=request)
ConnectionError: ('Connection aborted.', error(54, 'Connection reset by peer'))

# メリでめ将来性の整理
社員がウェブ上から任意のどんな言葉でも設定できるように
声の強弱をいつも同じではないように
自分が直前に何を言っていたかを覚えている
