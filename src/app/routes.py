from app import app, db
from app.models import User, Event, RSVP
from app.forms import SignUpForm, LoginForm, CreateEventForm, RSVPForm
from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime
import uuid
import bcrypt
from sqlalchemy import select


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    error = None
    if form.validate_on_submit():
        # check if email is taken
        if User.query.filter_by(email=form.email.data).first():
            error = 'That email is already registered'
        else:
            hashed_passwd = bcrypt.hashpw(form.passwd.data.encode('utf-8'), bcrypt.gensalt())
            new_user = User(
                username=form.name.data,
                email=form.email.data,
                passwd=hashed_passwd
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', form=form, error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd):
            login_user(user)
            return redirect(url_for('events'))
        error = 'Wrong email or password'
    return render_template('login.html', form=form, error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home')
@login_required
def home():
    return redirect(url_for('home'))


@app.route('/events')
@login_required
def events():
    all_events = Event.query.order_by(Event.startTime.asc()).all()
    return render_template('events.html', events=all_events)


@app.route('/events/<uuid:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    creator = db.session.get(User, event.creatorId)
    return render_template('event_detailS.html', event=event, creator=creator)


@app.route('/events/new', methods=['GET', 'POST'])
@login_required
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        new_event = Event(ta.strip(),
            location=form.location.data.strip(),
            startTime=form.start_time.data,
            endTime=form.end_time.data,
            creatorId=current_user.userId,
            title=form.title.data.strip(),
            description=form.description.data,
            capacity=form.capacity.data,
            createdAt=datetime.utcnow(),
            updatedAt=datetime.utcnow()
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('events', event_id=new_event.eventId))
    return render_template('create_event.html', form=form)

@app.route('/event/<uuid:event_id>/rsvp', methods=['GET', 'POST'])
@login_required
def rsvp(event_id):
    form = RSVPForm()

    existing_rsvp = db.session.scalar(
        select(RSVP).where(
            RSVP.eventId == event_id,
            RSVP.userId == current_user.userId
        )
    
    )
    event = db.session.get(Event, event_id)
    if not event:
        abort(404)

    if form.validate_on_submit():
        if existing_rsvp:
            old_status = existing_rsvp.status
            if old_status == "not_going":
                if event.capacity == 0:
                    flash("Event is at maximum capacity.")
                    return redirect(url_for('event_details', event_id=event_id))
                elif form.status.data == "going" or "maybe":
                    event.capacity -= 1
                
            existing_rsvp.status = form.status.data

            if old_status == "going" or "maybe":
                if form.status.data == "not_going":
                    event.capacity += 1     
        else:
            if event.capacity == 0:
                flash("Event is at maximum capacity.")
                return redirect(url_for('event_details', event_id=event_id))
            new_rsvp = RSVP(
                eventId=event_id,
                userId=current_user.userId,
                status=form.status.data
            )
            if new_rsvp.status == "going" or "maybe":
                event.capacity -= 1
            db.session.add(new_rsvp)
            
        db.session.commit()
        return redirect(url_for('events', event_id=event_id))
        
    return render_template('rsvp.html', form=form)