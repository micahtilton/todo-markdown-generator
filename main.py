from datetime import datetime
import json

def loadTemplate(filepath):
    with open("./template.json", "r") as f:
        return json.load(f)

def templateToTodo(template: dict):
    today = datetime.now()
    todayDay = today.weekday()
    daysOfTheWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    dayWord = daysOfTheWeek[todayDay]
    
    ret = {
        "day": dayWord,
        "date": today.strftime("%m-%d-%y"),
        "today": [],
        "upcoming": []
    }
    
    if "daily" in template:
        ret["today"] += template["daily"]
    
    if "weekday" in template:
        ret["today"] += template["weekday"]
    
    if "weekend" in template:
        ret["today"] += template["weekend"]
    
    if dayWord in template:
        ret["today"] += template[dayWord]
    
    # add upcoming tasks
    
    return ret 

def generateMarkdown(todo, fp):
    markdownText = ""
    markdownText += f"# {todo['date']}\n"
    
    markdownText += f"## Today\n"
    if len(todo["today"]) == 0:
        markdownText += "nothing to do today!  \n"   
    else:
        for task in todo["today"]:
            markdownText += f"- [ ] {task}\n"
    
    markdownText += f"## Upcoming\n"
    if len(todo["upcoming"]) == 0:
        markdownText += "nothing to do soon!  \n"
    for task in todo["upcoming"]:
        markdownText += f"- [ ] {task}\n"
    
    
    with open(fp, "w+") as f:
        f.write(markdownText)
    
template = loadTemplate("./template.json")
todo = templateToTodo(template)
generateMarkdown(todo, f"./todo/{todo['date']}.md")