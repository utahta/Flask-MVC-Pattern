# vim:fileencoding=utf8
from myapp import db

class Projects(db.Model):
    def __init__(self, title, description):
        self.title = title
        self.description = description

# テーブル自動読み込み＆Projectsクラスにマッピング
# スキーマはSQLファイルにて定義
db.mapper(Projects,
          db.Table('projects', db.metadata, autoload=True))
