
import random
import os

# ==================== HANGMAN ASCII ART ====================
HANGMAN_STAGES = [
    # Stage 0: Empty
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    # Stage 1: Head
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    # Stage 2: Body
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    # Stage 3: Left Arm
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    # Stage 4: Right Arm
    """
       ------
       |    |
       |    O
       |   /|\
       |
       |
    --------
    """,
    # Stage 5: Left Leg
    """
       ------
       |    |
       |    O
       |   /|\
       |   /
       |
    --------
    """,
    # Stage 6: Right Leg (Game Over)
    """
       ------
       |    |
       |    O
       |   /|\
       |   / \
       |
    --------
    """
]