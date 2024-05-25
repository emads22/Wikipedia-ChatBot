import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def download_nltk_data():
    """
    Download NLTK data required for tokenization, lemmatization, and part-of-speech tagging.

    This function downloads the following NLTK datasets:
    - `wordnet`: Data required for lemmatization.
    - `omw-1.4`: Open Multilingual WordNet for lemmatization.
    - `punkt`: Tokenizer data required for text tokenization.
    - `averaged_perceptron_tagger`: Data required for part-of-speech tagging.
    """
    nltk.download('wordnet')
    # nltk.download('omw-1.4')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')


def lemmatize_sentence(sentence):
    """
    Lemmatize words in a sentence based on their part of speech (POS).

    Args:
        sentence (str): The input sentence to lemmatize.

    Returns:
        list of str: List of lemmatized words in the sentence.
    """
    # Initialize an empty list to store lemmatized words
    sentence_lemmas = []

    # Initialize a WordNetLemmatizer instance
    lemmatizer = WordNetLemmatizer()

    # Tokenize the input sentence into words and convert to lowercase
    word_tokens = nltk.word_tokenize(sentence.lower())

    # Perform part-of-speech tagging on the word tokens
    pos_tags = nltk.pos_tag(word_tokens)

    # Iterate over each word token and its corresponding POS tag
    for word_token, pos_tag in pos_tags:
        # Extract the first character of the POS tag (to match WordNet format)
        pos = pos_tag[0].lower()

        # Check if the POS tag is relevant for lemmatization (noun, verb, adjective, adverb)
        if pos in ['n', 'v', 'a', 'r']:
            # Lemmatize the word based on its POS tag and append to the list of lemmas
            sentence_lemmas.append(lemmatizer.lemmatize(word_token, pos))
        # If the POS tag is not relevant, keep the original word
        # else:
        #     sentence_lemmas.append(word_token)

    # Return the list of lemmatized words
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
    # Download NLTK data required for text processing
    download_nltk_data()

    # Initialize variables
    closest_answer = None

    # Tokenize the text into sentences
    sentence_tokens = nltk.sent_tokenize(text)
    # Append the question to the tokenized sentences for comparison
    sentence_tokens.append(question)

    # Initialize TfidfVectorizer with lemmatization tokenizer function
    tfidf_vectorizer = TfidfVectorizer(tokenizer=lemmatize_sentence)
    # Fit and transform the sentence tokens into TF-IDF matrix
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentence_tokens)

    # Compute cosine similarity between the question and each sentence
    similarity_values = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    # Sort the similarity values in ascending order
    sorted_similarity_values = sorted(similarity_values.flatten())
    # Get the second highest similarity coefficient, as the highest similarity is with the question itself
    highest_similarity_coefficient = sorted_similarity_values[-2]

    # Check if the highest similarity coefficient exceeds the threshold
    if highest_similarity_coefficient > similarity_threshold:
        # Retrieve the index of the sentence with the highest similarity coefficient
        highest_similarity_coefficient_idx = similarity_values.argsort()[0][-2]
        # Get the closest answer from the sentence tokens
        closest_answer = sentence_tokens[highest_similarity_coefficient_idx]

    return closest_answer
