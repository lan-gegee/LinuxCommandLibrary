# TAGLINE

面向 stdin 行的模糊交互选择器

# TLDR

**选择一个文件**并打开它

```find . -type f | pick | xargs xdg-open```

从 shell 历史中**重新运行一条命令**

```eval $(fc -ln 1 | pick)```

从列表中**选择一行**

```printf '%s\n' [a b c] | pick```

# SYNOPSIS

**pick**

# DESCRIPTION

**pick** 从标准输入读取以换行分隔的选项，在终端中呈现一个交互式的模糊过滤器，并将选中的行写入标准输出。它专为 shell 管道和子 shell 设计：向它输入任意列表，用键盘选择一项，再把结果通过管道传给其他命令。

有 Vim 插件（**pick.vim**）以及适用于多种 Linux 发行版和 BSD 的软件包。主页：https://www.basename.se/pick/

# PARAMETERS

**pick** 通常不接收参数；配置通过终端交互完成（输入字符进行过滤、方向键/补全进行选择、Enter 确认）。按键绑定和编译期选项见已安装的手册页 **pick(1)**。

# CAVEATS

交互使用需要 TTY；没有终端的纯非交互式管道无法工作。输出是选中的单行（取消选择时的行为因版本而异——脚本中应检查退出状态）。

# INSTALL

```apt: sudo apt install pick```

```dnf: sudo dnf install pick```

```apk: sudo apk add mmh```

```brew: brew install pick```

```nix: nix profile install nixpkgs#pick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [fzy](/man/fzy)(1), [peco](/man/peco)(1), [selecta](/man/selecta)(1)

# RESOURCES

```[Source code](https://github.com/mptre/pick)```

```[Homepage](https://www.basename.se/pick/)```

<!-- verified: 2026-07-19 -->
