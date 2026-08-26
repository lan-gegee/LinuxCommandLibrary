# TAGLINE

显示键盘按键码和扫描码

# TLDR

以十进制**查看**按键码

```sudo showkey```

以十六进制**显示**扫描码

```sudo showkey -s```

以十进制**显示**按键码

```sudo showkey -k```

以 ASCII、十进制和十六进制**显示**按键码

```sudo showkey -a```

# SYNOPSIS

**showkey** [_options_]

# PARAMETERS

**-s**, **--scancodes**
> 以十六进制显示扫描码。

**-k**, **--keycodes**
> 以十进制显示按键码（默认模式）。

**-a**, **--ascii**
> 以 ASCII、十进制和十六进制显示键值。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 打印版本号并退出。

# DESCRIPTION

**showkey** 将每个按下按键的扫描码、按键码或 ASCII 码打印到标准输出。这对于调试键盘相关问题、重映射按键以及从底层理解键盘输入很有帮助。

在扫描码和按键码模式下，程序会一直运行，直到距最后一次按键或松开事件过去 10 秒。在 ASCII 模式下，用户输入 Ctrl+D 时程序终止。

# CAVEATS

必须以 root 身份或通过 sudo 运行。只能在 Linux 控制台上工作，不能用于 X11 或 Wayland 下的终端模拟器。运行期间键盘无法用于正常输入。

# HISTORY

**showkey** 是 **kbd**（keyboard tools）软件包的一部分，属于 Linux 控制台实用工具。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```brew: brew install showkey```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[loadkeys](/man/loadkeys)(1), [dumpkeys](/man/dumpkeys)(1), [getkeycodes](/man/getkeycodes)(1), [xmodmap](/man/xmodmap)(1)
