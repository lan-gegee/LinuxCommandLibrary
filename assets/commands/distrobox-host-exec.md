# TAGLINE

从 Distrobox 容器内部执行主机命令

# TLDR

在容器内**执行**主机上的命令

```distrobox-host-exec "[command]"```

在主机上执行 **ls**

```distrobox-host-exec ls```

# SYNOPSIS

**distrobox-host-exec** [_command_] [_arguments_]

# DESCRIPTION

**distrobox-host-exec** 从 Distrobox 容器内部在主机系统上执行命令。这可以访问容器内不可用的主机二进制文件和工具。

适用于在容器环境中运行主机特有的命令，如 flatpak、snap 或系统工具。

# PARAMETERS

_command_
> 要在主机上执行的命令

_arguments_
> 传给命令的参数

# CAVEATS

只能在 Distrobox 容器内使用。命令必须存在于主机系统上。容器与主机之间的环境变量可能不同。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-enter](/man/distrobox-enter)(1)

# RESOURCES

```[Source code](https://github.com/89luca89/distrobox)```

```[Homepage](https://distrobox.it/)```

<!-- verified: 2026-07-11 -->
