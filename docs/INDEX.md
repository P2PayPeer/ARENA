### AI-ARENA Code Structure Overview

1. **Root Directory (`ai_arena/`):**
    - Contains all modules, configuration files, and the main execution script.

2. **Main Execution Script (`main.py`):**
    - The entry point of the application, handling the initial setup and triggering the main event loop.

3. **Configuration Files (`config/`):**
    - `arena_config.py`: Arena settings and rules.
    - `llm_config.py`: Configuration for LLMs (OniiMaid, LeyLey).

4. **AI Modules (`ai_modules/`):**
    - `onii_maid.py`: Module for OniiMaid LLM.
    - `ley_ley.py`: Module for LeyLey LLM.
    - `common.py`: Shared functionalities used by both LLMs.

5. **Virtual Environment (`virtual_env/`):**
    - `arena.py`: Handles the 3D virtual environment setup and dynamics.
    - `avatar.py`: Manages customizable avatars for humans and LLMs.
    - `environment_settings.py`: Configures different environments like bedrooms, outdoor settings, etc.

6. **User Interaction (`user_interaction/`):**
    - `input_handler.py`: Manages user text inputs and commands.
    - `feedback_system.py`: Handles user feedback collection and processing.

7. **Battle Management (`battle_management/`):**
    - `battle_round.py`: Controls the battle rounds, including pairing and timing.
    - `scoring_system.py`: Manages scoring based on feedback and performance metrics.

8. **Viewer Engagement (`viewer_engagement/`):**
    - `stream_integration.py`: Integrates AI-analyzed transcripts into live streams.
    - `commentary.py`: Provides live commentary during battles.

9. **Monetization (`monetization/`):**
    - `subscription_system.py`: Manages subscription plans and access.
    - `ppv_system.py`: Handles pay-per-view access for individual matches.
    - `merchandising.py`: Manages merchandise sales.
    - `token_system.py`: Implements a token-based voting and tipping system.
    - `advertising.py`: Manages targeted advertising integrations.

10. **Utility and Support (`utils/`):**
    - `logger.py`: For logging events and errors.
    - `helpers.py`: General utility functions used across modules.

11. **Tests (`tests/`):**
    - Unit and integration tests for each module.

12. **Documentation (`docs/`):**
    - Detailed documentation for developers, including API references and usage examples.

### Key Points

- **Modularity:** Each module is self-contained, focusing on a specific aspect of the AI-ARENA. This design allows developers to work on distinct parts without interfering with others.
- **Scalability:** The structure supports the addition of new features or LLMs easily.
- **Maintainability:** Clear separation of concerns makes it easier to maintain and update specific parts of the system.
- **Testability:** The modular approach facilitates comprehensive testing, ensuring each component functions correctly in isolation and when integrated.
