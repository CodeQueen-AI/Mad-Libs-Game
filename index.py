def mad_libs():
    print("Welcome to the Mad Libs game!")
    print("Fill in the blanks to create your own funny story.")

    # User inputs
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    # Predefined story
    story = f"""
    Once upon a time, in a faraway {place}, there was a {adjective} {noun}.
    Every day, it would {verb} to make everyone laugh.
    People from all over the world would come to {place} just to see the amazing {noun}.
    And so, the {adjective} {noun} became the happiest in the land!
    """

    # Print the story
    print("\nHere's your Mad Libs story:")
    print(story)

# Run the Mad Libs game
mad_libs()