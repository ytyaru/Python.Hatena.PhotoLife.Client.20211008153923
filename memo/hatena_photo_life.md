# 明記されていない仕様

* http://developer.hatena.ne.jp/ja/documents/fotolife/apis/atom

## PostURI

> アップロード先のフォルダ名をdc:subject要素に
>   指定されたフォルダが存在しない場合は、自動的に作成されます。

* フォルダを指定しなければ「トップフォルダ」に配置される
* 自動作成されたフォルダの公開範囲は「自分のみ」である
  * 全員に公開する「トップと同じ」にしないとRSSで表示されない
    * 公開範囲の変更はAPIではできない
      * サイトからUIを操作することで変更する

## FeedURI

> フィードに含まれるエントリの件数は、はてなフォトライフでのユーザー設定によって決定されます。

* エントリ対象は「トップフォルダ」のみと思われる
* それ以外のフォルダに分類されると表示されない（公開範囲が「トップと同じ」であっても表示されない）

　なお、はてなフォトライフのサイトからRSSリンクを参照できる。フォルダごとにURLが分かれている。

* https://f.hatena.ne.jp/{hatena_id}/rss
* https://f.hatena.ne.jp/{hatena_id}/{folder}/rss

　引数`page`、`sort`がある。フォルダ名はURLエンコードされる。

* https://f.hatena.ne.jp/ytyaru/Hatena%20Blog/rss?page=1&sort=old
* https://f.hatena.ne.jp/ytyaru/Hatena%20Blog/rss?page=1&sort=new
* https://f.hatena.ne.jp/ytyaru/%E6%97%A5%E6%9C%AC%E8%AA%9E/rss
