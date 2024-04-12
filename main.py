import json
import anthropic

print("Start")

openai_keys = json.load(open('C:\\shared\\content\\config\\api-keys\\claude.json'))
my_openai_key = openai_keys['team-12']

print(my_openai_key)

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ]
)

print(message.content.text)