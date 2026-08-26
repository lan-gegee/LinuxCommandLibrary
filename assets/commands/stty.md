# TAGLINE

显示并更改终端线路设置

# TLDR

**显示所有设置**

```stty -a```

**显示设备的设置**

```stty -a -F [/dev/ttyUSB0]```

**设置波特率**

```stty -F [/dev/ttyUSB0] [115200]```

**禁用回显**

```stty -echo```

**启用原始模式**

```stty raw```

**重置为合理默认值**

```stty sane```

**设置终端大小**

```stty rows [24] cols [80]```

# SYNOPSIS

**stty** [_options_] [_settings_...]

# DESCRIPTION

**stty** 显示或更改终端线路设置。它控制终端 I/O 的各个方面，包括波特率、字符处理和信号处理。

该工具对于配置串口和自定义终端行为至关重要。

# PARAMETERS

**-a**, **--all**
> 打印所有设置。

**-g**, **--save**
> 以 stty 可读的形式打印。

**-F** _device_, **--file**=_device_
> 打开并使用指定设备而不是 stdin。

**sane**
> 重置为合理值。

**raw**
> 原始模式（不做处理）。

**cooked**
> 常规模式（raw 的反义）。

**echo** / **-echo**
> 启用/禁用输入字符回显。

**rows** _n_
> 设置终端行数。

**cols** _n_
> 设置终端列数。

**ispeed** _n_
> 设置输入波特率。

**ospeed** _n_
> 设置输出波特率。

**ixon** / **-ixon**
> 启用/禁用 START/STOP 输出控制。

**ixoff** / **-ixoff**
> 启用/禁用 START/STOP 字符的发送。

**crtscts** / **-crtscts**
> 启用/禁用 RTS/CTS 硬件流控制。

**cstopb** / **-cstopb**
> 每字符使用两个停止位（加 '-' 则为一个）。

# CAVEATS

设置影响当前终端。某些设置需要相应权限。原始模式会禁用许多特性。更改可能不会持久保存。

# HISTORY

**stty**（set tty）是一款传统 Unix 实用程序，可追溯到早期 Unix 版本。它在串口通信和终端配置方面仍然不可或缺。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tty](/man/tty)(1), [setserial](/man/setserial)(8), [getty](/man/getty)(8), [reset](/man/reset)(1)
