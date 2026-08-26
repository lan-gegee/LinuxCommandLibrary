# TAGLINE

停止运行中的 Distrobox 容器

# TLDR

**停止**一个容器

```distrobox-stop [container_name]```

**无需确认**停止

```distrobox-stop -n [container_name] -Y```

# SYNOPSIS

**distrobox-stop** [_options_] [_name_]

# DESCRIPTION

**distrobox-stop** 停止一个运行中的 Distrobox 容器。默认在停止前会请求确认。

已停止的容器会保留其状态，可以重新启动。

# PARAMETERS

**-n, --name** _name_
> 容器名称

**-Y, --yes**
> 跳过确认提示

# CAVEATS

停止容器会终止其中所有正在运行的进程。导出的应用在容器重启前将无法使用。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-enter](/man/distrobox-enter)(1), [distrobox-rm](/man/distrobox-rm)(1)

# RESOURCES

```[Source code](https://github.com/89luca89/distrobox)```

```[Homepage](https://distrobox.it/)```

<!-- verified: 2026-07-11 -->
