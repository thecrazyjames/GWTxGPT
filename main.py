import json
import anthropic

print("Start")

claude_keys = json.load(open('C:\\shared\\content\\config\\api-keys\\claude.json'))
my_claude_key = claude_keys['team-14']

print(my_claude_key)
print(type(my_claude_key))

client = anthropic.Anthropic(
    
    api_key=my_claude_key,
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "Write a short blog post about the developer?"}
    ]
)

print(message)