import string
import secrets
from app import db
from flask_login import UserMixin
from datetime import datetime
from zoneinfo import ZoneInfo

DENVER = ZoneInfo('America/Denver')

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    userId = db.Column(db.UUID, primarykey=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    passwd = db.Column(db.LargeBinary, nullable=False)
    createdAt =  db.Column(db.DateTime, nullable=False)

class Event(db.model):
    __tablename__ = 'events'
    eventId = db.Column(db.UUID, primarykey=True)
    creatorId = db.Column(db.UUID, db.ForeignKey('users.userId'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    #TODO: getDetails

class RSVP(db.model):
    rsvpId = db.Column(db.UUID, primarykey=True)
    eventId = db.Column(db.UUID, db.ForeignKey('events.eventId'), nullable=False)
    userId = db.Column(db.UUID, db.ForeignKey('users.userId'), nullable=False)
    status = db.Column(db.RSVPStatus, nullable=False) #Gotta make this type in models too
    respondedAt = db.Column(db.DateTime, nullable=False)


class EditRequest(db.model):
    requesterId = db.Column(db.UUID, db.ForeignKey('users.userId'), nullable=False)
    proposedTitle = db.Column(db.String)
    proposedLocation = db.Column(db.String)
    proposedStartTime = db.Column(db.DateTime)
    proposedEndTime = db.Column(db.DateTime)
    comment = db.Column(db.String)
    status = db.Column(db.EditRequestStatus, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    reviewedAt = db.Column(db.DateTime)
    #TODO: Approve and reject functions






    





