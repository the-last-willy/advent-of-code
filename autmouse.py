import pyautogui
import time
import random
import keyboard  # For detecting key presses

def move_mouse_randomly(duration=60):
    """Moves the mouse randomly for a specified duration or until ESC is pressed."""
    start_time = time.time()
    screen_width, screen_height = pyautogui.size()

    while time.time() - start_time < duration:
        if keyboard.is_pressed('esc'):  # Check if ESC is pressed
            print("Escape key pressed. Stopping mouse movement.")
            return  # Exit the function

        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(random.uniform(1, 3))

def move_mouse_in_circle(duration=60, radius=100, center_x=None, center_y=None):
    """Moves the mouse in a circle until ESC is pressed."""
    import math

    start_time = time.time()
    screen_width, screen_height = pyautogui.size()

    if center_x is None:
        center_x = screen_width // 2
    if center_y is None:
        center_y = screen_height // 2

    while True: # Loop indefinitely until ESC is pressed
        if keyboard.is_pressed('esc'):
            print("Escape key pressed. Stopping mouse movement.")
            return

        for i in range(0, 360, 10):
            if keyboard.is_pressed('esc'): # Check inside the loop as well
                print("Escape key pressed. Stopping mouse movement.")
                return

            x = center_x + radius * math.cos(math.radians(i))
            y = center_y + radius * math.sin(math.radians(i))

            x = max(0, min(x, screen_width - 1))
            y = max(0, min(y, screen_height - 1))

            pyautogui.moveTo(x, y, duration=0.1)
            time.sleep(0.01)

if __name__ == "__main__":
    print("Starting mouse movement in 5 seconds. Press ESC to stop.")
    time.sleep(5)

    # Example usage:
    #move_mouse_randomly()  # Runs until ESC is pressed or the default duration (60s)
    move_mouse_in_circle(radius=150) # Runs until ESC is pressed

    print("Mouse movement complete.")