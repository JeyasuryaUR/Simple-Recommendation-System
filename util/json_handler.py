import json
from util.log import logger
import os


def read_json(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
        logger.info("Successfully read JSON file: %s", file_name)
        return data
    except Exception as e:
        logger.error("Error occurred while reading JSON file: %s", e)

def format_questions(data):
    try:
        formatted_data = [{'Question': q['question'], 'Answer': q['answer']} for q in data]
        return formatted_data
    except Exception as e:
        logger.error("Error occurred while formatting questions: %s", e)

def save_json(data, file_name):
    if not os.path.exists('filtered_data'):
        os.makedirs('filtered_data')
    file_name = "filtered_data/" + file_name
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info("Successfully saved JSON file: %s", file_name)
    except Exception as e:
        logger.error("Error occurred while saving JSON file: %s", e)
