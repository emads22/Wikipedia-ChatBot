# Wikipedia ChatBot

```cmd
 __        __ _  _     _                   _  _           ____  _             _    ____          _   
 \ \      / /(_)| | __(_) _ __    ___   __| |(_)  __ _   / ___|| |__    __ _ | |_ | __ )   ___  | |_ 
  \ \ /\ / / | || |/ /| || '_ \  / _ \ / _` || | / _` | | |    | '_ \  / _` || __||  _ \  / _ \ | __|
   \ V  V /  | ||   < | || |_) ||  __/| (_| || || (_| | | |___ | | | || (_| || |_ | |_) || (_) || |_ 
    \_/\_/   |_||_|\_\|_|| .__/  \___| \__,_||_| \__,_|  \____||_| |_| \__,_| \__||____/  \___/  \__|
                         |_|                                                                         
```

## Overview
Wikipedia ChatBot is a simple chatbot application that allows users to interactively learn about various topics by fetching information from Wikipedia. Users can input a topic of interest, and the chatbot retrieves the corresponding Wikipedia article. Users can then ask questions related to the topic, and the chatbot provides answers based on the closest match found in the article text.

## Features
- **Interactive Learning**: Users can input topics of interest and ask questions to learn about different subjects.
- **Wikipedia Integration**: The chatbot fetches information from Wikipedia articles to provide answers to user queries.
- **Closest Matching Answer**: The chatbot utilizes Natural Language Processing (NLP) techniques to provide interactive learning experiences. By leveraging NLP algorithms and libraries, such as NLTK (Natural Language Toolkit) and scikit-learn, the chatbot can fetch information from Wikipedia articles and find the closest matching answers to user questions using cosine similarity. 

## Setup
1. Clone the repository.
2. Navigate to the project directory:

   ```bash
   cd path/to/project/directory
   ```

3. Ensure Anaconda or Miniconda is installed on your system.
4. Create a Conda environment using the provided `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   ```

5. Activate the Conda environment:

   ```bash
   conda activate chatbot_env
   ```

6. Configure the necessary parameters such as `BOT_PROMPT`, `USER_PROMPT`, and `EXIT_PROMPTS` in `constants.py`.
- Additional setup steps may include configuring any API keys or authentication tokens required for accessing Wikipedia.
7. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Enter a topic of interest when prompted.
3. Ask questions related to the chosen topic.
4. To exit the chatbot, type 'q' or 'quit' when prompted for a topic or question.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.