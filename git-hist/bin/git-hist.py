#!/usr/bin/env python

#from PIL import Image
#def flag(c,w=100,h=100):
#	c1,c2,c3 = c.split()
#	img = Image.new("RGB", (w*3,h), c1)
#	lay1 = Image.new("RGB", (w,h), c2)
#	lay2 = Image.new("RGB", (w,h), c3)
#	img.paste(lay1,(w,0))
#	img.paste(lay2,(w*2,0))
#	img.show()

#flag("gold blue pink",200,350)


import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()


