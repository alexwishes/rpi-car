# 树莓派小车遥控器
-----
## Need

需要Flask、RPi.GPIO模块

## 变更
1. 增加PWM调速功能，页面上增加了slider实时控制车速
2. 分离wheel和car的代码，方便以后所有模块调用都通过同样的方式实现（传感器独立成类）

## 使用

1. 所有传感器模块放在module目录下
2. 在module/car.py下修改GPIO针脚号码（代码中使用的是TB6612FNG）
3. 启动程序

```python app.py```

## UI

![sample](https://github.com/fordoo/rpi-car/blob/master/sample.png?raw=true)
