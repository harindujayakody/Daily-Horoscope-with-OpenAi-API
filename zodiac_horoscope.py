import openai
import random
from datetime import datetime
import os

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

# Dictionary to map numbers to zodiac signs
zodiac_signs = {
    1: "Aries", 2: "Taurus", 3: "Gemini",
    4: "Cancer", 5: "Leo", 6: "Virgo",
    7: "Libra", 8: "Scorpio", 9: "Sagittarius",
    10: "Capricorn", 11: "Aquarius", 12: "Pisces"
}

# Dictionary to suggest lucky colors based on zodiac signs
lucky_colors = {
    "Aries": "Red",
    "Taurus": "Green",
    "Gemini": "Yellow",
    "Cancer": "Silver",
    "Leo": "Gold",
    "Virgo": "White",
    "Libra": "Blue",
    "Scorpio": "Black",
    "Sagittarius": "Purple",
    "Capricorn": "Brown",
    "Aquarius": "Turquoise",
    "Pisces": "Sea Green"
}

# Dictionary to specify lucky number ranges based on zodiac signs
lucky_number_ranges = {
    "Aries": (1, 3),
    "Taurus": (4, 6),
    "Gemini": (7, 9),
    "Cancer": (1, 3),
    "Leo": (4, 6),
    "Virgo": (7, 9),
    "Libra": (1, 3),
    "Scorpio": (4, 6),
    "Sagittarius": (7, 9),
    "Capricorn": (1, 3),
    "Aquarius": (4, 6),
    "Pisces": (7, 9)
}

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Function to get a horoscope using the OpenAI API
def get_horoscope(sign):
    prompt = f"What's the horoscope for {sign} today?"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text

# Function to generate a custom lucky number based on the zodiac sign
def generate_custom_lucky_number(sign):
    min_range, max_range = lucky_number_ranges.get(sign, (1, 9))
    return random.randint(min_range, max_range)

# Display the hero section with "How's your Day"
print("╭───────────────────────────────────────────╮")
print("│           How's your Day?                │")
print("╰───────────────────────────────────────────╯")

# Add a line break here
print()

# Display zodiac sign options in English
print("Select your zodiac sign:")
for number, sign in zodiac_signs.items():
    print(f"{number}. {sign}")

# Get user's choice
while True:
    try:
        user_choice = int(input("Enter the number of your zodiac sign: "))
        if user_choice in zodiac_signs:
            selected_sign = zodiac_signs[user_choice]
            break
        else:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Get and display the horoscope in English (removed for Gemini)
if selected_sign != "Gemini":
    horoscope = get_horoscope(selected_sign)
    print(f"\nHoroscope for {selected_sign}:")
    print(horoscope)

# Add a line break here
print()

# Generate and display a custom lucky number based on the zodiac sign
custom_lucky_number = generate_custom_lucky_number(selected_sign)
print(f"Your Custom Lucky Number for Today (based on {selected_sign}): {custom_lucky_number}")

# Display the suggested lucky color to wear
suggested_lucky_color = lucky_colors.get(selected_sign, "N/A")
if suggested_lucky_color != "N/A":
    print(f"Suggested Lucky Color to Wear for {selected_sign}: {suggested_lucky_color}\n")
else:
    print(f"Lucky Color information not available for {selected_sign}.\n")
