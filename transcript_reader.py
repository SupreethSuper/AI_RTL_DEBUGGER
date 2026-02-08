import re

transcript_file_path = r"transcript"

def get_final_error_count(path=transcript_file_path):
    """
    Reads a ModelSim transcript and returns the FINAL error count.

    Returns:
        int  -> final error count (0, 1, 2, ...)
        None -> if not found or file missing
    """
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None

    pattern = re.compile(
        r"Final\s+error\s+count\s*[:=]\s*(\d+)",
        re.IGNORECASE
    )

    final_count = None

    for line in lines:
        match = pattern.search(line)
        if match:
            final_count = int(match.group(1))  # keep overwriting → last one wins

    return final_count


# Optional: allow standalone execution for debugging
if __name__ == "__main__":
    count = get_final_error_count()

    if count is None:
        print("Final error count not found")
    else:
        print(f"Final error count = {count}")
