import json
from util.log import logger

# Load the data from the JSON file
with open('questions.json') as f:
    data = json.load(f)

# Initialize empty sets for each category
difficulty_levels = set()
experience_levels = set()
categories = set()
roles = set()

# Iterate over each item in the data
for item in data:
    # Check if the required fields exist in the item
    if 'difficulty_level' in item:
        difficulty_levels.add(item['difficulty_level'])
    if 'experience_level' in item:
        experience_levels.add(item['experience_level'])
    if 'category' in item:
        categories.add(item['category'])
    if 'roles' in item:
        # Roles is a list, so we need to add each role individually
        for role in item['roles']:
            roles.add(role)

# Log the sets
logger.info('Difficulty Levels: %s', list(difficulty_levels))
logger.info('Experience Levels: %s', list(experience_levels))
logger.info('Categories: %s', list(categories))
logger.info('Roles: %s', list(roles))