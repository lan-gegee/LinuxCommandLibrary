# TAGLINE

仿 man page 风格的 Markdown 查看器

# TLDR

**查看 Markdown 文件**

```mdn [path/to/file.md]```

# SYNOPSIS

**mdn** [_options_] _file_

# DESCRIPTION

**mandown**（命令名：**mdn**）是一个终端中使用的、仿 man page 风格的 Markdown 查看器。它以熟悉的 man page 风格界面渲染 Markdown 文档，支持鼠标滚动以及类似 vim 和 less 的导航键位。

导航按键包括：用 **j**/**k** 或方向键逐行滚动，用 **f**/**b** 或 Page Down/Page Up 逐页滚动，按 **q** 退出。

# CONFIGURATION

**~/.config/mdn/mdnrc**
> 配置文件，可设置鼠标支持、缩进长度和控制方案（mdn、vim、less）。

# CAVEATS

编译时依赖 libncurses(w)、libxml2 和 libconfig。

# HISTORY

**mandown** 由 **Titor8115** 创建，使用 **C** 语言编写。

# INSTALL

```pacman: sudo pacman -S mandown```

```apk: sudo apk add mandown```

```zypper: sudo zypper install mandown```

```brew: brew install mandown```

```nix: nix profile install nixpkgs#mandown```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [glow](/man/glow)(1), [mdcat](/man/mdcat)(1), [bat](/man/bat)(1)
