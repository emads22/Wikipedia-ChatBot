from app_utils import find_closest_answer


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


if __name__ == "__main__":
    testing_function()
