from functools import partial


def spread_attributes(attributes):
    prefix = ' ' if attributes else ''
    return prefix + ' '.join(f'{k}={repr(v)}' for k, v in attributes.items())


def tag(_name, *children, **attributes):
    return f'<{_name}{spread_attributes(attributes)}>{"".join(children)}</{_name}>'


html = partial(tag, 'html')
head = partial(tag, 'head')
title = partial(tag, 'title')
meta = partial(tag, 'meta')
body = partial(tag, 'body')
h1 = partial(tag, 'h1')
ul = partial(tag, 'ul')
li = partial(tag, 'li')

if __name__ == '__main__':
    result = html(
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
            h1("A few things I like", style="color:red;"),
            ul(
                li("Item one"),
                li("Item two"),
                li("Item three")
            )
        )
    )
    with open('index.html', 'w') as file:
        file.write(result)
