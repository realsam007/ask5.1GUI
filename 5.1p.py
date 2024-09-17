import RPi.GPIO as GPIO
import tkinter as tk

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red_pin = 17
green_pin = 27
yellow_pin = 22
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

# Function to turn on a specific LED
def set_led(led_pin):
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(led_pin, GPIO.HIGH)

# Tkinter GUI setup
root = tk.Tk()
root.title("LED Control")

# Variables for radio buttons
led_choice = tk.IntVar()
led_choice.set(0)  # Default to no selection

# Radio buttons for LED selection
tk.Radiobutton(root, text="Red LED", variable=led_choice, value=red_pin, command=lambda: set_led(red_pin)).pack()
tk.Radiobutton(root, text="Green LED", variable=led_choice, value=green_pin, command=lambda: set_led(green_pin)).pack()
tk.Radiobutton(root, text="Blue LED", variable=led_choice, value=yellow_pin, command=lambda: set_led(yellow_pin)).pack()

# Exit button
tk.Button(root, text="Exit", command=root.quit).pack()

# Main event loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()
import RPi.GPIO as GPIO
import tkinter as tk

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red_pin = 17
green_pin = 27
yellow_pin = 22
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

# Function to turn on a specific LED
def set_led(led_pin):
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(led_pin, GPIO.HIGH)

# Tkinter GUI setup
root = tk.Tk()
root.title("LED Control")

# Variables for radio buttons
led_choice = tk.IntVar()
led_choice.set(0)  # Default to no selection

# Radio buttons for LED selection
tk.Radiobutton(root, text="Red LED", variable=led_choice, value=red_pin, command=lambda: set_led(red_pin)).pack()
tk.Radiobutton(root, text="Green LED", variable=led_choice, value=green_pin, command=lambda: set_led(green_pin)).pack()
tk.Radiobutton(root, text="Yellow", variable=led_choice, value=yellow_pin, command=lambda: set_led(yellow_pin)).pack()

# Exit button
tk.Button(root, text="Exit", command=root.quit).pack()

# Main event loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()
