import os
from groq import Groq
from dotenv import load_dotenv
from memory import retrieve_memory

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(user_input):
    # Retrieve past memory
    past = retrieve_memory(user_input)

    messages = [
        {
            "role": "system",
            "content": "You are a very basic customer support assistant. Give short, generic replies."
        }
    ]

    # If bad past exists → force improvement
    if past and past.get("feedback") == "bad":
        messages.append({
            "role": "system",
            "content": f"""
You previously gave a BAD response to a similar query.

Bad response:
{past.get('response', '')}

This response was too generic and unhelpful.

RULES for improvement:
- Do NOT apologize
- Do NOT give generic replies
- Provide step-by-step actionable solution
- Be specific and helpful

Now give a completely improved response.
"""
        })

    # Add user input
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content