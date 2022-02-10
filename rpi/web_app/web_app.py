import threading
import time

from flask import *
from scores import *
from game.led import LEDClass
from game.arduinoConnection import ArduinoClass
from game.game import play
from turbo_flask import Turbo


app = Flask(__name__, static_folder='static')
json_name = 'scores.json'

turbo = Turbo(app)

STATUS = 'Ready'
LASTSCORE = ''
ARDUINO = None
LED = None

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

# @app.teardown_appcontext
# def teardown_appcontext(response_or_exc):
#     LED.clearLeds()

@app.route('/')
def index():
    return render_template('index.html', title='home', status=STATUS, lastscore=LASTSCORE)

@app.route('/start')
def start():
    if STATUS == 'Ready':
        threading.Thread(target=gameplay).start()
    return redirect(url_for('index'))
    

@app.route('/changestatus')
def change_status():
    global STATUS
    STATUS = 'NOT READY'
    return redirect(url_for('index'))

@app.route('/recentscores')
def recent_scores():
    scores = get_recent_scores(os.path.join(app.static_folder, json_name), 10)
    return render_template('scores.html', title='Recent Scores', rows=scores)

@app.route('/highscores')
def high_scores():
    scores = get_high_scores(os.path.join(app.static_folder, json_name), 10)
    return render_template('scores.html', title='High Scores', rows=scores)

@app.route('/allscores')
def all_scores():
    scores = read_scores(os.path.join(app.static_folder, json_name))
    return render_template('scores.html', title='All Scores', rows=scores)

# update status every 5 seconds
def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('status.html', status=STATUS, lastscore=LASTSCORE), 'status'))

# manually update status
def update_status():
    with app.app_context():
        turbo.push(turbo.replace(render_template('status.html', status=STATUS, lastscore=LASTSCORE), 'status'))

def gameplay():
    global STATUS, LASTSCORE, ARDUINO, LED
    STATUS = "Busy"
    update_status()
    LASTSCORE = play(ARDUINO, LED)
    STATUS = "Ready"
    update_status()
    return

def main():
    # setup
    if not os.path.exists(os.path.join(app.static_folder, json_name)):
        # create an empty json file
        with open(os.path.join(app.static_folder, json_name), 'w') as f:
            f.write('{}')
    
    global ARDUINO, LED
    ARDUINO = ArduinoClass()
    LED = LEDClass()

    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
