# TAGLINE

基于二进制空间分区的平铺式窗口管理器

# TLDR

使用配置文件**启动** bspwm

```bspwm -c [path/to/config]```

# SYNOPSIS

**bspwm** [_options_]

# DESCRIPTION

**bspwm** 是一个基于二进制空间分区的平铺式窗口管理器。它以完整二叉树的结构组织窗口，递归地将屏幕切分为多个区域。

该窗口管理器完全通过 **bspc** 控制，后者经由套接字发送命令。配置通过运行 bspc 命令的 shell 脚本完成，通常位于 **~/.config/bspwm/bspwmrc**。

快捷键绑定由 **sxhkd**（Simple X Hotkey Daemon）等工具单独处理。

# PARAMETERS

**-c** _config_
> 配置文件的路径（默认：~/.config/bspwm/bspwmrc）

**-s** _socket_
> 套接字文件的路径

**-o** _count_
> 显示器数量

# CONFIGURATION

**~/.config/bspwm/bspwmrc**
> 启动时执行的 shell 脚本，通过 bspc 命令配置 bspwm。

**~/.config/sxhkd/sxhkdrc**
> sxhkd 的快捷键配置，sxhkd 是配套的快捷键守护进程。

# CAVEATS

在其他窗口管理器运行时不得启动。需要单独的快捷键守护进程（sxhkd）来处理键盘快捷键。其配置是 shell 脚本，而非配置文件。

# HISTORY

**bspwm** 由 Bastien Dejean 创建，遵循"做好一件事"的 Unix 哲学。它将快捷键处理和状态栏显示交给独立的程序完成。

# INSTALL

```apt: sudo apt install bspwm```

```dnf: sudo dnf install bspwm```

```pacman: sudo pacman -S bspwm```

```apk: sudo apk add bspwm```

```zypper: sudo zypper install bspwm```

```nix: nix profile install nixpkgs#bspwm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bspc](/man/bspc)(1), [sxhkd](/man/sxhkd)(1), [polybar](/man/polybar)(1), [i3](/man/i3)(1)

# RESOURCES

```[Source code](https://github.com/baskerville/bspwm)```

<!-- verified: 2026-06-22 -->
