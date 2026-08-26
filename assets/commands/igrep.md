# TAGLINE

带 TUI 的交互式 grep，可浏览搜索结果

# TLDR

在当前目录中**搜索模式**

```igrep "[pattern]"```

在指定目录中**搜索**

```igrep "[pattern]" [path/to/directory]```

不区分大小写地**搜索**

```igrep -i "[pattern]"```

**搜索隐藏文件**

```igrep --hidden "[pattern]"```

按文件类型**过滤**

```igrep -t [rust] "[pattern]"```

用指定的编辑器**打开结果**

```igrep --editor [nvim] "[pattern]"```

# SYNOPSIS

**igrep** [**-i**] [**--hidden**] [**-t** _type_] [**--editor** _editor_] _pattern_ [_path_]

# DESCRIPTION

**igrep**（Interactive Grep）在后台运行 **ripgrep**，并提供一个 TUI 来交互式浏览搜索结果。选中某个匹配后，它会用你选择的文本编辑器（默认 Vim）打开文件并定位到匹配行。支持的编辑器包括 Vim、Neovim、nano、VS Code、Emacs、Helix、Sublime Text、Micro 以及各种 JetBrains IDE。

该界面支持通过键盘快捷键对结果进行过滤、排序和导航，适合高效探索大型代码库。

# CAVEATS

需要 ripgrep（rg）作为搜索后端依赖。编辑器集成取决于编辑器是否支持行号参数。

# HISTORY

**igrep** 由 **konradsz** 开发，使用 **Rust** 编写。它的设计目的是弥补 grep 的搜索能力与编辑器集成之间的空隙，提供一个可视化的选择层。

# INSTALL

```apt: sudo apt install openimageio-tools```

```pacman: sudo pacman -S igrep```

```apk: sudo apk add openimageio-tools```

```zypper: sudo zypper install igrep```

```brew: brew install igrep```

```nix: nix profile install nixpkgs#igrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [rg](/man/rg)(1), [fzf](/man/fzf)(1)
