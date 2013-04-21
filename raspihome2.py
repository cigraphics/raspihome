# Imports
import webiopi

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Buttons
B1=17   # pompa apa
B2=27   # incalzire podea
B3=22   # lumini
B4=23   # dezumidificator
B5=24   # electrovalva

    
# -------------------------------------------------- #
# Initialization part                                #
# -------------------------------------------------- #

# Setup GPIOs - toate porturile sunt de iesire
GPIO.setFunction(B1, GPIO.OUT)
GPIO.setFunction(B2, GPIO.OUT)
GPIO.setFunction(B3, GPIO.OUT)
GPIO.setFunction(B4, GPIO.OUT)
GPIO.setFunction(B5, GPIO.OUT)

# -------------------------------------------------- #
# Main server part                                   #
# -------------------------------------------------- #


# Instantiate the server on the port 8000, it starts immediately in its own thread
server = webiopi.Server(port=8000, login="raspihome", password="raspihome")

# -------------------------------------------------- #
# Loop execution part                                #
# -------------------------------------------------- #

# Run our loop until CTRL-C is pressed or SIGTERM received
webiopi.runLoop()

# -------------------------------------------------- #
# Termination part                                   #
# -------------------------------------------------- #

# Stop the server
server.stop()

# Reset GPIO functions
GPIO.setFunction(B1, GPIO.IN)
GPIO.setFunction(B2, GPIO.IN)
GPIO.setFunction(B3, GPIO.IN)
GPIO.setFunction(B4, GPIO.IN)
GPIO.setFunction(B5, GPIO.IN)
