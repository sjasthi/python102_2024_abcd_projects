import random
import sheroes_base_lib

# Fetch Sheroes data from the API
sheroes_data = sheroes_base_lib.fetch_data_from_api(sheroes_base_lib.sheroes_id_list)

# Extract Sheroes' names from fetched data
sheroes = [data['name'] for data in sheroes_data]

# Function to generate a random Bingo card
def generate_bingo_card():
    if len(sheroes) < 25:
        raise ValueError("Not enough Sheroes available to generate a Bingo card.")
    card = random.sample(sheroes, 25)  # Select 25 random names
    card[12] = "FREE SPACE"  # Middle cell is the free space
    return card

# Function to print a Bingo card
def print_bingo_card(card):
    print("-" * 29)
    for i in range(5):
        row = "|".join("{:^5}".format(cell) for cell in card[i * 5: (i + 1) * 5])
        print("|" + row + "|")
        print("-" * 29)

# Generate Bingo cards for 10 players
for player in range(1, 11):
    print(f"Player {player} Bingo Card:")
    try:
        bingo_card = generate_bingo_card()
        print_bingo_card(bingo_card)
    except ValueError as e:
        print("Error:", e)
    print()
