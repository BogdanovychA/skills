import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def ensure_dependencies():
    """Ensures dependencies are available, or re-executes with the right environment."""
    try:
        import mr_transcript  # noqa: F401

        return  # Already available
    except ImportError:
        pass

    if os.environ.get("TRANSCRIPT_DOWNLOADER_REEXEC"):
        print("Error: Dependencies missing even after re-execution.", file=sys.stderr)
        sys.exit(1)

    os.environ["TRANSCRIPT_DOWNLOADER_REEXEC"] = "1"

    # Try uv
    uv_path = shutil.which("uv")
    if uv_path:
        script_path = os.path.abspath(__file__)
        args = [
            uv_path,
            "run",
            "--with",
            "mr-transcript",
            "python3",
            script_path,
        ] + sys.argv[1:]
        os.execv(uv_path, args)

    # Fallback to venv
    skill_dir = Path(__file__).resolve().parent.parent
    venv_dir = skill_dir / ".venv"

    if not venv_dir.exists():
        print(
            f"uv not found. Creating virtual environment in {venv_dir}...",
            file=sys.stderr,
        )
        try:
            subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
            pip_path = venv_dir / "bin" / "pip"
            if not pip_path.exists():
                pip_path = venv_dir / "Scripts" / "pip.exe"
            subprocess.run([str(pip_path), "install", "mr-transcript"], check=True)
        except Exception as e:
            print(f"Error creating virtual environment: {e}", file=sys.stderr)
            sys.exit(1)

    python_exe = venv_dir / "bin" / "python3"
    if not python_exe.exists():
        python_exe = venv_dir / "bin" / "python"
    if not python_exe.exists():
        python_exe = venv_dir / "Scripts" / "python.exe"

    if not python_exe.exists():
        print("Error: Could not find python executable in venv.", file=sys.stderr)
        sys.exit(1)

    script_path = os.path.abspath(__file__)
    os.execv(str(python_exe), [str(python_exe), script_path] + sys.argv[1:])


def list_languages(url):
    from mr_transcript import get_languages

    try:
        languages = get_languages(url)
        if not languages:
            print("No subtitles available for this video.")
            return
        print(json.dumps(languages, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error fetching languages: {e}", file=sys.stderr)
        sys.exit(1)


def download_transcript(url, lang, output):
    from mr_transcript import get_transcript

    try:
        transcript = get_transcript(url, language=lang)
        if not transcript:
            print(f"Could not download transcript in language '{lang}'.")
            return

        if not output:
            # Generate default filename from URL and language
            video_id = (
                url.split("v=")[-1].split("&")[0] if "v=" in url else url.split("/")[-1]
            )
            output = f"{video_id}_{lang}.txt"

        with open(output, 'w', encoding='utf-8') as f:
            f.write(transcript)

        print(f"Transcript saved to: {output}")
    except Exception as e:
        print(f"Error downloading transcript: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    # Ensure dependencies BEFORE parsing arguments
    ensure_dependencies()

    parser = argparse.ArgumentParser(
        description="Download YouTube transcripts using mr-transcript."
    )
    parser.add_argument("--list", help="List available languages for the URL")
    parser.add_argument("--download", help="Download transcript from the URL")
    parser.add_argument("--lang", help="Language code for download (e.g., 'en')")
    parser.add_argument("--output", help="Output filename")

    args = parser.parse_args()

    if args.list:
        list_languages(args.list)
    elif args.download:
        if not args.lang:
            print("Error: --lang is required for download.", file=sys.stderr)
            sys.exit(1)
        download_transcript(args.download, args.lang, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
