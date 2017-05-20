# このソフトウェアについて

アカウント登録のinsertサブコマンドコードを整理した。

# 変更箇所

* insertサブコマンドの実装を別ファイルにした。`./cui/register/Main.py`から`./cui/register/command/Inserter.py`に移した。
* insertサブコマンドの`-m`起動引数を削除した
    * GitHubAPIから取得するので不要

# 前回まで

* https://github.com/ytyaru/GitHub.Upload.Read.SshConfig.201704051338
* https://github.com/ytyaru/GitHub.Upload.GetMailAddressForAPI.201704041114
* https://github.com/ytyaru/GitHub.Upload.SSH.Check.201704040709
* https://github.com/ytyaru/GitHub.Upload.SSH.key.gen.201704031547
* https://github.com/ytyaru/GitHub.DB.Accounts.Create.Table.SshKeys.201704031424
* https://github.com/ytyaru/GitHub.Upload.UserRegister.Insert.Token.201704031122
* https://github.com/ytyaru/GitHub.Upload.UserRegister.CUI.201703311858
* https://github.com/ytyaru/GitHub.Upload.CUI.Account.SubCommand.201703302040
* https://github.com/ytyaru/GitHub.Upload.Headers.License.201703301853
* https://github.com/ytyaru/GitHub.Upload.Http.Response.201703301533
* https://github.com/ytyaru/GitHub.Upload.Response.201703291452
* https://github.com/ytyaru/GitHub.Upload.Delete.CommentAndFile.201703281815
* https://github.com/ytyaru/GitHub.Upload.Add.CUI.Directory.201703281703
* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.refactoring.GitHubApi.201703280740
* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.refactoring.Pagenation.201703271311
* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.refactoring.Response.201703270700
* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.refactoring.Data.201703261947
* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.Callable.refactoring.201703261352

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## GitHubアカウント登録

1. [GitHubアカウント登録ページ](https://github.com/join)にてアカウントを登録する
1. 指定したメールアドレスにGitHubからメールが届くので確認する
1. リンクをクリックしてメールアドレスを`verified`にする

GitHubアカウント登録と有効なメールアドレスの登録が完了した。

## SSH設定

`~/.ssh/config`に対象アカウントの設定をしておく。たとえば以下のように。

```
Host github.com.user1
  User git
  Port 22
  HostName github.com
  IdentityFile /home/mint/.ssh/github/rsa_4096_user1
  TCPKeepAlive yes
  IdentitiesOnly yes
```

# 実行

```sh
$ python3 GitHubUserRegister.py insert -u user1 -p pass -s github.com.user1
```

# 結果

`~/.ssh/config`ファイルから設定を読み込んで以下を行う。

* [GitHubにSSH公開鍵を登録する](https://developer.github.com/v3/users/keys/#create-a-public-key)
* DBに登録する
    * Host
    * 鍵(ファイルパス、鍵の値)
    * ssh-keygen値
        * bits(4096)
        * type(rsa)

`GitHub.Accounts.sqlite3`DBファイルにはSSH秘密鍵まで保存するのでDBの扱いは要注意。いずれどうするか考える。

# 課題

* Tokenが多くて邪魔
    A. 現在のように権限別で複数のTokenを作成する
    B. ツールで1つのTokenにし、権限は適時変更しながら使う
        * SSH鍵登録したTokenを削除するとSSH鍵設定も削除されてしまう
* SSH鍵生成時に、任意の値を指定したい
    * 暗号化方式
    * 暗号化強度
* SSHのconfigを編集したい（定義順などきれいに整形したい）

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)
[furl](https://github.com/gruns/furl)|[Unlicense](http://unlicense.org/)|[gruns/furl](https://github.com/gruns/furl/blob/master/LICENSE.md)
[PyYAML](https://github.com/yaml/pyyaml)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2006 Kirill Simonov](https://github.com/yaml/pyyaml/blob/master/LICENSE)

