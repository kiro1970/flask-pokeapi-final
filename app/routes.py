from urllib import response
from app import app
from flask import render_template, request, jsonify, redirect, url_for, flash
import requests
import json
from app import services
from .forms import PokeForm, LoginForm, RegistrationForm
from app import db
from app.models import Battle, User
from flask_login import current_user, login_required, login_user, logout_user


@app.route('/')
@app.route('/index')
@login_required
def home():
    return render_template('index.html', title="PokeAPI Battler!")

@app.route('/howitworks')
def about():
    return render_template('howitworks.html', title="Learn how to battle!")

@app.route('/letsbattle')
@login_required
def view():
    form = PokeForm()
    pokemon1 = None
    pokemon2 = None
    return render_template('letsbattle.html', title="Let's Battle!", form=form, pokemon1 = pokemon1, pokemon2 = pokemon2)

@app.route('/letsbattle', methods=['POST'])
@login_required
def battle():
    form = PokeForm()
    pokemon1input = request.form.get("pokemon1input")
    pokemon2input = request.form.get("pokemon2input")
    
    pokemon1 = services.getpokedata(pokemon1input)
    pokemon1 = services.Pokemon(pokemon1)
    pokemon2 = services.getpokedata(pokemon2input)
    pokemon2 = services.Pokemon(pokemon2)
    outcome1 = pokemon1.attack - pokemon2.defense
    outcome2 = pokemon2.attack - pokemon1.defense
    if outcome1 > outcome2:
        winner = pokemon1
    elif outcome2 > outcome1:
        winner = pokemon2
    elif pokemon1.hp > pokemon2.hp:
        winner = pokemon1
    else:
         winner = pokemon2
    print(winner.name)
    battle = Battle(player= current_user, YourPokemon=pokemon1.name, OpponentsPokemon=pokemon2.name, Winner=winner.name)
    db.session.add(battle)
    db.session.commit()
    return render_template('letsbattle.html', form=form, title="Let's Battle!", winner=winner, pokemon1=pokemon1, pokemon2=pokemon2)

@app.route('/results', methods=['POST', 'GET']) 
@login_required
def results():
    id = request.args.get("id")
    player = request.args.get("player")
    name = request.args.get("name")
    place = request.args.get("place")
    if id is not None:
        lines= Battle.query.filter_by(id = id)
    elif player is not None:
        user = User.query.filter(User.id == player).first()
        lines = user.battles
    elif place is not None:
        if place == '1':
            lines= Battle.query.filter(Battle.YourPokemon == name)
        elif place == '2':
            lines= Battle.query.filter(Battle.OpponentsPokemon == name)
        else:
            lines= Battle.query.filter(Battle.Winner == name)
    else:
        lines = Battle.query.all()
    

    return render_template('results.html', id=id, name=name, place=place, lines=lines)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)    