memory = []

def store_memory(query, response, feedback):
    memory.append({
        "query": query,
        "response": response,
        "feedback": feedback,
        "lesson": f"For '{query}', give a clearer and more helpful response instead of a generic one."
    })


def retrieve_memory(query):
    for item in reversed(memory):  # recent first
        if query.lower() in item["query"].lower():
            return item
    return None