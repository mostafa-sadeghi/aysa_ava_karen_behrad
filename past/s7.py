# for i in range(10):
#     print("I want to learn pygame")

# i = 0
# while i < 10:
#     print("I want to learn pygame")
#     i = i + 1

# import random

# for i in range(10):
#     random_number = random.randrange(10,21)
#     print(random_number)

# ACTIONS = ("rock", "paper", "scissors")
# while True:
#     computer_hand = random.choice(ACTIONS)
#     player_hand = input('enter "rock" "paper" "scissors" ')
#     # کدهای برنده شدن بازیکن
#     if player_hand == "paper" and computer_hand == "rock":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("player wins.")
#     elif player_hand == "scissors" and computer_hand == "paper":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("player wins")
#     elif player_hand == "rock" and computer_hand == "scissors":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("player wins.")
#     #  کدهای برنده شدن کامپیوتر
#     elif player_hand == "rock" and computer_hand == "paper":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("computer wins.")
#     elif player_hand == "paper" and computer_hand == "scissors":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("computer wins")
#     elif player_hand == "scissors" and computer_hand == "rock":
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("computer wins.")
#     else:
#         print("player's hand:", player_hand)
#         print("computer's hand:", computer_hand)
#         print("EQUAL")

#     print("Do you want to continue?('yes' or 'no') ")
#     if input('> ') == "no":
#         break


import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))

done = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.draw.polygon(screen, BLUE, [[0, 0], [0, 100], [100, 100], [100, 0]])
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
