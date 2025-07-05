from ultralytics import YOLO


def train_model(name):
    model = YOLO('yolo11n.pt')

    model.train(
        data='dataset.yaml',
        name=name,
        project='runs',
        epochs=40,
        imgsz=448,
        batch=-1
    )


def main():
    name = 'my_result'
    train_model(name)


if __name__ == "__main__":
    main()
