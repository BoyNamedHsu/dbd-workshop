import json
from pathlib import Path

from config import *


def main() -> None:

    config = {
        "name": CASE_NAME,
        "database": CASE_DB_NAME,
        "culpritName": CASE_CULPRIT,
        "evidenceFiles": CASE_EVIDENCE,
        "concepts": CASE_CONCEPTS,
        "author": CASE_AUTHOR,
        "difficulty": CASE_DIFFICULTY,
        "lockedTables": CASE_LOCKED_TABLES,
        "evidenceAudioFiles": CASE_AUDIO_EVIDENCE,
        "previewImage": CASE_PREVIEW_IMAGE,
        "culpritArrestImage": CASE_CULPRIT_ARREST_IMAGE,
        "arrestWarrant": CASE_ARREST_WARRANT,
        "voiceMessage": CASE_VOICE_MESSAGE,
        "voiceMessageTranscript": CASE_VOICE_TRANSCRIPT,
        "queryHints": CASE_QUERY_HINTS,
        "caseHints": CASE_STORY_HINTS
    }

    config_name = input("Name of the [config.json] file: ").strip() or "config.json"
    config_name = config_name if config_name.lower().endswith(".json") else f"{config_name}.json"
    config_path = Path(config_name)

    if config_path.exists():
        override = input(f"Overwrite file {config_path.name}? Yes or No [n]: ").lower().strip().startswith("y")
        if not override:
            print("No changes")
            return

    # These TODOs might be woth doing also in-game, so perhaps no point for double coding
    # TODO Add \n in caseHints or queryHints to assure visibility
    # TODO Some validation for e.g.
    # - concepts (limit valid tags)
    # - difficulty (limit valid tags)
    # - voiceMessage is actual valid MP3
    # - check existance of files
    # TODO Offer to remove extensions for better display in-game
    # TODO Add "deploy ready" validation, no dangling files etc.

    print(f"Writing to file {config_path.name}")
    with config_path.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
