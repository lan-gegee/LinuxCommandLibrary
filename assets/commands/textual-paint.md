# TAGLINE

终端里的 MS Paint

# TLDR

**启动编辑器**

```textual-paint```

**打开 ANSI 艺术文件**

```textual-paint [drawing.ans]```

**以深色主题和纯 ASCII 模式启动**

```textual-paint --theme dark --ascii-only```

# SYNOPSIS

**textual-paint** [_options_] [_filename_]

# DESCRIPTION

**textual-paint** 是一款 TUI 图像编辑器，在终端中忠实重现经典的 MS Paint 体验。它包含所有 MS Paint 工具（铅笔、画笔、形状、文本、选择、填充、橡皮擦等），支持多种文件格式（ANSI、PNG、BMP、SVG、HTML），支持撤销/重做，并已本地化为 26 种语言。

# HISTORY

**textual-paint** 由 **Isaiah Odhner**（1j01）创建，使用 **Python** 基于 Textual 框架编写。

# INSTALL

```aur: yay -S textual-paint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chafa](/man/chafa)(1), [figlet](/man/figlet)(1)
