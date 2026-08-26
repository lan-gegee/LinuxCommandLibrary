# TAGLINE

X11 剪贴板命令行接口

# TLDR

复制输出到 **primary selection**

```echo 123 | xclip```

复制到**系统剪贴板**

```echo 123 | xclip -selection clipboard```

复制**文件内容**到剪贴板

```xclip -selection clipboard input.txt```

复制**图像**到剪贴板

```xclip -selection clipboard -target image/png image.png```

从**用户输入**复制

```xclip -i```

从 primary selection **粘贴**

```xclip -o```

从剪贴板**粘贴**

```xclip -o -selection clipboard```

# SYNOPSIS

**xclip** [_-i_|_-o_] [_-selection sel_] [_-target type_] [_file_...]

# DESCRIPTION

**xclip** 是一款 X11 剪贴板操作工具。它可以从标准输入或文件读取数据并写入任意 X selection（primary、secondary 或 clipboard），或者将 selection 的内容输出到 stdout。

# PARAMETERS

**-i, -in**
> 从 stdin 或文件读取（默认模式）

**-o, -out**
> 将 selection 写到 stdout

**-se, -selection SELECTION**
> 指定 selection：primary、secondary 或 clipboard

**-t, -target TYPE**
> 指定 MIME 目标类型（如 image/png、text/html）

**-d, -display DISPLAY**
> 要连接的 X display

**-l, -loops N**
> 退出前服务的粘贴请求数量

**-f, -filter**
> 复制的同时将输入打印到 stdout

**-q, -quiet**
> 抑制提示性输出

**-v, -verbose**
> 打印额外信息

**-silent**
> 转入后台运行（与 -loops 配合使用）

# X11 SELECTIONS

**primary**：中键粘贴（高亮即复制）
**secondary**：很少使用的次级 selection
**clipboard**：Ctrl+C/Ctrl+V 剪贴板

# CAVEATS

数据仅在 xclip 运行期间可用（除非使用 -loops 或 -silent）。要持久保存剪贴板内容，请使用剪贴板管理器。默认 selection 是 primary 而不是 clipboard。

# HISTORY

**xclip** 由 Kim Saunders 编写，是 X11 selections 的命令行接口。它提供可脚本化的剪贴板访问能力，而不依赖 GUI。

# INSTALL

```apt: sudo apt install xclip```

```dnf: sudo dnf install xclip```

```pacman: sudo pacman -S xclip```

```apk: sudo apk add xclip```

```zypper: sudo zypper install xclip```

```brew: brew install xclip```

```nix: nix profile install nixpkgs#xclip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsel](/man/xsel)(1), [wl-copy](/man/wl-copy)(1), [wl-paste](/man/wl-paste)(1)
