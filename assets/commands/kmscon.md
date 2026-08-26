# TAGLINE

利用内核模式设置运行在 Linux 控制台上的终端模拟器

# TLDR

在第一个可用的 TTY 上**启动** kmscon

```sudo kmscon```

在**指定 TTY** 上启动

```sudo kmscon --vt [/dev/ttyX]```

启用**鼠标**支持

```sudo kmscon --mouse```

指定**登录命令**

```sudo kmscon -l [command]```

# SYNOPSIS

**kmscon** [_options_]

# PARAMETERS

**--vt** _TTY_
> 指定要使用的虚拟终端

**--mouse**
> 启用鼠标支持

**-l**, **--login** _COMMAND_
> 指定要执行的登录命令

**--font-name** _NAME_
> 设置使用的字体

**--font-size** _SIZE_
> 以磅为单位设置字号

# DESCRIPTION

**kmscon** 是一款使用内核模式设置（KMS）和帧缓冲运行在 Linux 控制台上的终端模拟器。它在 TTY 上提供现代终端体验，无需 X11。

与传统的文本模式 VT 不同，kmscon 使用 GPU 帧缓冲，使虚拟终端也能支持 Unicode、TrueType 字体和硬件加速渲染等特性。

# CAVEATS

需要图形驱动程序支持 KMS。可能与其他帧缓冲应用冲突。某些系统可能需要调整内核参数才能正常运行。

# HISTORY

kmscon 作为 systemd 项目的组成部分开发，旨在为 Linux VT 子系统提供现代化的替代品。它使用 libtsm 进行终端模拟，并采用类似 Wayland 的基础设施。

# INSTALL

```dnf: sudo dnf install kmscon```

```pacman: sudo pacman -S kmscon```

```zypper: sudo zypper install kmscon```

```nix: nix profile install nixpkgs#kmscon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getty](/man/getty)(8), [agetty](/man/agetty)(8)
