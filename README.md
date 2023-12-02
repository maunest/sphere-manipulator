# Sphere Manipulator

![License](https://img.shields.io/badge/license-MIT-blue.svg) 
![Python Version](https://img.shields.io/badge/python-3.11.1-blue)
[![GitHub release](https://img.shields.io/github/release/maunest/sphere-manipulator.svg)](https://github.com/maunest/sphere-manipulator/releases)
![GitHub stars](https://img.shields.io/github/stars/maunest/sphere-manipulator)
[![Build and Test](https://github.com/maunest/sphere-manipulator/actions/workflows/app.yml/badge.svg?branch=main)](https://github.com/maunest/sphere-manipulator/actions/workflows/app.yml)
[![Buy me a beer](https://img.shields.io/badge/Buy%20me%20a-beer-orange)](https://i6.otzovik.com/2017/07/29/5190608/img/7789362.jpeg)
---
Sphere Manipulator - это приложение для манипулирования трехмерной сферой с использованием библиотеки OpenGL в языке программирования Python.

Приложение позволяет вам управлять положением, масштабом, цветом и освещением трехмерной сферы, используя клавиши на клавиатуре.


Приложение разработано по следующему заданию:
> 23. Напишите программу, позволяющую делать различные преобразования со сферой (перемещение, сжатие, 
> растяжение, изменение цвета, освещение и т. д.); управление действиями задается с клавиатуры.

## Демонстрация приложения

---
<img src="../sphere-manipulator/gif/gifDemo.gif" alt="Демонстрация">

## Как установить

---

```cmd
git clone https://github.com/maunest/sphere-manipulator.git
cd sphere-manipulator
pip install -r requirements.txt
```


## Как использовать

---
Открыть терминал в исходной папке проекта и выполнить следующую команду:
```cmd
python main.py
```

После запуска, вы увидите окно со сферой, используйте следующие клавиши для управления:

1) W, S, A, D: перемещение сферы по осям X и Y
2) Q, E: изменение масштаба сферы
3) R, G, B: изменение цвета сферы на красный, зеленый и синий соответственно
4) Стрелки: перемещение источника света

## Лицензия

---

Этот проект лицензирован в соответствии с условиями лицензии [MIT](LICENSE.md).


## Автор

---

- **maunest**
  - GitHub: [maunest](https://github.com/maunest)
  - Электронная почта: max.hairulov@mail.ru

