# TAGLINE

通过 SSH 转发远程 Wayland 应用

# TLDR

在本地运行**远程**程序

```waypipe ssh [user]@[server] [program]```

打开 SSH **隧道**

```waypipe ssh [user]@[server]```

跳过 **Vulkan** 测试

```waypipe --test-skip-vulkan ssh [user]@[server] [program]```

显示**帮助**

```waypipe -h```

# SYNOPSIS

**waypipe** [_OPTIONS_] ssh _HOST_ [_PROGRAM_]

# PARAMETERS

**--test-skip-vulkan**
> 跳过 Vulkan 支持测试

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**waypipe** 在远程运行图形化 Wayland 应用并在本地显示，类似于 X11 forwarding，但面向 Wayland 合成器。它通过 SSH 处理 Wayland 协议。

该工具创建一条透明隧道，使远程应用看起来就像本地原生窗口一样。

# CAVEATS

本地和远程系统都需要支持 Wayland。性能取决于网络延迟。某些应用在远程渲染下可能无法正常工作。

# INSTALL

```apt: sudo apt install waypipe```

```dnf: sudo dnf install waypipe```

```pacman: sudo pacman -S waypipe```

```apk: sudo apk add waypipe```

```zypper: sudo zypper install waypipe```

```nix: nix profile install nixpkgs#waypipe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1)
