import nltk
from IPython.display import display, HTML

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def count_nouns_and_adjectives(text):
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    noun_count = 0
    adjective_count = 0

    for _, tag in tagged_tokens:
        if tag.startswith('NN'):  # Nouns
            noun_count += 1
        elif tag.startswith('JJ'):  # Adjectives
            adjective_count += 1

    return noun_count, adjective_count

def generate_html_table(description, did_you_know):
    noun_count, adjective_count = count_nouns_and_adjectives(description)
    html_table = f"""
    <table border="1">
      <thead>
        <tr>
          <th>Serial No (of SHEROES)</th>
          <th>hyperlink</th>
          <th>Description</th>
          <th>Count of Nouns</th>
          <th>Count of Adjectives</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>https://abcd2.projectabcd.com/display_the_dress.php?id=1</td>
          <td>Namaste</td>
          <td>{description}</td>
          <td>{noun_count}</td>
          <td>{adjective_count}</td>
        </tr>
      </tbody>
    </table>
    """
    return html_table

# Input description and "did_you_know" text
description = "Namasthe is a customary, non-contact form of Hindu greeting. Namaste is usually spoken with a slight bow and hands pressed together, palms touching and fingers pointing upwards. Namaste is used as a form of greeting, acknowledging, and welcoming a relative, guest, or stranger. In some contexts, it can be used to express gratitude for assistance offered or given and to thank people for their generosity. "
did_you_know = "The gesture of joining both hands has more than a symbolic meaning. It is said to provide a connection between the right and left hemispheres of the brain thus representing unification."

# Generate HTML table
html_table = generate_html_table(description, did_you_know)
display(HTML(html_table))
