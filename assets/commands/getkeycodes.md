# TAGLINE

打印内核的扫描码到键码映射表

# TLDR

**显示键盘扫描码**

```getkeycodes```

# SYNOPSIS

**getkeycodes**

# PARAMETERS

**-V**, **--version**
> 打印版本号。

**-h**, **--help**
> 打印用法信息。

# DESCRIPTION

**getkeycodes** 显示内核的扫描码到键码映射表。它展示原始键盘扫描码如何被翻译成应用程序使用的键码。

输出内容为扫描码范围及其对应的键码。Linux 输入子系统使用这一映射来转换硬件按键动作。

getkeycodes 可用于调试键盘问题和理解键位映射。

# CAVEATS

需要访问 Linux 控制台（在 X11 或 Wayland 终端模拟器中无法工作）。输出格式紧凑，包含十六进制扫描码和十进制键码。只显示内核级映射，不包括 X11 或桌面键盘布局。

# HISTORY

getkeycodes 是 **kbd** 软件包的一部分，该软件包为 Linux 控制台管理提供键盘工具。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[showkey](/man/showkey)(1), [dumpkeys](/man/dumpkeys)(1), [loadkeys](/man/loadkeys)(1)
