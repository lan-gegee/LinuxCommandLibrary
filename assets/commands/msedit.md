# TAGLINE

Microsoft 的终端文本编辑器

# TLDR

以空缓冲区**启动**编辑器

```msedit```

**打开**一个文件

```msedit [path/to/file]```

**打开**文件并定位到特定**行号**

```msedit [path/to/file]:[line]```

**打开**文件并定位到特定**行和列**

```msedit [path/to/file]:[line]:[column]```

在标签页中**打开多个文件**

```msedit [file1] [file2] [file3]```

# SYNOPSIS

**msedit** [_OPTIONS_] [_FILE_[:_LINE_[:_COLUMN_]]]...

# PARAMETERS

**-h**, **--help**
> 打印帮助信息

**-v**, **--version**
> 打印版本信息

# DESCRIPTION

**msedit** 是由 **Microsoft** 开发、用 **Rust** 编写的轻量级无模式终端文本编辑器。它的灵感来自经典的 MS-DOS Editor，但提供了现代化界面，输入控件与 VS Code 相似。与 Vim 这类模态编辑器不同，编辑即刻生效，无需切换模式。它具有菜单栏、状态栏、鼠标支持、UTF-8 处理、LF/CRLF 转换以及支持多语言的本地化界面。二进制文件不到 250 KB。

在 Linux 上，可执行文件名为 **msedit**，以避免与已有的 **edit** 命令冲突。在 Windows 上则直接叫 **edit**。

# KEYBOARD SHORTCUTS

```
Ctrl+S       Save file
Ctrl+Shift+S Save As
Ctrl+O       Open file
Ctrl+F       Find
Ctrl+R       Find & Replace
F3           Next search result
Ctrl+P       Switch between tabs
Ctrl+G       Go to line/column
Ctrl+Z       Undo
Ctrl+Y       Redo
Ctrl+C       Copy
Ctrl+V       Paste
Ctrl+Q       Quit
Ctrl+W       Close tab
Alt+Z        Toggle word wrap
Alt+F / F10  Focus menu bar
```

# CAVEATS

在 Linux 上，可执行文件名因安装方式而异：GitHub 二进制包为 **edit**，发行版软件包为 **msedit**。搜索和替换功能对 **ICU** 有可选依赖。从源码构建需要 **Rust nightly 工具链**。作为一款较新的工具（2025 年），它还缺少成熟编辑器所拥有的插件生态。

# HISTORY

Microsoft Edit 于 2025 年 5 月在 **Build 2025** 大会上公布，并以 **MIT 许可证**同步开源。它诞生的原因是 64 位 Windows 缺少默认的 CLI 文本编辑器。该项目已获得社区的高度关注，GitHub star 数超过 13,000。未来的 Windows 11 版本将预装此工具。

# INSTALL

```dnf: sudo dnf install msedit```

```pacman: sudo pacman -S msedit```

```zypper: sudo zypper install msedit```

```brew: brew install msedit```

```nix: nix profile install nixpkgs#msedit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [vim](/man/vim)(1), [emacs](/man/emacs)(1), [micro](/man/micro)(1)
