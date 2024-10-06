import os
import openai
import random
from dotenv import load_dotenv

load_dotenv(r'Scripts\api_key.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

# ======================================
# Function: ChatGPT
# ======================================

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",  # Update the model to the current version
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )

    response_content = response.choices[0].message.content #.strip("```")
    return response_content

# ======================================
# Function: To get 5 random task examples to include in prompt.
# ======================================

def getRandomTaskExamples(file_path, numExamples):
    allTasksExamples = []
    with open(file_path, 'r') as file:
        for line in file:
            if '. ' in line:
                allTasksExamples.append(line.split('. ')[1].replace('\n', ''))
    return random.sample(allTasksExamples, numExamples)

# ======================================
# Function: For prompt to read past outputs.
# ======================================

def readPastGPTOutputs(folder_path):
    pastOutputs = []
    for filename in os.listdir(folder_path):
        # Check if the file is a text file (ends with .txt)
        if filename.endswith(".txt"):
            # Build the full file path
            file_path = os.path.join(folder_path, filename)
            # print(f'Reading file: {file_path}')
            
            # Open and read the file
            with open(file_path, 'r') as file:
                # Read the contents and append to the list
                pastOutputs.append(file.read())
    return pastOutputs

# ======================================
# Function: Write the prompt
# ======================================

def getGPTPrompt(jobProfile, pastOutputs, jobProfile_taskExamples):
    prompt_layer1 =f'''Persona:
You are an agent which generates a daily time-stamped sequence of actions for a {jobProfile}.

Task:
Generate a new series of tasks (different from {pastOutputs}) that a {jobProfile} can complete in a day from 9am to 5pm.
The timing for this schedule need not be the same as the previous schedules.
The timing for each task should not follow the standard rounding to the nearest 5th or 10th minute (e.g., 9:00 AM, 9:10 AM). Instead, use more natural and varied timings like 9:07 AM, 9:18 AM, etc., while ensuring the schedule remains realistic and coherent. 

Examples of task: {", ".join(jobProfile_taskExamples)}

Include non-work related activities like scrolling social media, sending a telegram chat to a friend, taking a walk, taking a coffee break etc.

Format:
Please output a format that is easy to copy and paste into a text file.'''
    return prompt_layer1