from pygba import PyGBA, PyGBAEnv, PokemonEmerald

def setup_pokemon_environment(rom_path="PokemonEm.gba"):
    """
    Set up a Pokemon Emerald environment with PyGBA.

    Args:
        rom_path (str): Path to the Pokemon Emerald ROM file

    Returns:
        PyGBAEnv: Configured Pokemon environment
    """
    # Initialize GBA emulator with ROM
    gba = PyGBA.load(rom_path, autoload_save=True)

    # Create game wrapper with default reward settings
    game_wrapper = PokemonEmerald()

    # Create environment with human render mode enabled
    env = PyGBAEnv(
        gba=gba,
        game_wrapper=game_wrapper,
        render_mode="human",  # Set to "human" for window display
        obs_type="rgb",      # Use RGB observation type
        frameskip=0,         # No frame skipping for smooth rendering
        max_episode_steps=None  # No episode limit
    )

    return env

if __name__ == "__main__":
    # Create and start the environment
    env = setup_pokemon_environment()

    observation, info = env.reset()

    try:
        while True:
            # Render the current frame
            env.render()

            # No-op action (None, None) - index 0
            observation, reward, done, truncated, info = env.step(0)

            if done or truncated:
                observation, info = env.reset()

    except KeyboardInterrupt:
        print("\nClosing environment...")
        env.close()
