import subprocess
import os
from functools import wraps
from dotenv import load_dotenv


def run_script(script_path: str):
    """run_script Decorator to run bash scripts before entry point functions

    Args:
        script_path (str): Path to the script from the root directory.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if the script is executable
            if os.access(script_path, os.X_OK):
                # Run the shell script
                subprocess.run(["bash", script_path], check=True)
            else:
                raise FileNotFoundError(
                    f"Script {script_path} is not executable or not found."
                )
            # Call the actual function
            return func(*args, **kwargs)

        return wrapper

    return decorator


def load_env(env_file=".env"):
    """
    Decorator to load environment variables from a specified .env file
    and then run the decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Load environment variables from the .env file
            load_dotenv(env_file)
            # Call the decorated function
            return func(*args, **kwargs)

        return wrapper

    return decorator
