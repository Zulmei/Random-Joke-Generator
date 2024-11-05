import requests

# Adding a comment for a change

url = "https://official-joke-api.appspot.com/random_joke" 

def fetch_joke():
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data["setup"], joke_data["punchline"]
    else:
        print("Error:", response.status_code)
        return None, None

def write_joke_data_to_file(setup, punchline):
    with open("jokes.txt", 'w') as f:
        f.write(f"Joke: {setup}\nPunchline: {punchline}")

setup, punchline = fetch_joke()
if setup and punchline:
    print(f"Joke: {setup}\nPunchline: {punchline}")
    write_joke_data_to_file(setup, punchline)

