from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from .engine import Engine

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
engine = Engine('./data/student_courses_dataset.json')

@app.route("/")
def home():
    return "Hello!"

@app.route('/generate_model')
@cross_origin()
def generateModel():
    engine.generate_model()
    return "Okay...."

@app.route('/api/getrecommendation', methods=['POST'])
@cross_origin()
def recommend():
    params = request.form

    matric = params.get('matric_no')
    program = params.get('program')
    semester = params.get('semester')
    session = params.get('session')

    if len(params) < 1 or (not matric or not program or not semester or not session):
        abort(400)

    feature = f'{program} {semester} {session}'
    recommendations = engine.get_recommendations(feature)

    '''
    courses = []
    for row in recommendations.iterrows():
        courses.append({
            'courseCode': str(row['course_code']),
            'program': str(row['program']),
            'semester': int(row['semester']),
            'session': str(row['session']),
            'score': float(row['score'])
        })
    '''
    
    return jsonify(data = recommendations)