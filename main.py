from flask import Flask, request, render_template
from util.json_handler import *
from util.log import logger
from util.getFilterOpts import difficulty_levels, experience_levels, categories, roles

app = Flask(__name__)


def get_input(prompt, split=False):
    data = input(prompt)
    return data.split(',') if split and data else data

def experience_level_filter(question_level, candidate_level):
    # Experts can prepare Beginner questions too
    levels = ['Beginner', 'Intermediate', 'Expert']
    return levels.index(question_level) <= levels.index(candidate_level)

def tag_filter(question_tags, candidate_tags):  
    common_tags = set(question_tags) & set(candidate_tags)
    return len(common_tags) >= 1

@app.route('/', methods=['GET', 'POST'])
def recommend_questions():
    candidate_attributes = {
        'role': '',
        'experience_level': '',
        'tags': '',
        'category': ''
    }

    if request.method == 'POST':
        # Get candidate attributes from form data
        candidate_attributes = {
            'role': request.form.get('role'),
            'experience_level': request.form.get('experience_level'),
            'tags': request.form.get('tags'),
            'category': request.form.get('category')
        }
        print(candidate_attributes['tags'].split(','))

        # Load questions from JSON file
        questions = read_json('questions.json')

        # Filter questions based on candidate attributes
        filtered_questions = [q for q in questions if 
            (not candidate_attributes['role'] or candidate_attributes['role'] in q['roles']) and 
            (not candidate_attributes['experience_level'] or experience_level_filter(q['experience_level'], candidate_attributes['experience_level'])) and
            (not candidate_attributes['tags'] or tag_filter(q['tags'], candidate_attributes['tags'].split(','))) and
            (not candidate_attributes['category'] or q['category'] == candidate_attributes['category'])]

        # Save the filtered questions
        save_json(format_questions(filtered_questions), 'filtered_questions.json')

        return render_template('index.html', questions=filtered_questions, roles=roles, experience_levels=experience_levels, categories=categories, candidate_attributes=candidate_attributes)

    # Load all questions for 'GET' method
    questions = read_json('questions.json')
    return render_template('index.html', questions=questions, roles=roles, experience_levels=experience_levels, categories=categories, candidate_attributes=candidate_attributes)
if __name__ == '__main__':
    app.run(debug=True)