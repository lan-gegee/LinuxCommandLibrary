# TAGLINE

与 EuroBraille Clio 终端交换文件

# TLDR

**启动**交互式文件传输会话

```eutp```

# SYNOPSIS

**eutp**

# DESCRIPTION

**eutp** 用于与 EuroBraille 的 Clio 终端交换文件。它是 **brltty** 盲文显示驱动软件包的一部分。

该程序完全交互且由菜单驱动：它会提示你选择传输方向（向终端发送文件或从终端接收文件）、文件类型以及要传输的文件。没有任何命令行选项。

接收文件时要小心 shell 特殊字符。\* 和 . 等通配符会被终端的文件匹配逻辑解释，因此要用单引号或反斜杠保护它们，避免出现意外结果。

# PARAMETERS

_无。_
> eutp 不接受任何命令行选项；所有交互均通过其菜单完成。

# CAVEATS

需要连接 EuroBraille Clio 终端。出错时返回 1。文件名中的特殊字符应加引号，以防被 shell 或终端展开。

# INSTALL

```apt: sudo apt install brltty```

```dnf: sudo dnf install brltty```

```pacman: sudo pacman -S brltty```

```apk: sudo apk add brltty```

```zypper: sudo zypper install brltty```

```nix: nix profile install nixpkgs#brltty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[brltty](/man/brltty)(1)

# RESOURCES

```[Source code](https://github.com/brltty/brltty)```

```[Homepage](https://brltty.app/)```

<!-- verified: 2026-07-15 -->
