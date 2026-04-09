from agent import get_response
from memory import store_memory

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    # Get response
    response = get_response(user_input)
    print("Agent:", response)

    # Normal feedback (manual)
    feedback = input("Was this response good or bad? (good/bad): ").lower()

    # Safety check (avoid wrong input)
    if feedback not in ["good", "bad"]:
        print("Invalid input. Defaulting to 'bad'")
        feedback = "bad"

    # Store memory
    store_memory(user_input, response, feedback)