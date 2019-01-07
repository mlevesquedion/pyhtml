from flask import Flask

from dsl import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return \
        html(
            head(
                title(
                    "HTML DSL in Python"
                ),
                meta(
                    name="description",
                    content="a simple html dsl"
                )
            ),
            body(
                h1("Welcome to my website", style="color:red;"),
                h2("Here are a few items from my todo list: "),
                ul(
                    li("Item one"),
                    li("Item two"),
                    li("Item three")
                )
            )
        )
