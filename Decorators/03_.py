# Import wraps from functools
# This ensures that when we decorate a function, 
# the wrapper keeps the original function’s metadata (like name, docstring).
from functools import wraps

# Define the decorator function
def log_activity(func):
    """
    A decorator that logs when a function starts and finishes execution.
    """

    # Use @wraps to preserve the original function’s identity
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before calling the actual function, log its name
        print(f"Calling: {func.__name__}")

        # Call the original function with all arguments
        result = func(*args, **kwargs)

        # After the function finishes, log again
        print(f"Finished Calling: {func.__name__}")

        # Return the result so the decorated function behaves normally
        return result

    # Return the wrapper function so it replaces the original
    return wrapper


@log_activity
def greet(name):
    """Simple function to greet someone by name."""
    print(f"Hello, {name}!")

# When we call greet, the decorator adds logging around it
greet("Vishal")

# Output:
# Calling: greet
# Hello, Vishal!
# Finished Calling: greet
