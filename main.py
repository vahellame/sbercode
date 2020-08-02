import requests

r = requests.post("http://vahella.me:5000/recognition", json={
    "text": """
    мне почти 20, я не пью таблетки и прекрасно себя чувствую
        """
})

print(r.text)
