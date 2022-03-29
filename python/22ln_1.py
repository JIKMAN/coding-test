import re

logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]

def solution(logs):
    
    format = "^team_name : [a-zA-Z]+ application_name : [a-zA-Z]+ error_level : [a-zA-Z]+ message : [a-zA-Z]+$"
    p = re.compile(format)

    result = 0
    for log in logs:
        print(len(log))
        m = p.findall(log)
        print(m)
        if len(m) == 0:
            result += 1

    return result

print(solution(logs))