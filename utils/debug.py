import logging
import colorlog

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler with a colored formatter
console_handler = logging.StreamHandler()
console_formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s\033[0m',
    log_colors={
        'DEBUG': 'reset',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# # Test the logger
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
