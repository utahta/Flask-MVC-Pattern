# vim:fileencoding=utf8
from flask import Module, render_template, redirect, url_for, request
from flaskext.wtf import Form, TextField, validators
from myapp.model.projects import ProjectsModel

projects = Module(__name__)

@projects.route('/')
def index():
    model = ProjectsModel()
    # リスト表示
    return render_template('projects/index.html', model=model)

class CreateForm(Form):
    """
    /projects/create 用のフォームクラス
    入力値チェックも担う
    """
    title = TextField(u'タイトル', [validators.Length(min=1, max=25)])
    description = TextField(u'説明', [validators.Length(min=1, max=100)])

@projects.route('/create', methods=("GET", "POST"))
def create():
    model = ProjectsModel()
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        # チェック通ったらデータを保存し、/projects へリダイレクト
        model.save(form.title.data, form.description.data)
        return redirect(url_for('projects.index'))
    # 作成画面を表示
    return render_template('projects/create.html', form=form)
