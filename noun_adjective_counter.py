import requests
from bs4 import BeautifulSoup
from IPython.display import display, HTML
import nltk
import random

# Download NLTK resources (move these lines outside the loop if they're required only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define abcd_id_list
abcd_id_list = [50]  # Define the list of IDs

# Define the base URL
base_url = "https://www.projectabcd.com/display_the_dress.php?id="

# Randomly select an ID
random_id = random.choice(abcd_id_list)

# Getting the Sheroes
url = base_url + str(random_id)  # Incorporate random ID into URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting relevant information from the HTML
        name = soup.find('title').text if soup.find('title') else "Title not found"
        hyperlink = url
        description = soup.find('p').text if soup.find('p') else "Description not found"

        # Counting nouns and adjectives using NLTK
        tokens = nltk.word_tokenize(description)
        tagged_tokens = nltk.pos_tag(tokens)
        noun_count = sum(1 for _, tag in tagged_tokens if tag.startswith('NN'))
        adjective_count = sum(1 for _, tag in tagged_tokens if tag.startswith('JJ'))

        # Generating HTML table
        html_table = f"""
        <table border="1">
            <thead>
                <tr>
                    <th>Hyperlink</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Count of Nouns</th>
                    <th>Count of Adjectives</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{hyperlink}</td>
                    <td>{name}</td>
                    <td>{description}</td>
                    <td>{noun_count}</td>
                    <td>{adjective_count}</td>
                </tr>
            </tbody>
        </table>
        """
        display(HTML(html_table))
    except Exception as e:
        print("Error:", e)
else:
    print("Error:", response.status_code)
