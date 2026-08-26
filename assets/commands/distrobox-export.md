# TAGLINE

将容器中的应用和二进制文件导出到主机系统

# TLDR

向主机**导出一个应用**

```distrobox-export --app [mpv]```

**导出一个应用**并附加启动标志

```distrobox-export --app [atom] --extra-flags "--foreground"```

**导出一个二进制文件**到 ~/.local/bin

```distrobox-export --bin [/usr/bin/vim] --export-path [~/.local/bin]```

**列出**此容器已导出的应用

```distrobox-export --list-apps```

**删除**一个已导出的应用

```distrobox-export --app [atom] --delete```

# SYNOPSIS

**distrobox-export** [_options_]

# DESCRIPTION

**distrobox-export** 将应用或二进制文件从 Distrobox 容器导出到主机系统。导出的应用会出现在主机的应用菜单中，导出的二进制文件通过一个小包装脚本在主机上可用，该脚本会在容器内运行它们。

请在容器内部运行此命令。**--app** 和 **--bin** 只能二选一，不可同时使用。

# PARAMETERS

**-a, --app** _app_
> 按名称或 .desktop 文件的绝对路径导出应用（创建桌面条目）

**-b, --bin** _binary_
> 按其在容器内的绝对路径导出二进制文件

**--list-apps**
> 列出此容器已导出的应用

**--list-binaries**
> 列出此容器已导出的二进制文件

**-ep, --export-path** _path_
> 导出的二进制文件的目标路径（如 ~/.local/bin）

**-el, --export-label** _label_
> 附加到导出的应用名称上的标签（默认为 "(on _container_)"；用 "none" 禁用）

**-ef, --extra-flags** _flags_
> 运行导出项时传给命令的额外标志

**-nf, --enter-flags** _flags_
> 传递给底层 `distrobox enter` 的额外标志

**-S, --sudo**
> 在容器内以 root 身份运行导出项

**-d, --delete**
> 取消导出指定的应用或二进制文件

# CAVEATS

必须在容器内运行。导出的应用依赖于容器的存在（启动时会自动开启容器）。删除容器会使已导出的应用和二进制文件失效。

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
