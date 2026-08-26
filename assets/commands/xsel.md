# TAGLINE

操作 X11 剪贴板选区

# TLDR

**复制**到剪贴板

```echo 123 | xsel -ib```

将**文件**复制到剪贴板

```cat [path/to/file] | xsel -ib```

**输出**剪贴板内容

```xsel -ob```

输出到**文件**

```xsel -ob > [path/to/file]```

**清空**剪贴板

```xsel -cb```

输出 **primary** 选区

```xsel -op```

# SYNOPSIS

**xsel** [_OPTIONS_]

# PARAMETERS

**-i, --input**
> 从 stdin 读取

**-o, --output**
> 写入 stdout

**-c, --clear**
> 清空选区

**-b, --clipboard**
> 使用剪贴板选区（Ctrl+C/V）

**-p, --primary**
> 使用 primary 选区（鼠标中键）

**-s, --secondary**
> 使用 secondary 选区

**-a, --append**
> 追加到选区

# DESCRIPTION

**xsel** 操作 X11 剪贴板和选区缓冲。它可以在 primary 选区、secondary 选区和剪贴板之间读取、写入、清空和交换内容。

类似于 xclip，但语法不同且有一些额外功能。

# CAVEATS

仅支持 X11。X server 重启后内容可能丢失。Wayland 请使用 wl-copy/wl-paste。

# INSTALL

```apt: sudo apt install xsel```

```dnf: sudo dnf install xsel```

```pacman: sudo pacman -S xsel```

```apk: sudo apk add xsel```

```zypper: sudo zypper install xsel```

```brew: brew install xsel```

```nix: nix profile install nixpkgs#xsel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xclip](/man/xclip)(1), [wl-copy](/man/wl-copy)(1), [wl-paste](/man/wl-paste)(1)
