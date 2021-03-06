# python-rps

Rock, paper, scissors CLI game in Python

## Description

We are building the project as part of learning Python 3.

## Getting Started

### Dependencies

* [Python 3](https://www.python.org/)
* mysql-connector:
    ```
    pip install mysql-connector
    ```
* requests:
    ```
    pip install requests
    ```

### Installing

* Clone or download the project files to your local machine. 

### Executing program

* Run main.py
```
Commands
> R or ROCK
> P or PAPER
> S or SCISSOR
> X or EXIT
```

![alt text](https://github.com/pjjroux/python-rps/blob/master/resources/images/welcome.PNG "Welcome to Super Ultimate Battle Rock Paper Scissors!")
![alt text](https://github.com/pjjroux/python-rps/blob/master/resources/images/play1.PNG "User plays rock but then lose to COM's paper")
![alt text](https://github.com/pjjroux/python-rps/blob/master/resources/images/play2.PNG "COM's rock beats player's scissor!")
![alt text](https://github.com/pjjroux/python-rps/blob/master/resources/images/result.PNG "It's another WIN for COM!")

## Authors

* [Jaco Roux](https://github.com/pjjroux)
* [Quartus Kok](https://github.com/qkok)

## Features

* Working Rock, paper, scissor game with ASCII art displayed after each play.
* Match outcomes logged in a database using a PHP API to build up historic data.
* COM moves decided by using the historic data after 10 rounds against the same player.
