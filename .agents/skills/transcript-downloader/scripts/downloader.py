import argparse
import json
import sys
from pathlib import Path

from mr_transcript import get_languages, get_transcript


def list_languages(url):
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
