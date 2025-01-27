import random

def get_user_choice():
    # Pobieramy wybór użytkownika
    user_input = input("Wybierz (kamień, papier, nożyce): ").lower()
    while user_input not in ["kamień", "papier", "nożyce"]:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        user_input = input("Wybierz (kamień, papier, nożyce): ").lower()
    return user_input

def get_computer_choice():
    # Generujemy losowy wybór dla komputera
    return random.choice(["kamień", "papier", "nożyce"])

def determine_winner(user_choice, computer_choice):
    # Określamy zwycięzcę
    if user_choice == computer_choice:
        return "Remis!"
    elif (user_choice == "kamień" and computer_choice == "nożyce") or \
         (user_choice == "papier" and computer_choice == "kamień") or \
         (user_choice == "nożyce" and computer_choice == "papier"):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"

def play_game():
    print("Witaj w grze Kamień, Papier, Nożyce!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Twój wybór: {user_choice}")
    print(f"Wybór komputera: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
