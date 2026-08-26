# TAGLINE

极简的串口终端模拟器

# TLDR

**连接串口**

```picocom [/dev/ttyUSB0]```

**以指定波特率连接**

```picocom -b [115200] [/dev/ttyUSB0]```

**启用流控制连接**

```picocom -f h [/dev/ttyUSB0]```

**设置校验位连接**

```picocom -y e [/dev/ttyUSB0]```

**启用本地回显**

```picocom -c [/dev/ttyUSB0]```

**将会话记录到文件**

```picocom -g [log.txt] [/dev/ttyUSB0]```

# SYNOPSIS

**picocom** [_options_] _device_

# DESCRIPTION

**picocom** 是一个极简的串口终端模拟器。它提供与微控制器、路由器和嵌入式系统等串口设备的基本通信。

该工具注重简洁和可靠，适用于调试和配置串口设备。

# PARAMETERS

**-b**, **--baud** _baud_
> 波特率（默认 9600）。

**-f**, **--flow** _x|h|n_
> 流控制：x=xon/xoff（软件），h=硬件（RTS/CTS），n=无。

**-y**, **--parity** _e|o|n_
> 校验位：e=偶校验，o=奇校验，n=无。

**-d**, **--databits** _5-8_
> 数据位（5、6、7 或 8）。

**-p**, **--stopbits** _1|2_
> 停止位（1 或 2）。

**-e**, **--escape** _char_
> 转义字符（默认：a，即 C-a）。

**-c**, **--echo**
> 启用本地回显。

**-g**, **--logfile** _file_
> 将串口输入输出记录到文件。

**-t**, **--initstring** _str_
> 打开端口后发送初始化字符串。

**-i**, **--noinit**
> 启动时跳过端口初始化。

**-r**, **--noreset**
> 退出时不重置端口。

**-q**, **--quiet**
> 静默模式。

**-s**, **--send-cmd** _cmd_
> 用于发送文件的外部程序（默认：sz -vv）。

**-v**, **--receive-cmd** _cmd_
> 用于接收文件的外部程序（默认：rz -vv）。

# ESCAPE COMMANDS

默认转义前缀是 **C-a** (Ctrl-A)。

**C-a C-x**: 退出（重置端口）
**C-a C-q**: 退出（不重置）
**C-a C-h** / **C-a C-k**: 帮助
**C-a C-s**: 发送（上传）文件
**C-a C-r**: 接收（下载）文件
**C-a C-b**: 以交互方式设置波特率
**C-a C-u** / **C-a C-d**: 提高 / 降低波特率
**C-a C-f**: 循环切换流控制模式
**C-a C-y**: 循环切换校验位模式
**C-a C-i**: 循环切换数据位
**C-a C-j**: 循环切换停止位
**C-a C-v**: 显示当前端口设置
**C-a C-c**: 切换本地回显
**C-a C-\\**: 发送 break 信号

# CAVEATS

设备权限可能需要配置。硬件流控制需要正确的接线。应通过转义序列退出，而不是 Ctrl+C。

# HISTORY

**picocom** 由 **Nick Patavalis** 创建，作为 minicom 的极简替代品。它致力于为基础串口通信提供简单可靠的方案，避免完整终端模拟器的复杂性。

# INSTALL

```apt: sudo apt install picocom```

```dnf: sudo dnf install picocom```

```pacman: sudo pacman -S picocom```

```apk: sudo apk add picocom```

```zypper: sudo zypper install picocom```

```brew: brew install picocom```

```nix: nix profile install nixpkgs#picocom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[minicom](/man/minicom)(1), [screen](/man/screen)(1), [cu](/man/cu)(1), [microcom](/man/microcom)(1)
