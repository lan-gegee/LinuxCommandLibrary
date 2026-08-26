# TAGLINE

构建共享的 MIME-Info 数据库缓存

# TLDR

**更新系统 MIME 数据库**

```sudo update-mime-database /usr/share/mime```

**更新用户 MIME 数据库**

```update-mime-database ~/.local/share/mime```

**显示版本**

```update-mime-database -v```

**显示帮助**

```update-mime-database -h```

# SYNOPSIS

**update-mime-database** [_options_] _mime-dir_

# PARAMETERS

**-h**
> 显示帮助并退出。

**-v**
> 显示版本并退出。

**-V**
> 处理过程中输出详细信息。

**-n**
> 仅当文件发生变化时才更新。

# DESCRIPTION

**update-mime-database** 根据 XML 源文件构建共享 MIME-Info 数据库缓存。它扫描指定目录中的 MIME 类型定义，并将它们编译成经过优化的二进制缓存（mime.cache），供应用程序快速访问。

该数据库把文件模式、magic 字节等特征映射到 MIME 类型，让应用能够正确识别文件类型。系统级定义位于 /usr/share/mime，而用户自定义内容则放在 ~/.local/share/mime。

软件包管理器通常会在安装提供新 MIME 类型定义的软件时自动运行此命令。添加自定义 MIME 类型时才需要手动执行。

# DIRECTORIES

**/usr/share/mime**: 系统级 MIME 数据库。

**/usr/share/mime/packages/**: MIME 类型的源 XML 文件。

**~/.local/share/mime**: 用户专属的 MIME 数据库。

# CAVEATS

需要对目标目录的写权限。更新系统目录需要 root 权限。应用程序可能需要重启才能识别新类型。属于 shared-mime-info 软件包的一部分。

# HISTORY

**update-mime-database** 属于 freedesktop.org 的 shared-mime-info 项目，该项目旨在统一各 Linux 桌面环境的 MIME 类型处理方式。在此之前，GNOME 与 KDE 各自维护着互不兼容的 MIME 数据库。

# INSTALL

```apt: sudo apt install shared-mime-info```

```dnf: sudo dnf install shared-mime-info```

```pacman: sudo pacman -S shared-mime-info```

```apk: sudo apk add shared-mime-info```

```zypper: sudo zypper install shared-mime-info```

```brew: brew install shared-mime-info```

```nix: nix profile install nixpkgs#shared-mime-info```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-mime](/man/xdg-mime)(1), [file](/man/file)(1), [mimetype](/man/mimetype)(1)
