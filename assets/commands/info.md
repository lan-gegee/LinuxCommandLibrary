# TAGLINE

阅读 GNU texinfo 格式的文档

# TLDR

**阅读命令的手册**

```info [command]```

**从顶层目录开始**

```info```

**跳转到指定节点**

```info -n "[node_name]" [command]```

**在手册中搜索**

```info --apropos=[keyword]```

**输出到标准输出**

```info -o - [command]```

**使用指定的文件**

```info -f [file.info]```

# SYNOPSIS

**info** [_options_] [_menu-item_...]

# PARAMETERS

_MENU-ITEM_
> 要显示的手册页或节点。

**-f** _FILE_
> 读取指定的 info 文件。

**-n** _NODE_
> 从指定节点开始。

**-o** _FILE_
> 输出到文件（- 表示标准输出）。

**--apropos** _STRING_
> 在所有手册中搜索字符串。

**-w**, **--where**
> 打印 info 文件的位置。

**--all**
> 使用所有匹配的手册。

**--subnodes**
> 递归输出菜单项。

**-k** _STRING_, **--index-search** _STRING_
> 在所有手册的所有索引中查找 STRING。

**--help**
> 显示帮助信息。

# DESCRIPTION

**info** 读取 GNU texinfo 格式的文档。它以超文本方式浏览按树状节点组织的结构化文档。

该阅读器支持在节点、菜单和交叉引用之间导航。常用导航键：**n**（下一个节点）、**p**（上一个节点）、**u**（上一层）、**l**（上次访问的节点）、**q**（退出）、**/** 或 **s**（搜索）、**Tab**（下一个链接）、**Enter**（跟随链接）。

# CAVEATS

并非所有软件都有 info 页面。导航键与 man 不同。默认使用 Emacs 风格的键绑定。**--apropos** 搜索可能较慢，因为它要扫描所有 info 文件。

# HISTORY

info 是 **GNU 项目**的一部分，旨在提供比 man page 更丰富的文档，支持超文本特性。

# INSTALL

```apt: sudo apt install info```

```dnf: sudo dnf install info```

```pacman: sudo pacman -S texinfo```

```apk: sudo apk add texinfo```

```zypper: sudo zypper install info```

```brew: brew install texinfo```

```nix: nix profile install nixpkgs#texinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1)
