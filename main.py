import sys
import wikipedia
from app_utils import find_closest_answer
from constants import *


def testing_function():
    """
    A function to test finding the closest matching answer to a question within a given text.

    Args:
        None

    Returns:
        None
    """

    # Original text and question
    text = """
A yacht is a luxurious watercraft typically used for recreational purposes, often associated with leisurely sailing or cruising. These vessels are usually privately owned and can range in size from small, sleek sailing yachts to large, extravagant motor yachts equipped with modern amenities such as spacious cabins, gourmet kitchens, and entertainment systems. Yachts are commonly seen in coastal areas and are popular among the affluent for hosting parties, enjoying vacations, or simply basking in the serenity of the open sea.
"""
    question = 'Where are yachts seen?'

    # Find the closest matching answer to the question in the provided text
    answer = find_closest_answer(text, question)

    # Print the original text
    print(f'\n\n- Input text is:\n\n=>', text)

    # Print the question
    print(f'\n\n- Question is:\n\n=>', question)

    # Print the closest answer to the question from the provided text
    print(f'\n\n- The closest answer to the question from the provided text is:\n\n=>', end=" ")

    # Check if a matching answer was found
    if answer is None:
        # Indicate that no matching answer was found
        print("No matching answer found.")
    else:
        # Print the closest matching answer
        print(answer)

    print("\n")


def get_and_validate_input(prompt):
    """
    Get and validate user input.

    Args:
    - prompt (str): The prompt message displayed to the user.

    Returns:
    - user_input (str): The validated user input.
    """

    while True:
        # Prompt the user for input
        user_input = input(f"\n{BOT_PROMPT}{prompt.title()} (Type 'q' or 'quit' to exit):\n{
                           USER_PROMPT}").strip().lower()

        # Check if user_input is not empty
        if user_input:
            break
        else:
            # If user_input is empty, prompt the user to enter a valid input
            print(f"\n{BOT_PROMPT}Please enter a valid {prompt}.")

    return user_input


def wikipedia_chatbot():
    """
    Simple chatbot function that greets the user, asks for a topic, fetches
    the corresponding Wikipedia article, and then continuously prompts the user
    for questions related to the topic, providing answers based on the closest match
    found in the article text. The chatbot terminates if the user inputs an exit command.
    """

    # Print initial greeting message
    print(f"\n\n{BOT_PROMPT}Hi there! I'm here to help you learn about any topic. Please tell me what topic you'd like to learn about.")

    # Main loop for conversation
    while True:
        # Ask user for a topic
        topic = get_and_validate_input("topic")

        # Check if user wants to exit
        if topic in EXIT_PROMPTS:
            print(f"\n{BOT_PROMPT}Goodbye!\n")
            break

        try:
            # # Fetch a 5 sentences summary of the Wikipedia article on the given topic
            # text = wikipedia.summary(topic, sentences=5)

            # Fetch Wikipedia article content for the given topic
            text = wikipedia.page(topic).content

            # Inform the user that the topic is found
            print(f"\n{BOT_PROMPT}Great! Let's talk about '{
                  topic.title()}'. Feel free to ask any questions.")
        except wikipedia.exceptions.DisambiguationError as e:
            # If there are multiple options for the topic, ask the user to be more specific
            print(f"\n{
                  BOT_PROMPT}There are multiple options for this topic. Please be more specific.")
            continue
        except wikipedia.exceptions.PageError as e:
            # If no information is found for the topic, inform the user and ask for another topic
            print(f"\n{
                  BOT_PROMPT}Sorry, I couldn't find any information on that topic. Please try another one.")
            continue

        # Loop for answering questions related to the topic
        while True:
            # Ask the user for a question
            question = get_and_validate_input("question")

            # Check if user wants to exit
            if question in EXIT_PROMPTS:
                print(f"\n{BOT_PROMPT}Goodbye!\n")
                return

            # Find and display the closest answer to the question
            output = find_closest_answer(text, question)

            if output:
                print(f"\n{BOT_PROMPT}{output}")
            else:
                print(
                    f"\n{BOT_PROMPT}Sorry, I don't have an answer to that question.")


if __name__ == "__main__":
    try:
        # # Test the ChatBot
        # testing_function()

        # Call the chatbot function
        wikipedia_chatbot()

        # Print a message indicating successful completion
        print("\n=== Thank you for using our ChatBot. ===\n\n")

        # Exit the program
        sys.exit()

    except Exception:
        # If an exception occurs, raise it
        raise
