# TAGLINE

终端文件管理器

# TLDR

**启动文件管理器**

```nnn```

**在指定目录中启动**

```nnn [/path/to/dir]```

**显示隐藏文件**

```nnn -H```

**详细模式**

```nnn -d```

**不使用颜色**

```nnn -c```

**用编辑器打开**

```nnn -e```

**带书签启动**

```nnn -b [bookmark-file]```

# SYNOPSIS

**nnn** [_options_] [_directory_]

# PARAMETERS

_DIRECTORY_
> 起始目录。

**-H**
> 显示隐藏文件。

**-d**
> 详细模式。

**-c**
> 无颜色。

**-e**
> 在编辑器中打开文本文件。

**-b** _FILE_
> 书签文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nnn** 是一个终端文件管理器。快速、极简、以键盘驱动。

该工具用于浏览目录。支持插件和文件操作。

# CAVEATS

以键盘为中心。类 Vim 的按键绑定。插件可扩展功能。

# HISTORY

nnn 创建之初就是一个**速度飞快**且资源占用低的终端文件管理器。

# INSTALL

```apt: sudo apt install nnn```

```dnf: sudo dnf install nnn```

```pacman: sudo pacman -S nnn```

```apk: sudo apk add nnn```

```zypper: sudo zypper install nnn```

```brew: brew install nnn```

```nix: nix profile install nixpkgs#nnn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [mc](/man/mc)(1), [lf](/man/lf)(1)
