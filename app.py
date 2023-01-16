from flask import Flask
from flask import send_file
import subprocess
import asyncio

app = Flask(__name__)

@app.route("/<path:url>")
def hello_world(url):
    if url.startswith("http"):
        file_name = url.split(":")[1][2:]
    else:
        file_name = url
    file_name = file_name.replace("/", "_")
    subprocess.run(["youtube-dl", "-o", f"{file_name}.mp4", url])
    #return f"{url}"
    return send_file(f"{file_name}.mp4")