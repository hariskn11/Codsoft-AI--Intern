import json
import random

# Load the intents file
def load_intents(file_path):
    with open(file_path) as file:
        return json.load(file)

# Save the updated intents to the file
def save_intents(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to get a response from the chatbot
def get_response(message,data):
    for intent in data['intents']:
        if intent['tag']=='goodbye':
            if message in intent['patterns']:
                print(random.choice(intent['responses']))
                return None
        elif message in intent['patterns']:
            return random.choice(intent['responses'])
    return 0

# Add a new pattern to an existing tag
def add_pattern_to_json(new_pattern, tag, data, file_path):
    for intent in data['intents']:
        if intent['tag'] == tag:
            intent['patterns'].append(new_pattern)
            save_intents(data, file_path)
            return f"I've added '{new_pattern}' to the '{tag}' tag."
    return "Tag not found."

# Create a new tag with patterns and responses
def create_new_tag(tag, patterns, responses, data, file_path):
    new_intent = {
        "tag": tag,
        "patterns": patterns,
        "responses": responses
    }
    data['intents'].append(new_intent)
    save_intents(data, file_path)
    return f"New tag '{tag}' created with patterns and responses."

# Example usage
def chatbot_interaction(file_path):
    data=load_intents(file_path)
    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input,data)
        if response is None:
            break
        elif response==0:
            tags = [intent['tag'] for intent in data['intents']]
            print(f"I don't understand what you are saying.\nAvailable tags: {tags}")
            new_tag = input("Under which tag should I categorize this? ").lower()
            if new_tag not in tags:
                patterns = [user_input]
                responses = [input("What should be the response? ").lower()]
                print(create_new_tag(new_tag, patterns, responses, data, file_path))
            else:
                print(add_pattern_to_json(user_input,new_tag,data,file_path))
        else:
            print("Chatbot:", response)

# Example usage
if __name__ == "__main__":
    chatbot_interaction('D:\\codesoft\\st.json')
