# Press Start: Find Your Gamer Type
> "Answer a few questions and discover what kind of gamer you really are."

## Overview
> This program is a personality quiz that determins what type of gamer the user is based on their gaming >preferences and habits. The user will answer five multiple-choice questions about how they like to play video >games. Their answers will be used with conditional statements to determine their gamer type. At the end of the >quiz, the user will receive one of four results: Competitive Gamer, Explorer Gamer, Social Gamer, or Casual Gamer.

## Sample Questions and Responses
> 1. Do you enjoy competitive games?
> Yes
> No
> 2. Do you prefer playing video games with friends?
> Yes
> No
> 3. Do you enjoy exploring large game worlds?
> Yes
> No
> 4. Do you care more about winning than the story?
> Yes
> No
> 5. Do you play video games almost every day?
> Yes
> No


## Variables
> name (str): stores the user's name so the program can personally address the user.
> competitive (str): stores whether the user enjoys competitive games. It will contain either "yes" or "no".
> friends (str): stores whether the user prefers playing video games with friends. It will contain either "yes" or > "no".
> exploring (str): stores whether the user enjoys exploring large game worlds. It will contain either "yes" or "no".
> winning (str): stores whether the user cares more about winning than the story. It will contain either "yes" or "no".
> daily (str): stores whether the user plays video games almost every day. It will contain either "yes" or "no".
> gamer_type (str): stores the user's final gamer type after their answers have been evaluated. A single variable > works because the program will give the user one final result.



## Conditional Logic Outline
> Conditional statement 1 - related to "Do you enjoy competitive games?"
> if the response is "yes": show that the user enjoys competitive games.
> else: show that the user does not enjoy competitive games.

> Conditional statement 2 — related to "Do you prefer playing video games with friends?"
> if the response is "yes": show that the user prefers playing with friends.
> else: show that the user prefers playing alone.

> Conditional statement 3 — related to "Do you enjoy exploring large game worlds?"
> if the response is "yes": show that the user enjoys exploring game worlds.
> else: show that the user does not prefer exploring game worlds.

> Conditional statement 4 — related to "Do you care more about winning than the story?"
> if the response is "yes": show that winning is more important to the user than the story.
> else: show that the story is more important to the user than winning.

> Conditional statement 5 — related to "Do you play video games almost every day?"
> if the response is "yes": show that the user plays games frequently.
> else: show that the user does not play games every day.

> Conditional statement 6 — reveals the user's final gamer type based on their answers.
> if competitive is "yes" and winning is "yes": set gamer_type to "Competitive Gamer."
> elif exploring is "yes": set gamer_type to "Explorer Gamer."
> elif friends is "yes": set gamer_type to "Social Gamer."
> else: set gamer_type to "Casual Gamer."

> Display the user's final gamer type.


## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]


