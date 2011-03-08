Flask MVC Sample.

Installation
============

Pythonと依存ライブラリのインストール::

  pythonbrew install 2.6.6
  pythonbrew switch 2.6.6
  pip install Flask
  pip install Flask-WTF
  pip install SQLAlchemy
  
Flas-MVC-Sampleのダウンロードとデータベース初期化::
  
  --- Download Flas-MVC-Sample & Uncompress ---
  cd Flask-MVC-Sample
  sqlite3 /tmp/test.db < myapp/db/sql/projects.sql

Usage
=====

実行::

  python main.py

