# main.py for AI-ARENA

# Import necessary modules
from config.arena_config import ArenaConfig
from config.llm_config import LLMConfig
from ai_modules.onii_maid import OniiMaid
from ai_modules.ley_ley import LeyLey
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

    # Cleanup and exit
    logger.log("Shutting down AI-ARENA")
    virtual_arena.cleanup()

if __name__ == "__main__":
    main()
