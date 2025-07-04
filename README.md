Извлечение кадров из видео
1. Закиньте видео которые из которого вы хотите извлечь кадры в папку cv_ml_test/video
2. На 31 строке модуля cv_ml_test/main/extract_frames.py укажите название файла(file_name)
3. Выполните извлечение кадров командой python -m main.extract_frames.
Отмечу, что по умолчанию стоит значение fps=1, т.е. 1 кадр в секунду.
4. Результат будет сохранен в папку cv_ml_test/media/frames/file_name

Аннотировать изображения (bounding boxes + классы)
Необходимо выбрать программу для аннотирования. Я использовал Label Studio.
Ниже команды для развертывания
pip install poetry

poetry new my-label-studio
cd my-label-studio
poetry add label-studio

### activate poetry environment
poetry env active # выведет команду для активации, выполнить её

# для локального получения данных, home/user ваша основная папка
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/home/sasha
### Start the server at http://localhost:8080
label-studio

После этого в бразуере будет открыта программа Label Studio по адресу http://localhost:8080
Далее
5. Зайти и вбить email и password
6. Создать аккаунт
7. Войти под указанными кредами
8. Create Project и вбить наименование и описание(опционально) проекта
9. Для импорта подключите хранилище, перейдети в раздел Settings проекта
10. Cloud Storage → Added source storage → Storage type → Local Files
11. Укажите путь до папки с изображениями из пункта 4. Например. /home/sasha/TestProjects/cv_ml_test/media/frames/4.MOV
12. В File Filter Regex укажи какие файлы искать. Например .*png
13. Активируй Treat every bucket object as a source file
14. Check connection должен вернуть Successfully connected!
15. Нажать Save → Sync Storage, теперь изображения будут загружены
16. Для присвоения классов необходимо Settings → Labeling Interface → Browse Templates → Object Detection with Bounding Boxes
17. Для добавления классов Add label names
18. Далее необходимо размечать изображения для этого необходимо разметить разобрать видео и кадры и определиться с классами. 
19. Сохраните результаты
20. Экспортируйте только размеченные кадры в формат YOLO with Images, можно использовать фильтр Annotated_by
21. Перенеси экспортируемые данные в папку media в проекте
22. На 6 строке модуля cv_ml_test/main/create_dataset.py укажите название папки(folder_name)
23. Выполните команду python -m main.create_dataset. Будет создан dataset и будет произведено разделение на train/val/test
24. Выполните команду python -m main.albumentation для аугементации данных
25. Поправьте файл dataset.yaml
26. Выполните команду python -m main.learning для обучения


Заключение.
Взял видео 2_1.MOV и разметил все классы блюд все кадры не размечал, периодически пропускал наборы одинаковых кадров
параметры использовал. Для обучения использовал параметры 50 эпох и 320 значений imgsz для максимального быстрого выполнения и получения начального результата
После обучения проверял результат командой model.predict() в итоге желтый суп вообще ни разу не был на видео никак размечен
Попробую разметить больше кадров с желтым супом и дообучать модель увеличив значение imgsz вдвое до 640 что распознать мелкие объекты. 
К сожалению желтый суп все еще не детектится. Поэтому попробую его разметитить в Label Studio более широко и повторю действия. Увеличу албументацию до 10. проходов.
Да это привелу к результату теперь все блюда на видео 2_1 отлично детектятся

