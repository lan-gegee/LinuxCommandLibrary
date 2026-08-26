# TAGLINE

打开终端并提示登录

# TLDR

把标准输入连接到某个**端口**，可选指定波特率

```agetty [tty] [115200]```

为登录设置**超时**

```agetty -t [timeout_in_seconds] -```

假定 tty 为 **8-bit clean** 并覆盖 TERM 变量

```agetty -8 - [term_var]```

跳过登录并调用**另一个登录程序**

```agetty -n -l [login_program] [tty]```

不显示**登录前 issue** 文件

```agetty -i -```

# SYNOPSIS

**agetty** [_options_] _port_ [_baud_rate_...] [_term_]

# DESCRIPTION

**agetty** 打开一个 tty 端口，提示输入登录名，然后调用 /bin/login 命令。它通常由 **init**(8) 调起。该命令提供了对固定接线和拨入连接都实用的功能，包括自动奇偶校验检测、从调制解调器消息推断波特率，以及可选的硬件流控。

# PARAMETERS

**-8, --8bits**
> 为 8-bit clean 终端禁用奇偶校验检测

**-a, --autologin username**
> 自动登录，不提示输入用户名

**-h, --flow-control**
> 启用 RTS/CTS 硬件流控

**-i, --noissue**
> 跳过显示 /etc/issue

**-J, --noclear**
> 在登录提示前不清屏

**-l, --login-program program**
> 使用替代的登录可执行程序

**-L, --local-line**
> 控制载波检测要求

**-m, --extract-baud**
> 从调制解调器状态消息中提取波特率

**-n, --skip-login**
> 不提示输入登录名

**-r, --chroot directory**
> 更改根目录

**-H, --host hostname**
> 向 utmp 文件写入指定的伪造主机名

**-t, --timeout seconds**
> 在超时时间内没有输入则终止

# CONFIGURATION

**/etc/issue**
> 登录提示之前显示的预登录消息。支持转义码来展示系统信息。

**/etc/os-release**
> 操作系统标识数据，agetty 用它来处理 /etc/issue 中的 \S 转义符。

# CAVEATS

波特率指终端与设备之间经串行链路传输数据的速度。串行终端默认为 9600。

# HISTORY

属于 **util-linux** 软件包。是传统 **getty** 命令的替代品，为现代 Linux 系统增加了更多功能。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add agetty```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[login](/man/login)(1), [init](/man/init)(8), [getty](/man/getty)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man8/agetty.8.html)```

<!-- verified: 2026-06-11 -->
