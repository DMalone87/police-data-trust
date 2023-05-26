import enum
from .. import db

class JURISDICTION(enum.Enum):
    FEDERAL = 1
    STATE = 2
    COUNTY = 3
    MUNICIPAL = 4
    PRIVATE = 5
    OTHER = 6

class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    incident_id = db.Column(db.Integer, db.ForeignKey("incident.id"))
    name = db.Column(db.Text)
    hq_address = db.Column(db.Text)
    hq_city = db.Column(db.Text)
    hq_zip = db.Column(db.Text)
    jurisdiction = db.Column(db.Enum(JURISDICTION))
