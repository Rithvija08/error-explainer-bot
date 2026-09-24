import ollama

#get name from input
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
 
while True:
    data = input("Enter your error message or exit to stop : ")
    if not data:
        print("enter an error: ")
    elif data.lower() == "exit":
        break
    elif data.lower() == "help":
        print("if you enter any error message i'll resolve it if you enter exit i'll stop")
    else:
        try:
            response = ollama.chat(model="llama3.2",
            messages=[
            {
               "role": "system",
               "content":SYSTEM
            },         
            {
               "role": "user",
               "content":data
            }  
       ])
            print(response.message.content)
        except Exception as e:
            print(f"could not reach the model: {e}")

