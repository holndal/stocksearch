import requests
def discord_post(txt,hookurl):
    requests.post(hookurl, {"content":txt})
if __name__ == "__main__":
    discord_post("HELLO WORLD", "https://discord.com/api/webhooks/******/******")
