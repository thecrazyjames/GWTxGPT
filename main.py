import json
import anthropic
import base64
import httpx

print("Start")

claude_keys = json.load(open('C:\\shared\\content\\config\\api-keys\\claude.json'))
my_claude_key = claude_keys['team-14']

print("TO GENERATE A USER STORY AND GHERKIN FILES PLEASE PROVIDE A GIVEN WHEN THEN SCENARIO")


given = input("GIVEN: ")
when = input("WHEN: ")
then = input("THEN: ")

prompt = f"GIVEN: {given}. WHEN: {when}. THEN: {then}"

client = anthropic.Anthropic(
    
    api_key=my_claude_key,
)


# ********************Use this code if you need to consume an image ***************************

# image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDQLAycA7Nszy0mmlgw_EfN1YHHrvDUILzXHsIrWUkDw&s"
# image_media_type = "image/png"
# image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")



# message3 = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0.0,
#     system="Respond",
#     messages=[
#         {"role": "user", "content": 
#          [
#              {
#                  "type": "image",
#                  "source": {
#                      "type": "base64",
#                      "media_type": "image/png",
#                      "data": image_data
#                  }
#              },
#              {"type": "text", "text": f"The image is a Gherkin feature file.  Can you create given when thens in the format of the image provided using the following scenario: {prompt}?"}
#          ]}
#     ]
# )

feature_file = open('feature_file_template.txt', 'r').read()

message3 = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond",
    messages=[
        {"role": "user", "content": 
         [
             {
                 "type": "text",
                 "text": feature_file
             },
             {"type": "text", "text": f"Can you generate a feature file with as many scenarios as described based on the given when thens using the following scenario: {prompt}?"}
         ]}
    ]
)

user_story = open('user_story_complex.txt', 'r').read()


message4 = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond",
    messages=[
        {"role": "user", "content": 
         [
             {
                 "type": "text",
                 "text": user_story
             },
             {"type": "text", "text": f"Using the user story text included in this prompt and the following feature file details: {message3.content[0].text}. Can you create a fully detailed user story?"}
         ]}
    ]
)

print(message3.content)
with open("GWTxGPT.feature", "w") as file:
     file.write(message3.content[0].text)

print(message4.content)
with open("SampleUserStory.txt", "w") as file:
     file.write(message4.content[0].text)