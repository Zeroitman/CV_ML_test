from ultralytics import YOLO
from .main import VIDEO_PATH


def predict_model(video_path):
    model = YOLO('runs/yolo11m/50e/best.pt')

    for result in model.predict(
            source=video_path,  # путь к видео
            save=True,
            imgsz=320,
            conf=0.3,  # минимальный threshold
            stream=True  # не показывать в реальном времени
        ):
        print(result)


def main():
    video_path = f'{VIDEO_PATH}/2_1.MOV'
    predict_model(video_path)


if __name__ == "__main__":
    main()