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
# Function: Write the prompt
# ======================================

def getGPTPrompt2(layer1_output, jobProfile_environment):
    prompt_layer2 =f'''Context:
Actions - Parameters
Ping target: ipAddress, pingInterval, pingEchoNum, pingTimeout
Use browser to open URL: url,watchInterval
Open Word document: filePath, openInterval
Run one command: cmdID,console, cmdStr, repeat, interval
Clone repo: dirPath, repoName, reporURL
Hold Zoom meeting: username, meetingURL
Take screenshot of website: url, outputFolder, driverMode
Send Telegram: token, chatID, message
Send email: username, appPassword, recipients, subject, message

Layer 1 Output:
{layer1_output}

Environment details:
{jobProfile_environment}.

Task:
For each task listed under Layer 1 Output, generate a time-stamped schedule of actions, from the list provided under Context, needed to complete the task.
If no actions can complete the task, drop the task and indicate it with [task dropped].

The software engineer's details are listed under environment details.
Please include the relevant parameter values when necessary. You do not need to include all the values for each parameter.
For parameters whose values are not included in the text file, please generate relevant and working values. If they refer to the software engineer's personal details not listed in the text file, please put [placeholder].


Format:
Please generate in the following format:
Time,Action,Description,Parameter1,Value1,Parameter2,Value2,Parameter3,Value3,Parameter4,Value4,Parameter5,Value5
09:00,Use browser to open URL,Watch YouTube,url,"https://www.youtube.com/watch?v=NQ1cvwEvh44",watchInterval,10,,,,
10:00,Run one command,Ping google.com,cmdID,"pingGoogle",console,True,cmdStr,"ping -n 5 www.google.com.sg",repeat,1,interval,0.8
11:00,Open Word document,Key in results of command,fileName,"placeholder.docx",openInterval,10,,,,
13:30,Ping target,Ping www.singtel.com.sg,ipAddress,"www.singtel.com.sg",pingInterval,0.1,pingEcho,5,pingTimeout,1
'''
    return prompt_layer2
