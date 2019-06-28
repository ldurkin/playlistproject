from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'GET':
        return "Please fill out the form."
    else:
        userdata = formopener.dict_from(request.form)
        print(userdata)
        name = userdata['name']
        genre = userdata['genre']
        print(genre)
        results = model.findPlaylist(genre)
        playlistlink = results[0]
        embedlink = results[1]
        return render_template("results.html", name = name, genre = genre, playlistlink = playlistlink, embedlink=embedlink)