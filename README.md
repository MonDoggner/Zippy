# Zippy
### Привет, программист! Тут я тебе о своём проекте и как им пользоваться. 

### -Что это вообще такое?
Zippy - это архиватор, использующий алгоритм Хаффмана. Школьный проект, который должен показать работу этого алгоритма.

### -Как это работает?
Смотри, всё очень просто. 
В репозитории лежит проект. Давай разберём, что входит в комплект:

-Zippy.py 
Тут у нас главный файл программы. Основа всего приложения.

-AppTools
Пакет, который я сделал для своего удобства. Без него ничего у тебя не запустится  
        
-Assets
Папка с картинками, иконками и всем, что сделает прогу красивее.

---

### -Zippy.py
В этом разделе я расскажу тебе что и как тут работает. Смотри, открываешь файлик и видишь импорты, сейчас поясню, что они делают.

```python
import AppTools #самописный пакет
import customtkinter
import os
import tempfile
import shutil
import time
from tkinter import *
from tkinter import filedialog
from PIL import Image
```
Как ты уже понял, AppTools сделал я, поэтому его разберём в следующем разделе.

Тут всё очень просто:

- tkinter и customtkinter для создания красивого интерфейса
- os, tempfile и shutil нам нужны для работы с файлами
- time мы будем использовать для загрузок
- PIL для работы с картинками

Дальше идёт стандартнное для customtkinter создание окна. Один момент, иконка указана немного необычно. Зачем? Ответ очень прост: когда ты соберёшь проект в .exe и будешь запускать его на разных компах эта фича позволит избежать ошибки. Она может возникнуть, если указать путь до иконки простым путём, ибо комп всегда будет искать её там, но скорее всего её там не будет. (Давай ещё разочек, но проще. Это ровно такой же путь, но универсальный. Ему пофиг, где ты будешь хранить иконку. Он её найдёт сам.)


Дальше у нас идут функции, думаю ты не совсем маслёнок и понимаешь что делают функции open_file и save_file, хотя обращу твоё внимание на последнюю. Если ты тыкал палочкой shutil, то знаешь, что он спокойно создаёт архивы самостоятельно, но тогда зачем там tempfile? Ответ: без него всё будет работать, НО в архиве у тебя будет хранится вообще вся инфа о репозитории, включая исходники, картинки и тп. (То есть, tempfile позволяет создавать архив только с выбранным тобой .txt)


Функции char_counter, counter_textbox_print и code_textbox_print. Отвечают за 2 поля, в которых визуализируется алгоритм Хаффмана. Тут без всяких хитростей, эти функции отвечают за подсчёт символов, вывод их кодировок. Другими словами, просто показывают пользователю информацию.

progress_bar, как не странно, создаёт полоску загрузки.

about создаёт окошко с информацией о приложении (нажми на кнопочку 3 раза, там сюприз)

Всё, что я не описал тут будет либо в разделе AppTools, либо взято из примеров customtkinter.

### -AppTools
Знаю ждали. Поздравляю, дождались! Тут я поясню за пакет, который ты видишь почти в каждой части кода.

Итак, зачем он? Ответ: это удобно. Читая эту документацию ты 100% заглядывал в customtkinter. Там ты точно успел заметить, что кнопки, лэйблы и прочие виджеты создаются отдельными объектами с длиннющими названиями, а потом ещё и размещаются отдельными функциями. 

Согласись звучит не очень удобно и громоздко. Поэтому я решил облегчить себе жизнь и сделать свои классы для создания и размещения некоторых виджетов. Объективно мы не дизайнеры и кнопки шлёпаем примерно одинаковые, так что открывай папку, сейчас всё разберём.

Файлик со словцом init не трогай, там просто инициализация пакета.

CustomTools.py содержит классы, которые создают кнопки и лэйблы, а также размещают их на указанных координатах. А так же на кнопки можно цеплять картинки.

Huffman.py - основа проекта. Тут лежит реализация жадного алгоритма со степика. По сути своей самый обычный алгоритм сжатия, детишкам такое на информатике рассказывают.

В этом же пакете будет появляться кэш, на него можешь забить, он никак не влияет на работу.

### Заключение

Что ж, я постарался максимально понятно и без лишней воды описать всё самое важное в проекте, поэтому предлагаю тебе просто запустить Zippy.py и посмотреть как же это работает на самом деле.  
