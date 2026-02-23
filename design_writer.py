import os
import tempfile

def design_writer(
    sv_file_path: str,
    sv_text: str,
    mode: str = "atomic",   # "atomic" (recommended) or "direct"
    encoding: str = "utf-8"
) -> str:

    # Writes SystemVerilog code to a .sv file.

    # Modes:
    #   - "atomic": writes to a temp file first, then replaces target (safer)
    #   - "direct": writes directly to target

    # Returns:
    #   Absolute path of the written file.

    if not sv_file_path.lower().endswith(".sv"):
        raise ValueError(f"sv_file_path must end with .sv, got: {sv_file_path}")

    # Normalize + ensure directory exists
    sv_file_path = os.path.abspath(sv_file_path)
    out_dir = os.path.dirname(sv_file_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    if mode not in ("atomic", "direct"):
        raise ValueError("mode must be 'atomic' or 'direct'")

    if mode == "direct":
        with open(sv_file_path, "w", encoding=encoding, newline="\n") as f:
            f.write(sv_text)
        return sv_file_path

    # atomic mode: write to temp in same directory then replace
    fd, tmp_path = tempfile.mkstemp(prefix=".tmp_", suffix=".sv", dir=out_dir or None)
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline="\n") as f:
            f.write(sv_text)

        # Atomic replace on Windows + Unix
        os.replace(tmp_path, sv_file_path)
        return sv_file_path

    except Exception:
        # Cleanup temp file if something goes wrong
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise
