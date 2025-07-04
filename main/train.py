from ultralytics import YOLO


def train_model(name):
    model = YOLO('yolo11n.pt')

    model.train(
        data='dataset.yaml',
        name=name,
        project='runs',
        epochs=50,
        imgsz=640,
        batch=4
    )


def main():
    name = 'custom_yolo_training7'
    train_model(name)


if __name__ == "__main__":
    main()
