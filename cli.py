import random 
import click
@click.command()
@click.option('--count', default=1, help='number of times')
def Random(count):
    """ This application prints the numbers from 1 to 10 in random order to the terminal """
    for x in range(count):
        r = random.sample(range(1, 11), k=10)
        print(r)
if __name__ == '__main__':
    Random()        
