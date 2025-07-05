import shutil
import os
from sklearn.model_selection import train_test_split
from .main import MEDIA_PATH


def create_dataset(folder_name):
    images_dir = f'{MEDIA_PATH}/{folder_name}/images'
    labels_dir = f'{MEDIA_PATH}/{folder_name}/labels'

    images = sorted([f for f in os.listdir(images_dir)])

    # 1. Делим на train/val/test, поставил 70/20/10 т.к маленкьий датасет
    train_val, test = train_test_split(images, test_size=0.1, random_state=42)
    train, val = train_test_split(train_val, test_size=0.22, random_state=42)

    # 2. Создаём директории
    for string, obj in {'train': train, 'val': val, 'test': test}.items():
        dataset_images_folder = f'{MEDIA_PATH}/dataset/images/{string}'
        dataset_labels_folder = f'{MEDIA_PATH}/dataset/labels/{string}'

        os.makedirs(dataset_images_folder, exist_ok=True)
        os.makedirs(dataset_labels_folder, exist_ok=True)

        # 3. Копируем изображения и соответствующие .txt
        for filename in obj:
            shutil.copy(
                f"{images_dir}/{filename}",
                f"{dataset_images_folder}/{filename}"
            )
            label_file = filename.replace('.jpg', '.txt')
            shutil.copy(
                f"{labels_dir}/{label_file}",
                f"{dataset_labels_folder}/{label_file}"
            )


def main():
    folder_name = "download"
    create_dataset(folder_name)

if __name__ == "__main__":
    main()
