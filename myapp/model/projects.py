# vim:fileencoding=utf8
from myapp import db
from myapp.db.orm.projects import Projects

class ProjectsModel(object):
    
    def get_entries(self):
        return db.session.query(Projects).all()
    
    def save(self, title, description):
        db.session.add(Projects(title, description))
        db.session.commit()
