# TAGLINE

阻止 Flatpak 应用程序更新

# TLDR

对某个 flatpak 设置**屏蔽**以忽略更新

```flatpak mask [com.example.app]```

**移除**屏蔽以恢复更新

```flatpak mask --remove [com.example.app]```

**列出**当前所有被屏蔽的模式（用户安装）

```flatpak mask --user```

**列出**当前所有被屏蔽的模式（系统安装）

```flatpak mask --system```

屏蔽来自**特定域名**的所有应用

```flatpak mask app/org.domain.*```

屏蔽应用的特定**分支**

```flatpak mask [com.example.app]//unstable```

# SYNOPSIS

**flatpak mask** [_options_] [_pattern..._]

# PARAMETERS

**--remove**
> 移除指定的屏蔽模式而不是添加

**-u, --user**
> 将屏蔽应用于按用户划分的安装

**--system**
> 将屏蔽应用于默认的系统级安装

**--installation** _name_
> 针对指定的命名系统安装

**-v, --verbose**
> 处理过程中输出调试信息

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**Flatpak mask** 用于阻止指定的应用程序或扩展被更新或自动安装。被屏蔽的 ref 永远不会收到更新，标记为自动下载的被屏蔽扩展也不会被下载。

模式支持使用 **\*** 通配符来匹配 ref 各段中的内容。你可以屏蔽特定应用、整个域名、特定架构的构建版本或特定分支。

不带模式运行该命令会列出指定安装（用户或系统）当前所有的屏蔽项。

# CAVEATS

屏蔽会阻止包括安全补丁在内的所有更新。请谨慎使用，并在希望恢复接收更新时记得解除屏蔽。用户安装和系统安装的屏蔽项是分开存储的。

# HISTORY

mask 功能加入 **Flatpak** 是为了让用户能够控制自动更新，特别适用于固定特定版本或避开有问题的版本。Flatpak 本身由 Red Hat 的 Alexander Larsson 开发，约在 **2015 年**从 xdg-app 项目演化而来。

# INSTALL

```apt: sudo apt install flatpak```

```dnf: sudo dnf install flatpak```

```pacman: sudo pacman -S flatpak```

```apk: sudo apk add flatpak```

```zypper: sudo zypper install flatpak```

```nix: nix profile install nixpkgs#flatpak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-update](/man/flatpak-update)(1), [flatpak-install](/man/flatpak-install)(1)

# RESOURCES

```[Homepage](https://flatpak.org/)```

```[Source code](https://github.com/flatpak/flatpak)```

<!-- verified: 2026-07-15 -->
