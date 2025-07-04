from pathlib import Path
import os

PROJECT_DIR = Path(__file__).parent.parent

MEDIA_PATH = os.path.join(PROJECT_DIR, "media")
VIDEO_PATH = os.path.join(MEDIA_PATH, "video")
FRAMES_PATH = os.path.join(MEDIA_PATH, "frames")
