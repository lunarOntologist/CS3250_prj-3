
import uuid
from datetime import datetime

from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    userId = db.Column(
        db.Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwd = db.Column(db.LargeBinary, nullable=False)
    createdAt = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def get_id(self):
        return str(self.userId)


class Event(db.Model):
    __tablename__ = 'events'

    eventId = db.Column(
        db.Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    creatorId = db.Column(
        db.Uuid,
        db.ForeignKey('users.userId'),
        nullable=False
    )
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class RSVP(db.Model):
    __tablename__ = 'rsvps'

    rsvpId = db.Column(
        db.Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    eventId = db.Column(
        db.Uuid,
        db.ForeignKey('events.eventId'),
        nullable=False
    )
    userId = db.Column(
        db.Uuid,
        db.ForeignKey('users.userId'),
        nullable=False
    )
    status = db.Column(db.String(20), nullable=False, default='pending')
    respondedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class EditRequest(db.Model):
    __tablename__ = 'edit_requests'

    editRequestId = db.Column(
        db.Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    eventId = db.Column(
        db.Uuid,
        db.ForeignKey('events.eventId'),
        nullable=False
    )
    requesterId = db.Column(
        db.Uuid,
        db.ForeignKey('users.userId'),
        nullable=False
    )
    proposedTitle = db.Column(db.String(120))
    proposedLocation = db.Column(db.String(200))
    proposedStartTime = db.Column(db.DateTime)
    proposedEndTime = db.Column(db.DateTime)
    comment = db.Column(db.String)
    status = db.Column(db.String(20), nullable=False, default='pending')
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reviewedAt = db.Column(db.DateTime)
