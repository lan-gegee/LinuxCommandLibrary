# TAGLINE

微型 GNU Emacs 风格编辑器

# TLDR

**打开文件**

```mg [file.txt]```

**在指定行打开文件**

```mg +[10] [file.txt]```

**以只读模式打开**

```mg -R [file.txt]```

**打开多个文件**（用 C-x b 切换）

```mg [file1.txt] [file2.txt]```

# SYNOPSIS

**mg** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要编辑的文件。

**+** _LINE_
> 从指定行号开始。

**-R**
> 只读（查看）模式。

**-n**
> 关闭备份文件的生成。

**-f** _mode_
> 启动时运行给定的模式（例如 -f auto-fill-mode）。

# DESCRIPTION

**mg** 是一个微型 GNU Emacs 风格编辑器。它以轻量的体积提供基本的 Emacs 按键绑定，非常适合在极简系统上进行快速编辑。

常用按键绑定：**C-x C-s**（保存）、**C-x C-c**（退出）、**C-x C-f**（打开文件）、**C-s**（增量搜索）、**C-x b**（切换缓冲区）、**C-x k**（关闭缓冲区）、**C-space**（设置标记）、**C-w**（剪切区域）、**M-w**（复制区域）、**C-y**（粘贴）、**C-x u**（撤销）。

mg 是 OpenBSD 的默认编辑器，也可在其他 BSD 和 Linux 系统上使用。

# CAVEATS

比 GNU Emacs 功能有限得多。不支持 Emacs Lisp 扩展、无语法高亮、不支持 Unicode。仅适合基本文本编辑。

# HISTORY

mg 最初名为 **MicroGNUEmacs**（后简化为 **mg**），由 Dave Conroy 于 **1986 年**为完整 GNU Emacs 过于庞大的系统而创建。此后由多位贡献者维护，现已成为 OpenBSD 基础系统的一部分。

# INSTALL

```apt: sudo apt install mg```

```dnf: sudo dnf install mg```

```pacman: sudo pacman -S mg```

```apk: sudo apk add mg```

```zypper: sudo zypper install mg```

```brew: brew install mg```

```nix: nix profile install nixpkgs#mg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emacs](/man/emacs)(1), [nano](/man/nano)(1), [vi](/man/vi)(1)
