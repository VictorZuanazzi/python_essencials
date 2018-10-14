fruit_to_colour = {
    'banana' : 'yellow',
    'cherry' : 'red',
    'orange' : 'orange',
    'pear' : 'green',
    'peach' : 'orange',
    'plum' : 'purple',
    'pomegranate' : 'red',
    'strawberry' : 'red'}

# invert fruit_to_colour.
colour_to_fruit = {}
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    

    # If colour is not already a ky in the accumulator,
    # add colour: [fruit] as an entry.
    if not(colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]


    # Otherwise, append fruit to the existing list.
    else:
        colour_to_fruit[colour].append(fruit)
