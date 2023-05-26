from .. import db


agency_incident = db.Table('agency_incident',
    db.Column('agency_id', db.Integer, db.ForeignKey('agency.id'), primary_key=True),
    db.Column('incident_id', db.Integer, db.ForeignKey('incident.id'), primary_key=True)
)

