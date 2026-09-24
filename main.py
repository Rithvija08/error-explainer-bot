import ollama


name =input("Enter your name: ")

branch = input("Enter your branch: ")
#print message - eg:Hi Rithvija from CSE
print(f"Hi {name} from {branch}")

SYSTEM = '''
You explain programming error messages to a 2nd year egineering student.Reply in 3 parts.
1) What it means in plain English.
2) the likely cause
3) how to fix 
Keep it under 120 words.
'''
 
response = ollama.chat(model="llama3.2",messages=[
    {
        "role": "system",
        "content":SYSTEM
    },
    {
        "role": "user",
        "content":"Python error NameError: name 'x' is not defined"
    }
])
print(response.message.content)
