import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download NLTK data required for tokenization and lemmatization
nltk.download('wordnet')  # Download WordNet data for lemmatization
# Download Open Multilingual WordNet for lemmatization
# nltk.download('omw-1.4')
nltk.download('punkt')    # Download NLTK tokenizer data
nltk.download('averaged_perceptron_tagger')  # Download NLTK POS tagger data


def lemmatize_sentence(sentence):
    """
    Lemmatize words in a sentence based on their part of speech (POS).

    Args:
        sentence (str): The input sentence to lemmatize.

    Returns:
        list of str: List of lemmatized words in the sentence.
    """
    sentence_lemmas = []
    lemmatizer = WordNetLemmatizer()
    word_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(word_tokens)

    for word_token, pos_tag in pos_tags:
        # Extract the first character (proper POS tag)
        pos = pos_tag[0].lower()
        if pos in ['n', 'v', 'a', 'r']:
            sentence_lemmas.append(lemmatizer.lemmatize(word_token, pos))
        # else:
        #     # Keep the original word if POS is not relevant
        #     sentence_lemmas.append(word_token)

    return sentence_lemmas


def find_closest_answer(text, question, similarity_threshold=0.3):
    """
    Find the closest matching answer to a question in a given text.

    Args:
        text (str): The original text containing sentences.
        question (str): The question to find the closest answer to.
        similarity_threshold (float, optional): The threshold for cosine similarity.
            Defaults to 0.3.

    Returns:
        str or None: The closest matching answer if found, or None if no matching answer is found.
    """
    # Initialize variables
    closest_answer = None

    # Tokenize the text into sentences
    sentence_tokens = nltk.sent_tokenize(text)
    sentence_tokens.append(question)

    # Initialize TfidfVectorizer with lemmatization tokenizer function
    tfidf_vectorizer = TfidfVectorizer(tokenizer=lemmatize_sentence)
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentence_tokens)

    # Compute cosine similarity between the question and each sentence
    similarity_values = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    similarity_coefficient = sorted(similarity_values.flatten())[-2]

    # Check if the similarity coefficient is above the threshold
    if similarity_coefficient > similarity_threshold:
        # Retrieve the index of the sentence with the highest similarity coefficient
        similarity_coefficient_idx = similarity_values.argsort()[0][-2]
        closest_answer = sentence_tokens[similarity_coefficient_idx]

    return closest_answer


def main():
    # Original text and question
    text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
    question = 'What are vegetables?'

    # Find the closest matching answer to the question in the provided text
    answer = find_closest_answer(text, question)

    # Print the original text
    print(f'\n- Input text is:\n=>', text)

    # Print the question
    print(f'\n- Question is:\n=>', question)

    # Print the closest answer to the question from the provided text
    print(f'\n- The closest answer to the question from the provided text is:\n=>', end=" ")

    # Check if a matching answer was found
    if answer is None:
        # Indicate that no matching answer was found
        print("No matching answer found.")
    else:
        # Print the closest matching answer
        print(answer)

    print()


if __name__ == "__main__":
    main()
