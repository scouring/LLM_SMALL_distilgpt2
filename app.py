from model import generate_response

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break
    response = generate_response(prompt)
    print("Bot:", response)
