import os
import cv2
import albumentations as A
from tqdm import tqdm
from .main import MEDIA_PATH


def augmentation(augmentation_count=10):
    INPUT_IMAGES_DIR = f'{MEDIA_PATH}/dataset/images/train'
    INPUT_LABELS_DIR = f'{MEDIA_PATH}/dataset/labels/train'
    OUTPUT_IMAGES_DIR = f'{MEDIA_PATH}/dataset/images/train_aug/'
    OUTPUT_LABELS_DIR = f'{MEDIA_PATH}/dataset/labels/train_aug'

    os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_LABELS_DIR, exist_ok=True)

    # Аугментации
    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.3),
        A.ShiftScaleRotate(
            shift_limit=0.05, scale_limit=0.1, rotate_limit=10, p=0.5
        )
    ], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

    # Цикл по файлам
    for filename in tqdm(os.listdir(INPUT_IMAGES_DIR)):
        if not filename.endswith('.png'):
            continue

        img_path = os.path.join(INPUT_IMAGES_DIR, filename)
        label_path = os.path.join(
            INPUT_LABELS_DIR,
            filename.replace('.png', '.txt')
        )

        # Пропустить, если нет аннотаций
        if not os.path.exists(label_path):
            continue

        image = cv2.imread(img_path)
        h, w = image.shape[:2]

        # Загрузим bbox'ы
        bboxes = []
        class_labels = []
        with open(label_path, 'r') as f:
            for line in f.readlines():
                cls, x, y, bw, bh = map(float, line.strip().split())
                bboxes.append([x, y, bw, bh])
                class_labels.append(int(cls))

        for i in range(augmentation_count):
            augmented = transform(
                image=image, bboxes=bboxes, class_labels=class_labels
            )
            aug_img = augmented['image']
            aug_bboxes = augmented['bboxes']
            aug_labels = augmented['class_labels']

            # Сохраняем изображение
            new_img_name = filename.replace('.png', f'_aug{i}.png')
            new_img_path = os.path.join(OUTPUT_IMAGES_DIR, new_img_name)
            cv2.imwrite(new_img_path, aug_img)

            # Сохраняем аннотации
            new_label_path = os.path.join(
                OUTPUT_LABELS_DIR,
                new_img_name.replace('.png', '.txt')
            )
            with open(new_label_path, 'w') as f:
                for bbox, cls in zip(aug_bboxes, aug_labels):
                    f.write(f"{cls} {' '.join(f'{x:.6f}' for x in bbox)}\n")


def main():
    augmentations_count=10
    augmentation(augmentations_count)

if __name__ == "__main__":
    main()