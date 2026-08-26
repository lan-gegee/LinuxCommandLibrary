# TAGLINE

类 Unix 系统的文本界面串口通信程序

# TLDR

打开**串口**

```sudo minicom -D /dev/ttyUSB0```

以指定**波特率**打开

```sudo minicom -D /dev/ttyUSB0 -b 115200```

打开**配置**菜单

```sudo minicom -D /dev/ttyUSB0 --setup```

将输出**捕获**到文件

```sudo minicom -D /dev/ttyUSB0 -C [path/to/file]```

显示**帮助**

```minicom --help```

# SYNOPSIS

**minicom** [_options_]

# DESCRIPTION

**minicom** 是类 Unix 系统上的文本界面串口通信程序。常用于与嵌入式设备、路由器及其他支持串口的硬件通信。

# PARAMETERS

**-D, --device DEVICE**
> 要打开的串口设备

**-b, --baudrate BAUD**
> 波特率（例如 9600、115200）

**-s, --setup**
> 进入配置菜单

**-C, --capturefile FILE**
> 将输出捕获到文件

**-o, --noinit**
> 跳过调制解调器初始化

**-w, --wrap**
> 启用自动换行

**-H, --displayhex**
> 以十六进制显示输出

**-S, --script SCRIPT**
> 启动时运行脚本

**-7, --7bit**
> 强制 7 位模式

**-8, --8bit**
> 强制 8 位模式

**-h, --help**
> 显示帮助信息

# KEYBOARD SHORTCUTS

**Ctrl+A X**: 退出 minicom
**Ctrl+A Z**: 帮助菜单
**Ctrl+A S**: 发送文件
**Ctrl+A L**: 切换日志捕获
**Ctrl+A O**: 配置 minicom
**Ctrl+A W**: 切换自动换行

# CAVEATS

需要 root 权限或属于 dialout 组。配置存储在 /etc/minicom/ 或 ~/.minirc.* 中。

# INSTALL

```apt: sudo apt install minicom```

```dnf: sudo dnf install minicom```

```pacman: sudo pacman -S minicom```

```apk: sudo apk add minicom```

```zypper: sudo zypper install minicom```

```brew: brew install minicom```

```nix: nix profile install nixpkgs#minicom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [picocom](/man/picocom)(1), [cu](/man/cu)(1)
