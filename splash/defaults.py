
# timeouts
TIMEOUT = 60
WAIT_TIME = 0.0

MAX_TIMEOUT = 90.0
MAX_WAIT_TIME = 30.0

# global render options
LOAD_FINISHED_OK_DELAY = 1000 # milliseconds
LOAD_FINISHED_RENDER_DELAY = 1000 # milliseconds

# png rendering options
VIEWPORT = '1024x768'
VIEWPORT_FALLBACK = VIEWPORT  # do not set it to 'full'
VIEWPORT_MAX_WIDTH = 20000
VIEWPORT_MAX_HEIGTH = 20000
VIEWPORT_MAX_AREA = 4000*4000

MAX_WIDTH = 1920
MAX_HEIGTH = 1080

# on screen rendering options
WINDOW_GRID_WIDTH = 25
WINDOW_GRID_HEIGHT = 2

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 768
WINDOW_MAX_WIDTH  = 1200
WINDOW_MAX_HEIGHT = 3500

# defaults for render.json endpoint
DO_HTML = 0
DO_IFRAMES = 0
DO_PNG = 0
SHOW_SCRIPT = 0
SHOW_CONSOLE = 0

# servers
SPLASH_PORT = 8050
PROXY_PORT = 8051
MANHOLE_PORT = 5023
MANHOLE_USERNAME = 'admin'
MANHOLE_PASSWORD = 'admin'

# pool options
SLOTS = 50
CACHE_ENABLED = True
CACHE_SIZE = 50  # MB
CACHE_PATH = '.splash-cache'
