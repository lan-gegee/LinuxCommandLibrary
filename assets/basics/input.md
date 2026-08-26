# 输入

## 入门
使用哪个工具取决于你的显示服务器：**xclip**、**xsel** 和 **xdotool** 用于 X11，而 **wl-copy**、**wtype** 用于 Wayland。**ydotool** 在两者上都能用，因为它在内核层面注入事件（需要 **ydotoold** 守护进程正在运行，且具备 root 或 uinput 权限）。
```[echo](/man/echo) $XDG_SESSION_TYPE```

## X11 上的剪贴板
将文件或命令输出复制到剪贴板，再粘贴出来。
```[xclip](/man/xclip) -sel clip [file]```
```[uname](/man/uname) -a | [xclip](/man/xclip) -sel clip```
```[xclip](/man/xclip) -o -sel clip```

**xsel** 做同样的工作，但选项略有不同。
```[xsel](/man/xsel) -b < [file]```
```[xsel](/man/xsel) -b```

X11 有两个剪贴板：常规剪贴板（**-sel clip**，用 Ctrl+V 粘贴）和主选择区（用鼠标中键粘贴）。

## Wayland 上的剪贴板
```[wl-copy](/man/wl-copy) "Hello world"```
```[uname](/man/uname) -a | [wl-copy](/man/wl-copy)```
```[wl-paste](/man/wl-paste)```

## 移动鼠标
移动到屏幕绝对位置，或相对于当前位置移动。
```[xdotool](/man/xdotool) mousemove [x] [y]```
```[xdotool](/man/xdotool) mousemove_relative [x] [y]```
```[ydotool](/man/ydotool) mousemove --absolute [x] [y]```
```[ydotool](/man/ydotool) mousemove [x] [y]```

## 点击
**xdotool** 用数字表示按键：1（左键）、2（中键）、3（右键）。**ydotool** 使用按键代码：**0xC0** 左键、**0xC1** 右键、**0xC2** 中键。
```[xdotool](/man/xdotool) click 1```
```[xdotool](/man/xdotool) click 3```
```[ydotool](/man/ydotool) click 0xC0```
```[ydotool](/man/ydotool) click 0xC1```

## 输入文本
```[xdotool](/man/xdotool) type "Hello world"```
```[ydotool](/man/ydotool) type "Hello world"```
```[wtype](/man/wtype) "Hello world"```

## 按键
**xdotool** 和 **wtype** 接受按键名称。**ydotool** 使用 Linux 键码，**:1** 表示按下、**:0** 表示释放，因此 Escape（键码 1）写作 **1:1 1:0**。
```[xdotool](/man/xdotool) key Escape```
```[xdotool](/man/xdotool) key ctrl+shift+t```
```[wtype](/man/wtype) -k Escape```
```[ydotool](/man/ydotool) key 1:1 1:0```

ydotool 的键码可在 /usr/include/linux/input-event-codes.h 中查找，例如 KEY_ENTER 是 28，KEY_LEFTALT 是 56。
