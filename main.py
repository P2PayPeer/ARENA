# main.py for AI-ARENA

# Import necessary modules
from config.arena_config import ArenaConfig
from config.llm_config import LLMConfig
from ai_modules.onii_maid import OniiMaid
from ai_modules.leyley import LeyLey
from virtual_env.arena import VirtualArena
from user_interaction.input_handler import InputHandler
from battle_management.battle_round import BattleRound
from viewer_engagement.stream_integration import StreamIntegration
from monetization.subscription_system import SubscriptionSystem
from utils.logger import Logger

def main():
    # Initialize logger
    logger = Logger()
    logger.log("Starting AI-ARENA")

    # Load configurations
    arena_config = ArenaConfig()
    llm_config = LLMConfig()

    # Initialize AI Modules
    onii_maid = OniiMaid(llm_config)
    ley_ley = LeyLey(llm_config)

    # Set up the virtual environment
    virtual_arena = VirtualArena(arena_config)

    # Initialize user interaction handler
    input_handler = InputHandler()

    # Set up the battle management system
    battle_round = BattleRound(onii_maid, ley_ley)

    # Initialize viewer engagement modules
    stream_integration = StreamIntegration()

    # Initialize monetization systems
    subscription_system = SubscriptionSystem()

    # Main event loop
    while True:
        # Handle user input
        user_input = input_handler.get_input()
        if user_input == "exit":
            break

        # Process the input and update the arena
        response = battle_round.process_input(user_input)
        virtual_arena.update(response)

        # Stream updates
        stream_integration.stream_update(virtual_arena, battle_round)

#    # Main event loop [DEV: Leyley-13B]
#    while True:
#        # Display the menu
#        print("Welcome to AI-ARENA!")
#        print("1. Choose Characters")
#        print("2. Choose Arena Type")
#        print("3. Start Fight!")
#        print("4. Exit")
#        user_choice = int(input("Your choice: "))
    
#        # Process user input
#        if user_choice == 1:
#            character_choices = ["Onii-chan", "Ley-ley"]
#            selected_characters = []
#            while len(selected_characters) < 2:
#                print("Select characters: ")
#                for char in character_choices:
#                    print(f"{char} | {character_choices.index(char)}")
#                chosen_characters = [int(input(f"Enter number for '{ch}' (0 to dismiss): ")) for ch in character_choices]
#                if chosen_characters[0] != 0 and chosen_characters[1] != 0:
#                    selected_characters.extend([chosen_characters[0], chosen_characters[1]])
#                elif chosen_characters[0] == 0:
#                    print("Please select both characters.")
#                elif chosen_characters[1] == 0:
#                    print("Please select both characters.")
#                else:
#                    print("Invalid input.")
    
#            battle_round.set_fighters(selected_characters)
            
#        elif user_choice == 2:
#            room_types = ["Bedroom", "Kitchen", "Living Room"]
#            selected_rooms = []
#            while len(selected_rooms) < 1:
#                print("Choose arena types: ")
#                for room in room_types:
#                    print(f"{room} | {room_types.index(room)}")
#                chosen_room = input("Enter number for the desired room: ")
#                try:
#                    selected_rooms.append(room_types.index(chosen_room))
#                except ValueError:
#                    print("Invalid input. Please enter a valid option.")
    
#            battle_round.set_arena(selected_rooms[0])
#        elif user_choice == 3:
#            virtual_arena.start_match()
#        elif user_choice == 4:
#            break
    
    # Cleanup and exit
    logger.log("Shutting down AI-ARENA")
    virtual_arena.cleanup()

if __name__ == "__main__":
    main()
