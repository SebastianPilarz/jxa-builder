import logging
from jxa_builder.core.constants import LOG_FILE_ABS

# TODO: Make log file circular
logger = logging.getLogger(__name__)

shell_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOG_FILE_ABS)

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(100)
file_handler.setLevel(logging.DEBUG)

fmt_shell = '{levelname:<9} {filename}:{funcName}:{lineno} {message}'
fmt_file = '[{asctime}] {levelname:<9} {filename}:{funcName}:{lineno} {message}'
date_fmt = '%Y/%m/%d %H:%M:%S'

shell_formatter = logging.Formatter(fmt_shell, date_fmt, style='{')
file_formatter = logging.Formatter(fmt_file, date_fmt, style='{')

shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)
