# python-rps

Rock, paper, scissors CLI game in Python

## Description

We are building the project as part of learning Python 3.

## Getting Started

### Dependencies

* [Python 3](https://www.python.org/)
* psycopg2:
    ```
    pip install psycopg2
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

![alt text](resources/images/welcome.png "Welcome to Super Ultimate Battle Rock Paper Scissors!")
![alt text](resources/images/play1.png "User plays rock but then lose to COM's paper")
![alt text](resources/images/play2.png "COM's rock beats player's scissor!")
![alt text](resources/images/result.png "It's another WIN for COM!")

## Authors

* [Jaco Roux](https://github.com/pjjroux)
* [Quartus Kok](https://github.com/qkok)

## Features

* Working Rock, paper, scissor game played over a match consisting of three rounds with ASCII art displayed after each play. (WIP)
* Match outcomes logged in a database to build up historic data.

## Goals
* COM moves decided by using the historic data.
