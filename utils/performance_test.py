import os
import time
import logging
from functools import wraps

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Create your own dedicated logger (avoids root logger conflicts)
perf_logger = logging.getLogger("performance_logger")
perf_logger.setLevel(logging.INFO)

# Avoid adding multiple handlers if script is reloaded
if not perf_logger.handlers:
    file_handler = logging.FileHandler("logs/performance.log", mode="a")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    perf_logger.addHandler(file_handler)

def log_runtime(func):
    """
    A decorator to measure and log the runtime of a function.
    Writes logs to logs/performance.log
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        msg = f"Function '{func.__name__}' executed in {runtime:.4f} seconds."
        print(msg)
        perf_logger.info(msg)
        return result
    return wrapper


