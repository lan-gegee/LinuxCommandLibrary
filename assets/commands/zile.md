# TAGLINE

轻量级 Emacs 克隆

# TLDR

**启动**编辑器

```zile```

**打开**文件

```zile [path/to/file]```

在指定**行**号打开

```zile +[line_number] [path/to/file]```

# SYNOPSIS

**zile** [_OPTIONS_] [_FILE..._]

# PARAMETERS

**+**_LINE_
> 在指定行号启动

**-q**
> 安静模式，抑制消息

**Ctrl+x Ctrl+s**
> 保存文件

**Ctrl+x Ctrl+c**
> 退出

**Ctrl+k**
> 删除（剪切）至行尾

**Ctrl+y**
> 粘贴（yank）被删除的文本

**Ctrl+x u**
> 撤销

**Ctrl+s**
> 向前增量搜索

**Ctrl+g**
> 取消当前命令

# DESCRIPTION

**zile** 是 Emacs 文本编辑器的轻量级克隆。它在更小更快的软件包中实现了 Emacs 的核心按键绑定和特性。

其名称是一个递归缩写："Zile Is Lossy Emacs"。它有意省略 Lisp 脚本等复杂的 Emacs 功能，同时保留熟悉的按键绑定。

# CAVEATS

缺少许多 Emacs 特性，如 Elisp 脚本、主模式/次模式和软件包管理。不是完整的 Emacs 替代品。

# INSTALL

```apt: sudo apt install zile```

```dnf: sudo dnf install zile```

```zypper: sudo zypper install zile```

```brew: brew install zile```

```nix: nix profile install nixpkgs#zile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emacs](/man/emacs)(1), [nano](/man/nano)(1), [mg](/man/mg)(1), [vi](/man/vi)(1), [ed](/man/ed)(1)
