# TAGLINE

远程显示和控制 Android 设备

# TLDR

**镜像 Android 设备屏幕**

```scrcpy```

**镜像指定设备**（按序列号）

```scrcpy -s [SERIAL]```

**镜像的同时录制屏幕**

```scrcpy --record [file.mp4]```

**限制分辨率**

```scrcpy --max-size [1024]```

**限制帧率**

```scrcpy --max-fps [30]```

**无线连接**

```adb tcpip 5555 && adb connect [device_ip]:5555 && scrcpy```

**仅镜像不控制**（只读查看）

```scrcpy --no-control```

**镜像时关闭设备屏幕**

```scrcpy --turn-screen-off```

# SYNOPSIS

**scrcpy** [_-s serial_] [_--record file_] [_--max-size px_] [_--max-fps fps_] [_options_]

# PARAMETERS

**-s** _SERIAL_, **--serial** _SERIAL_
> 设备序列号。

**--max-size**, **-m** _SIZE_
> 限制分辨率（较短边）。

**--max-fps** _FPS_
> 限制帧率。

**-r**, **--record** _FILE_
> 录制到文件（mp4/mkv）。

**-b** _RATE_, **--video-bit-rate** _RATE_
> 视频码率（默认：8M）。旧版本使用 **--bit-rate**。

**-n**, **--no-control**
> 禁用控制（仅镜像）。

**-N**, **--no-playback**
> 禁用在电脑上的回放（适合无头录制）。旧名为 **--no-display**。

**--show-touches**
> 在设备上显示物理触点。

**-S**, **--turn-screen-off**
> 镜像时关闭设备屏幕。

**-w**, **--stay-awake**
> 设备接入电源时保持唤醒。

**--window-title** _TITLE_
> 自定义窗口标题。

**--window-x** _X_
> 窗口 X 坐标。

**--window-y** _Y_
> 窗口 Y 坐标。

**--window-width** _W_
> 窗口宽度。

**--window-height** _H_
> 窗口高度。

**--fullscreen**, **-f**
> 全屏启动。

**--always-on-top**
> 保持窗口置顶。

**--crop** _W:H:X:Y_
> 裁剪屏幕区域。

**--no-audio**
> 禁用音频转发。

# DESCRIPTION

**scrcpy**（screen copy）可在桌面上显示和控制 Android 设备。它以低延迟镜像设备屏幕，支持通过鼠标和键盘进行交互。

连接可通过 USB 或 WiFi。USB 性能最佳；WiFi 支持无线使用。该工具使用 ADB 通信，并向设备推送自定义 server。

控制功能包括触摸模拟、键盘输入、剪贴板同步以及设备按键（电源、音量、返回）。借助鼠标加键盘修饰键可以模拟多点触控。

录屏功能将镜像的屏幕捕获为 MP4 或 MKV，没有音频开销。结合 --no-display 可实现无头录制。

息屏模式在桌面显示画面的同时保持设备屏幕关闭，有助于省电。保持唤醒可防止镜像期间设备休眠。

窗口管理选项控制窗口的位置和行为。全屏和置顶模式适用于不同的工作流程。

# CAVEATS

需要 ADB 并启用 USB 调试。音频转发需要 Android 11 及以上。某些应用会阻止屏幕捕获。无线模式需要先用 USB 完成初始设置。高分辨率/高帧率会增加延迟。并非所有快捷键在所有应用中都有效。

# HISTORY

**scrcpy** 由 **Genymobile** 的 **Romain Vimont**（rom1v）于 **2018 年**前后创建。它是 Android 模拟器和厂商专用投屏工具的轻量替代品。项目使用 C 和 SDL 编写，注重性能与简洁。这是一个开源且持续活跃维护的项目。

# INSTALL

```pacman: sudo pacman -S scrcpy```

```apk: sudo apk add scrcpy```

```zypper: sudo zypper install scrcpy```

```brew: brew install scrcpy```

```nix: nix profile install nixpkgs#scrcpy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adb](/man/adb)(1), [sndcpy](/man/sndcpy)(1), [ffmpeg](/man/ffmpeg)(1)
