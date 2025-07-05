import os
import subprocess
from .main import FRAMES_PATH, VIDEO_PATH


def extract_frames(file_name, fps=1):
    video_file = os.path.join(VIDEO_PATH, file_name)
    output_path = os.path.join(FRAMES_PATH, file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_pattern = os.path.join(output_path, "frame_%05d.jpg")

    command = [
        'ffmpeg',
        '-i', video_file,
        '-vf', f'fps={fps}',
        '-qscale:v', '2',
        output_pattern
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Кадры успешно извлечены в {FRAMES_PATH} с частотой {fps} FPS.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при извлечении кадров: {e}")
    except FileNotFoundError:
        print("Ошибка: FFmpeg не найден.")


def main():
    file_name = "2_1.MOV"
    extract_frames(file_name, fps=1)

if __name__ == "__main__":
    main()
