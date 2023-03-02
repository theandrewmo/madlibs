from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """ Show homepage with form """
    
    return render_template('home.html', prompts=story.prompts)

@app.route('/story', methods=["POST"])
def story_page():
    """ Show story """

    form_data = request.form
    new_story = story.generate(form_data)
    return render_template('story.html', new_story=new_story)