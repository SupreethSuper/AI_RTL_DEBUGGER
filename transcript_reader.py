#load trasnscript file path

transcript_file_path = r"C:\Users\supre\OneDrive - Arizona State University\AI chip\buffer\code\AI_RTL_DEBUGGER\transcript"


def read_transcript(path = transcript_file_path):
    """
    Reads the ModelSim transcript file and returns lines as a list.
    """
    try:
        with open(path, "r") as f:
            lines = f.readlines()
        return lines

    except FileNotFoundError:
        print(f"[ERROR] Transcript file not found at: {path}")
        return []

if __name__ == "__main__":
    transcript_lines = read_transcript()

    print("---- TRANSCRIPT START ----")
    for line in transcript_lines:
        print(line.strip())
    print("---- TRANSCRIPT END ----")


