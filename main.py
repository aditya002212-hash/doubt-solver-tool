import json                    
import datetime as dt 
import google.generativeai as genai 
import os

# memory 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

profile = os.path.join(DATA_DIR, "profile.json")
history = os.path.join(DATA_DIR, "history.json")


def load_file(file):
    try:
        with open(file, 'r') as f:
            data=json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def show_history(file):
    data=load_file(file)
    return data
def add_profile(file,name,currentclass,targetexam,weaksubject):
    data=load_file(file)
    data.append({'name':name,'currentclass':currentclass,'targetexam':targetexam,'weaksubject':weaksubject})
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
def add_history(file,query,response):
    data=load_file(file)
    timestamp=dt.datetime.now().isoformat()
    data.append({'timestamp':timestamp,'query':query,'response':response})
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# main function 
def doubt_solver():
    genai.configure(api_key='AIzaSyB2cQEOG9KKI_hGG4OkvR1VpKcjkKHJwS4')
    model=genai.GenerativeModel('gemini-2.5-flash')
    while True:
        user_input=input('''
                         
                        1. addprofile 
                        2. askdoubt 
                        3. viewhistory
                        4. exit
                         choose an option by writitng their number like 1 to askdoubt
                         ''')
        if user_input in ['4','exit']:
            break 
        elif user_input in ['1','addprofile']:
            name=input("Enter name: ")
            current_class=input("Enter current class if you are dropper add 13 or write dropper: ")
            target_exam=input("Enter target exam only jee and neet: ")
            weak_subject=input("Enter weak subject: ")
            add_profile(profile, name, current_class, target_exam, weak_subject)
        elif user_input in ['2','askdoubt']:
            subject=input("Enter the subject of your doubt: ")
            query=input("Enter your doubt: ")
            prompt=f'''Role Kota teacher who taught top rankers in subject :{subject}
                    Act as a personalized study assistant for a student 
                    task on the basis of the profile help student to solve their doubt: {query} 
                    in case you do not find profile information relevant to the doubt, provide a general answer
                    Note - be concise and straight forward in your answers do not add noise 
                    output format is dtudent asked a question about a topic
                    key points :
                    diagram or image related to the topic if needed :
                    summary :
                    exam tips related to the topic :
                    topic weightage in jee and neet :
                    output format if student solves a question and having doubt or getting wrong anser or can not able to solve 
                    student mistakes and how to avoid them :
                    step by step solution of the question :
                    if student can not able to solve the question then give them a detailed solution with explanation of each step and provide how to think in that approch: 
                    after explaining  add a good luck message and motivate them '''
            response=model.generate_content(prompt)
            print(' hello student, here is the answer to your doubt: ')
            print(response.text)
            add_history(history, query, response.text)
            user_input=input('want follow up on this doubt? yes /no')
            if user_input.lower()=='no':
              break
            while True:
                follow_input=input('''
                                   
                                1. give another example
                                2. make it in hinglish
                                3. give short revision note
                                4. give one related practice question
                                5. no follow up (type no or exit or 5 to end)
                                6. custom follow up (type your custom follow up question or instruction related to the doubt
                                  to get output just enter the number like 1 ,2 ,3 ''')
                if follow_input in ['5','no','exit']:
                    continue
                elif follow_input in ['1','give another example']:
                    prompt=f'''analyse the previous discussion above {response} on the based on this give an another example of it  '''
                    response=model.generate_content(prompt)
                    print(response.text)
                elif follow_input=='2':
                    prompt=f'''analyse the previous discussion above {response} on the based on this make it in hinglish  '''
                    response=model.generate_content(prompt)
                    print(response.text)
                elif follow_input == '3':
                    prompt=f'''analyse the previous discussion above {response} on the based on this give short revision note of the topic that is in the conversation  '''
                    response=model.generate_content(prompt)
                    print(response.text)
                elif follow_input == '4':
                    prompt=f'''analyse the previous discussion above {response} on the based on this give one related practice question of the topic that is in the conversation  '''
                    response=model.generate_content(prompt)
                    print(response.text)
                elif follow_input == '6':
                    custom_follow=input("Enter your custom follow up question or instruction related to the doubt: ")
                    prompt=f'''analyse the previous discussion above {response} on the based on this {custom_follow} '''
                    response=model.generate_content(prompt)
                    print(response.text)
                
        elif user_input in ['3','viewhistory']:
            data=show_history(history)
            for item in data:
                print(f"Timestamp: {item['timestamp']}")
                print(f"Query: {item['query']}")
                print(f"Response: {item['response']}")
                print('-----------------------------')
if __name__ == "__main__":
    doubt_solver()

