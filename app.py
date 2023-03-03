from flask import Flask, request, render_template
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """ Show homepage for story selection """

    return render_template('story-select.html', stories=stories)
    

@app.route('/form', methods=["POST"])
def form():
    """ Show form with prompts for chosen story instance"""

    ind = int(request.form.get('stories'))
    return render_template('form.html', prompts=stories[ind].prompts, ind=ind)

@app.route('/story/<int:storyInd>', methods=["POST"])
def story_page(storyInd):
    """ Show story """

    form_data = request.form
    new_story = stories[storyInd].generate(form_data)
    return render_template('story.html', new_story=new_story)
