from api import db
from api.Model.circonscription.models import Commune
from api.Model.elector.model import Elector


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    elector_id = db.Column(db.Integer, db.ForeignKey(Elector.id, nullable=False))
    commune_id = db.Column(db.Integer, db.ForeignKey(Commune.id, nullable=False))


db.create_all()
