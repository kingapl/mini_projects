from random import choice

answers = ['Yes.',
    'Of course.',
    'Definitely yes.',
    'Probably yes.',
    'Undeniably.',
    'One hundred percent sure.',
    'A little patience and... yes.',
    'Everything will go your way.',
    'If that\'s what you want, yes.',
    'Sure.'
    'I don\'t know.',
    'Maybe.',
    'Maybe yes, maybe no.',
    'I do not confirm.',
    'I do not deny.',
    'Probably not.',
    'No.',
    'Definitely not.',
    'Never.',
    'Be under no illusions.',
]

question = input("Ask a yes or no question:\n")

answer = choice(answers)
print(answer)