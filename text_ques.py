import openai

openai.api_key="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"


text="Codex understands dozens of different programming languages. Many share similar conventions for comments, functions and other programming syntax. By specifying the language and what version in a comment, Codex is better able to provide a completion for what you want. That said, Codex is fairly flexible with style and syntax."
prompt="Generate 5 questions from the given tex '"+ text +"'"
response= openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=1000)

print(response)