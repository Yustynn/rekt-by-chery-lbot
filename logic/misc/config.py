import sys

DEAD_MESSAGES = [
    "What's this? $NAME is evolving... $NAME evolved into. No. No wait. $NAME is dead. Sorry.",
    "Hey $NAME, remember when you used to be alive?",
    "I hope the dead person is $NAME. Is it $NAME? It's $NAME."
]

REKT_MESSAGES = [
    "And thusly as dear $NAME was casually minding their own business did the powers of Cheryl scorch their flesh.",
    "$NAME, are you sure your name isn't Icarus? Cause you been burnt.",
    "$NAME got rekt! On an unrelated note, let's all take a moment to be grateful for how blessed we are to have Cheryl, the nicest person, be part of our Capstone group.",
    "$NAME, it's better to let someone think you are an Idiot than to open your mouth and prove it.",
    "$NAME, if laughter is the best medicine, your face must be curing the world."
]

# Currently unused
DEAD_REKT_MESSAGES = [
    "Cheryl don't necro leh.",
    "And so dread empress Cheryl decided that death was not enough and began hacking $NAME's corpse to pieces."
]

SEVERITY_RANKINGS = [
    ('Rare', 'Medium-well', 'Overcooked'),
    ('Fried chicken', 'Fried fried chicken', 'Fried fried fried chicken'),
    ('First Degree Burn', 'Second degree burn', 'Third degree burn'),
    ('Just a bit warm', 'Cigarette burn', 'Offering to dead relatives')
]

INIT_HP = 40
DAMAGE_MULTIPLIER = 10

PEOPLE = [
    'Cheryl',
    'Gabriel',
    'Kady',
    'Tze How',
    'Yos',
    'Yustynn'
]

TOKEN = '694288013:AAFN4oN35zoE7oGB8Ixnyt9VChLvNnXbDKo'
