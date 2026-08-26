# TAGLINE

从图像创建 X 光标文件

# TLDR

从**配置**创建光标

```xcursorgen [path/to/config.cursor] [path/to/output_file]```

使用图像**前缀**创建

```xcursorgen --prefix [path/to/image_directory]/ [path/to/config.cursor] [path/to/output_file]```

写入 **stdout**

```xcursorgen [path/to/config.cursor]```

# SYNOPSIS

**xcursorgen** [_OPTIONS_] _CONFIG_ [_OUTPUT_]

# PARAMETERS

**--prefix** _PATH_
> 图像目录的路径

# DESCRIPTION

**xcursorgen** 从一组 PNG 图像创建 X 光标文件。配置文件指定图像尺寸、热点以及动画光标的帧延迟。

配置文件格式以尺寸、热点坐标、文件名和可选的延迟来定义每个光标帧。

# CAVEATS

图像必须为 PNG 格式。配置文件的格式比较特殊。不使用 --prefix 时，图像必须位于当前目录。

# INSTALL

```apt: sudo apt install x11-apps```

```dnf: sudo dnf install xcursorgen```

```apk: sudo apk add xcursorgen```

```zypper: sudo zypper install xcursorgen```

```brew: brew install xcursorgen```

```nix: nix profile install nixpkgs#xcursorgen```

<!-- packages: 2026-07-22 -->

# SEE ALSO
