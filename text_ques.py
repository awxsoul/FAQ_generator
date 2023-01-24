import openai

openai.api_key="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"

content="Hormonal changes are also a major cause of why your hair may start thinning at a young age. Note that there are two phases of hair growth"

prompt="Generate 5 questions from the given text '"+ content +"'"
response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=1000)

# print(response["choices"][0]["text"])

#gets only the text from the output
questions=response["choices"][0]["text"]
print(response)
ques_list=questions.split("\n")
#to seperate the numbers


#remove numbering
for i in range(2,7):
    ques_list[i]=ques_list[i].split(".")[1]
for i in range(2,7):
    

    prompt= "Answer this question in one sentence,"+ques_list[i]
    response= openai.Completion.create(engine="text-davinci-001",prompt=prompt, max_tokens=100)
    answer=response["choices"][0]["text"]
    
    print("Q: ",ques_list[i])
    print("ans: ",answer,"\n")

    



