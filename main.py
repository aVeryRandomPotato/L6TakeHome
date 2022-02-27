from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "hu90bv2yb0824y0BYUG0h9EGWH&igfRG&2h-GRW&5*Hg08yWRhy80GRWhy80RGWhwqaety80"

if __name__ == "__main__":
    app.run(host="localhost", port="8693")
