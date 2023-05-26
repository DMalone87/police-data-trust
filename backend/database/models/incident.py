"""Define the SQL classes for Users."""
import enum


from ..core import CrudMixin, SourceMixin, db

class RecordType(enum.Enum):
    NEWS_REPORT = 1
    GOVERNMENT_RECORD = 2
    LEGAL_ACTION = 3
    PERSONAL_ACCOUNT = 4

class InitialEncounter(enum.Enum):
    UNKNOWN = 1
    TRAFFIC_VIOLATION = 2
    TRESSPASSING = 3
    POTENTIAL_CRIMINAL_SUSPECT = 4
    OTHER = 5


class VictimWeapon(enum.Enum):
    UNKNOWN = 1
    FIREARM = 2
    BLADE = 3
    BLUNT = 4
    NO_WEAPON = 5
    OTHER = 6


class VictimAction(enum.Enum):
    UNKNOWN = 1
    SPEAKING = 2
    NO_ACTION = 3
    FLEEING = 4
    APPROACHING = 5
    ATTACKING = 6
    OTHER = 7


class CauseOfDeath(enum.Enum):
    UNKNOWN = 1
    BLUNT_FORCE = 2
    GUNSHOT = 3
    CHOKE = 4
    OTHER = 5


class VictimStatus(enum.Enum):
    UNKNOWN = 1
    UNHARMED = 2
    INJURED = 3
    DISABLED = 4
    DECEASED = 5


# TODO: This file's a bit of a mess (my fault!)
#  There are a lot of association tables in here, and the incidents table is
#  not clearly either a facts table or component table.
#  We need to get a better idea of the relationships we want and then we should
#  implement them accordingly.


class Incident(db.Model, CrudMixin, SourceMixin):
    """The incident table is the fact table."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_id = db.Column(db.Integer, db.ForeignKey("source.id"))
    description = db.Column(db.Text)
    record_type = db.Column(db.Enum(RecordType))
    time_of_incident = db.Column(db.DateTime)
    time_confidence = db.Column(db.Integer)
    has_attachments = db.Column(db.Boolean)
    complaint_date = db.Column(db.Date)
    publication_name = db.Column(db.Text)
    publication_date = db.Column(db.Date)
    author = db.Column(db.Text)
    source_url = db.Column(db.Text)
    closed_date = db.Column(db.Date)
    location = db.Column(db.Text)  # TODO: location object
    # Float is double precision (8 bytes) by default in Postgres
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    stop_type = db.Column(db.Text)  # TODO: enum
    call_type = db.Column(db.Text)  # TODO: enum
    was_victim_arrested = db.Column(db.Boolean)
    arrest_id = db.Column(db.Integer)  # TODO: foreign key of some sort?
    # Does an existing warrant count here?
    criminal_case_brought = db.Column(db.Boolean)
    case_id = db.Column(db.Integer)  # TODO: foreign key of some sort?
    # TODO: Remove this. incident-officer relationship is many-many using
    # accusation as the join table.
    officers = db.relationship("Officer", backref="incident")
    agencies_present = db.relationship('Agency', secondary='agency_incident', backref='incidents')
    tags = db.relationship("Tag", backref="incident")
    participants = db.relationship("Participant", backref="incident")
    attachments = db.relationship("Attachments", backref="incident")
    investigations = db.relationship("Investigation", backref="incident")
    results_of_stop = db.relationship("ResultOfStop", backref="incident")
    actions = db.relationship("Action", backref="incident")
    use_of_force = db.relationship("UseOfForce", backref="incident")
    legal_case = db.relationship("LegalCase", backref="incident")
    accusations = db.relationship("Accusation", backref="incident")


