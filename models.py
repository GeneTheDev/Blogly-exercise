from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Create table"""
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, unique=True, nullable=False)
    last_name = db.Column(db.Text, unique=True, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    @classmethod
    def Name(self):
        """Return name of the user"""
        return f'{self.first_name}  {self.last_name}'
