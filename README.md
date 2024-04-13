<div align="center">

<h1>Math Brain Games</h1>

<p>Five CLI math brain games</p>

[![Actions Status](https://github.com/vitalychasovskih/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vitalychasovskih/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1939e982167320ac0042/maintainability)](https://codeclimate.com/github/vitalychasovskih/python-project-49/maintainability)
</div>

## About

This is my first python project on Hexlet.

"**Math Brain Games**" is a set of five console games. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and prompt you to play it again.

### Games:

* [X] **_Brain Even_**: Determining an even number.
* [X] **_Brain Calc_**: Arithmetic expressions to be calculated.
* [X] **_Brain GCD_**: Determining the largest common divisor.
* [X] **_Brain Progression_**: Finding missing numbers in a sequence of numbers.
* [X] **_Brain Prime_**: Determining a prime number.

#### Example:

```bash
>> brain-progression

Welcome to the Brain Game!
May I have your name? Jon Snow # The user enters the answer
What number is missing in this progression?
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # The user enters the answer
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # The user enters the answer
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # The user enters the answer
Correct!
Congratulations, Jon Snow!
```

### Built With

* Python
* Poetry
* flake8

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.10 or higher installed:

```bash
>> python --version
Python 3.10.0+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/vitalychasovskih/python-project-49
```

Then you have to build the package and install it:

```bash
>> cd python-project-49
```

```bash
>> make build
>> make package-install
```

---

## Usage

### _Brain Even_

A random number is shown to the user. And he needs to answer `yes` if the number is even, or `no` if it is odd.

```bash
>> brain-even

Answer "yes" if the number is even, otherwise answer "no".
Question: 98
Your answer: no
'no' is wrong answer ;(. Correct answer was 'yes'.
```

```bash
>> brain-even

Answer "yes" if the number is even, otherwise answer "no".
Question: 82
Your answer: yes
Correct!
```

<a href="https://asciinema.org/a/650933" target="_blank"><img src="https://asciinema.org/a/650933.svg" width="300"/></a>

### _Brain Calc_

The user is shown a random mathematical expression, for example `25 + 17` which needs to be calculated and written down the correct answer.

```bash
>> brain-calc

What is the result of the expression?
Question: 3 + 15
Your answer: 315
'315' is wrong answer ;(. Correct answer was '18'.
```

```bash
>> brain-calc

What is the result of the expression?
Question: 5 * 15
Your answer: 75
Correct!
```

<a href="https://asciinema.org/a/650934" target="_blank"><img src="https://asciinema.org/a/650934.svg" width="300"/></a>

### _Brain GCD_

The user is shown two random numbers, for example, `25 50`. The user must calculate and enter the greatest common divisor of these numbers.

```bash
>> brain-gcd

Find the greatest common divisor of given numbers.
Question: 95 96
Your answer: 5
'5' is wrong answer ;(. Correct answer was '1'.
```

```bash
>> brain-gcd

Find the greatest common divisor of given numbers.
Question: 56 91
Your answer: 7
Correct!
```

<a href="https://asciinema.org/a/650935" target="_blank"><img src="https://asciinema.org/a/650935.svg" width="300"/></a>

### _Brain Progression_

A series of numbers that form an arithmetic progression is shown to the player, replacing any of the numbers with two dots. The player must enter this number.

```bash
>> brain-progression

What number is missing in the progression?
Question: 13 22 31 40 49 58 67 76 85 .. 103
Your answer: 100
'100' is wrong answer ;(. Correct answer was '94'.
```

```bash
>> brain-progression

What number is missing in the progression?
Question: 11 16 .. 26 31 36 41 46
Your answer: 21
Correct!
```

<a href="https://asciinema.org/a/650937" target="_blank"><img src="https://asciinema.org/a/650937.svg" width="300"/></a>

### _Brain Prime_

A random number is shown to the user. He needs to answer `yes` if the number is prime, or `no` if it is not.

```bash
>> brain-prime

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 66
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
```

```bash
>> brain-prime

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 22
Your answer: no
Correct!
```

<a href="https://asciinema.org/a/650938" target="_blank"><img src="https://asciinema.org/a/650938.svg" width="300" /></a>

---

## Additionally

### Dependencies

* python = "^3.10"

### Dev Dependencies

* flake8 = "^7.0.0"

---

This is the first training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@Vitaly Сhasovskih](https://github.com/vitalychasovskih)