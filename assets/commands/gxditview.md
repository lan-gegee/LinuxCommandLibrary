# TAGLINE

在 X11 窗口中显示 groff 输出

# TLDR

**查看 groff 文档**

```gxditview [file.roff]```

**指定页面尺寸**

```gxditview -page [a4] [file.roff]```

**从标准输入查看**

```groff -X [file.roff]```

**以指定分辨率查看**

```gxditview -resolution [100] [file.roff]```

# SYNOPSIS

**gxditview** [_options_] [_file_]

# PARAMETERS

_FILE_
> Groff 中间输出。

**-page** _SIZE_
> 页面尺寸（a4、letter）。

**-resolution** _DPI_
> 显示分辨率。

**-backingStore**
> 使用后备存储（backing store）。

**-help**
> 显示帮助信息。

# DESCRIPTION

**gxditview** 在 X11 窗口中显示 groff 输出。它可以在不打印的情况下在屏幕上预览排版后的文档。

该工具读取 groff 的中间输出格式并将其图形化渲染。它由 groff -X 调用，也可以直接读取 ditroff 输出。

# CAVEATS

属于 groff 软件包的一部分。需要 X11。界面较为陈旧。可能存在字体问题。

# HISTORY

gxditview 作为 **GNU groff** 的一部分开发而成，是一个 X11 预览器，派生自 X11 的 **xditview**。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [groffer](/man/groffer)(1)
