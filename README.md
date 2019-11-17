# simple-cli-with-python-3
to run the program on unix based os, you need Python 3.x and pip installed and the you can execute it through below:

[root@localhost tmp]# python3.6 cli.py --help
Usage: cli.py [OPTIONS]

  This application prints the numbers from 1 to 10 in random order to the
  terminal

Options:
  --count INTEGER  number of times
  --help           Show this message and exit.




[root@localhost tmp]# python3.6 cli.py --count 5
[6, 7, 2, 4, 8, 1, 9, 10, 3, 5]
[8, 9, 10, 1, 3, 4, 7, 2, 5, 6]
[4, 5, 3, 7, 6, 2, 1, 8, 9, 10]
[9, 2, 6, 7, 5, 10, 3, 1, 4, 8]
[7, 8, 9, 3, 5, 2, 10, 1, 4, 6]

  
