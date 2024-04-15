import json
import anthropic

print("Start")

claude_keys = json.load(open('C:\\shared\\content\\config\\api-keys\\claude.json'))
my_claude_key = claude_keys['team-14']

print(my_claude_key)
print(type(my_claude_key))


given = input("Enter a GIVEN Statement for a GIVEN WHEN THEN scenario")
when = input("Enter a WHEN Statement for a GIVEN WHEN THEN scenario")
then = input("Enter a THEN Statement for a GIVEN WHEN THEN scenario")

prompt = f"GIVEN: {given}. WHEN: {when}. THEN: {then}"

client = anthropic.Anthropic(
    
    api_key=my_claude_key,
)

message1 = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond with well defined gherkin files and a standardized user story for a software feature. The output should be a formatted html file that I can paste into another file.",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# message2 = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0.0,
#     system="Respond with well defined gherkin files and a standardized user story for a software feature. The o",
#     messages=[
#         {"role": "user", "content": prompt}
#     ]
# )



print(message1.content)