# Simple Recommendation System

This Flask web app recommends questions based on the user's role, experience level, tags, and category. The questions are loaded from a JSON file and filtered based on the user's input.

## Tech Stack

This script uses Python 3 and its inbuilt `json` model and `flask` for basic frontend

## Recommendation System

The script then filters the loaded questions based on the user's input. The filtering is done using list comprehension and includes the following checks:

- Role: The script checks if the user's role is in the roles associated with the question.
- Experience Level: The `experience_level_filter` function checks if the user's experience level is equal to or higher than the question's level. This is based on the assumption that an expert can prepare beginner questions too.
- Tags: The `tag_filter` function checks if at least one of the question's tags are common with the user's tags.
- Category: If the user has specified a category, the script checks if the question's category matches the user's category.

Finally, the script prints the recommended questions, along with their answer, difficulty level, and category. Each question is numbered for easy reference.

## User Filter

The filter pane will allow you to modify the following:

- Role: The role for which you want to recommend questions (e.g., "Software Developer").
- Experience Level: Your experience level ("Beginner", "Intermediate", "Expert").
- Tags( Optional): The tags related to the questions you want to recommend (e.g., "Python", "Algorithms"). Enter multiple tags separated by commas.
- Category (Optional): The category of the questions (e.g., "Data Structures").
  
NOTE: If you don't want to filter by category or tags, just hit enter.

## Questions JSON Format

The questions are stored in a JSON file in the following format:

```
{
    "question": "QUESTION",
    "answer": "ANSWER",
    "difficulty_level": "Easy/Medium/Advanced",
    "tags": ["TAG1", "TAG2"...],
    "roles": ["ROLE1", "ROLE2"...],
    "experience_level": "Beginner/Intermediate/Expert",
    "category": "CATEGORY",
    "sub_category": "SUB CATEGORY"
}
```

## How to Run

1. Ensure you have Python and Flask installed on your system.
2. Run the script using the command: `python main.py`

## Output

The webapp will print the recommended questions, along with their answer, difficulty level, and category. Each question is numbered for easy reference.
