from datetime import datetime

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"[{start_time}] - '{func.__name__}' function started.")
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"[{end_time}] - '{func.__name__}' function finished.")

        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time.total_seconds():.5f} seconds")
        return result

    return wrapper
