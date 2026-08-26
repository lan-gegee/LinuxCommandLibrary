# TAGLINE

基于终端的 Markdown 幻灯片演示工具

# TLDR

**开始演示**

```presenterm [presentation.md]```

**使用指定主题演示**

```presenterm --theme [dark] [presentation.md]```

**导出为 PDF**

```presenterm --export-pdf [presentation.md]```

**实时重载模式**

```presenterm --watch [presentation.md]```

# SYNOPSIS

**presenterm** [_options_] _file_

# PARAMETERS

_FILE_
> Markdown 演示文件。

**--theme** _NAME_
> 演示主题。

**--export-pdf**
> 导出为 PDF。

**--watch**
> 文件更改时自动重载。

**-e**, **--execute**
> 启用代码执行。

# DESCRIPTION

**presenterm** 是一个基于终端的演示工具，可直接在终端中将 Markdown 文件渲染为幻灯片。幻灯片在 Markdown 源文件中由水平分隔线分隔；该工具支持语法高亮的代码块、图片（在支持的终端中）以及多个内置主题。

监视模式会在源文件变化时自动重载演示，实现实时编辑工作流。幻灯片还可以导出为 PDF，以便在终端之外分享。

# CAVEATS

仅限终端。必须使用 Markdown 格式。

# HISTORY

presenterm 为 **基于终端的** Markdown 演示而创建。

# INSTALL

```pacman: sudo pacman -S presenterm```

```zypper: sudo zypper install presenterm```

```brew: brew install presenterm```

```nix: nix profile install nixpkgs#presenterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdp](/man/mdp)(1), [slides](/man/slides)(1)
