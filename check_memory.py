from memory import search_memory

result = search_memory(
    "What do you know about me?"
)

for item in result:
    print(item)