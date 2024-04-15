import json
import anthropic
import base64
import httpx

print("Start")

claude_keys = json.load(open('C:\\shared\\content\\config\\api-keys\\claude.json'))
my_claude_key = claude_keys['team-14']

print(my_claude_key)
print(type(my_claude_key))


# given = input("Enter a GIVEN Statement for a GIVEN WHEN THEN scenario: ")
# when = input("Enter a WHEN Statement for a GIVEN WHEN THEN scenario: ")
# then = input("Enter a THEN Statement for a GIVEN WHEN THEN scenario: ")

# prompt = f"GIVEN: {given}. WHEN: {when}. THEN: {then}"

client = anthropic.Anthropic(
    
    api_key=my_claude_key,
)

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDQLAycA7Nszy0mmlgw_EfN1YHHrvDUILzXHsIrWUkDw&s"
image_media_type = "image/png"
image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")

# message1 = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0.0,
#     system="Respond with well defined gherkin files and a standardized user story for a software feature. The output should be a formatted html file that I can paste into another file.",
#     messages=[
#         {"role": "user", "content": prompt}
#     ]
# )

message3 = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond",
    messages=[
        {"role": "user", "content": 
         [
             {
                 "type": "image",
                 "source": {
                     "type": "base64",
                     "media_type": "image/png",
                     "data": image_data
                 }
             },
             {"type": "text", "text": "The image is a Gherkin feature file.  Can you create given when thens for a food delivery scenario in the format of the image provided?"}
         ]}
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



print(message3.content)
with open("GWTxGPT.feature", "w") as file:
     file.write(message3.content[0].text)