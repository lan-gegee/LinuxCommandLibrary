# TAGLINE

用 Rust 编写的快速模糊查找器

# TLDR

**启动 skim**，从输入中交互式选择条目

```sk```

**查找文件**并在编辑器中打开选中的文件

```sk | xargs [vim]```

**带预览窗口搜索**

```sk --preview '[cat {}]'```

**启用多选模式**（TAB 切换选中）

```sk -m```

**用作交互式命令过滤器**

```sk -i -c '[rg --color=always {}]'```

将命令输出**通过管道传给 skim**

```[ls -la] | sk```

**使用正则表达式搜索**而非模糊匹配

```sk --regex```

**生成 shell 补全脚本**

```sk --shell [bash]```

# SYNOPSIS

**sk** [_options_]

# PARAMETERS

**-m**
> 启用多选模式；按 TAB 可选中多个条目

**-i**
> 交互模式；随查询变化重新执行命令

**-c** _command_
> 要执行的命令；{} 会被替换为当前查询

**--ansi**
> 解析并显示输入中的 ANSI 颜色代码

**--regex**
> 使用正则表达式模式而非模糊匹配

**--preview** _command_
> 显示所选条目的预览；{} 会被替换为该条目

**--preview-window** _opts_
> 配置预览窗格（位置、大小、边框）

**--bind** _key:action_
> 将按键绑定到动作；多个绑定用逗号分隔

**--color** _scheme_
> 配色方案：dark、light、16、bw、none、molokai

**--tiebreak** _criteria_
> 排序依据：score、index、begin、end、length

**--shell** _shell_
> 为 bash、zsh、fish、powershell、elvish 生成补全

**-q**, **--query** _string_
> 以指定的初始查询字符串启动

**--height** _lines_
> 显示高度，以行数或百分比表示

**--reverse**
> 反转布局（提示符显示在顶部）

# DESCRIPTION

**sk**（skim）是一个用 Rust 编写的快速模糊查找器，可作为 fzf 的替代品。它提供交互式界面，用于从任意列表中过滤和选择条目，非常适合文件选择、命令历史搜索和进程管理等场景。

搜索语法支持 AND（空格分隔的词）、OR（用空格分隔的竖线）、精确匹配（前缀 **'**）和取反（前缀 **!**）。例如，**src main** 匹配同时包含两个词的条目，而 **.md$ | .markdown$** 匹配任一扩展名。

**-i** 标志启用交互模式，输入时 **-c** 指定的命令会随之重新执行。**--preview** 选项显示当前高亮条目的预览，适合查看文件内容或命令帮助。

skim 既可作为 Rust 库使用，也可作为独立二进制程序使用，便于集成到其他 Rust 应用中。

# CAVEATS

其模糊匹配算法与 fzf 不同，因此结果可能有所差异。部分按键绑定和标志的行为与 fzf 略有不同。输入集很大时，性能可能受可用内存影响。

# HISTORY

**skim** 由 **Jinzhou Zhang**（lotabout）创建，首次发布于 **2016 年**前后。它采用 **Rust** 编写，旨在成为比 fzf 更快、内存更安全的替代品，同时兼容 fzf 的多数特性。该项目目前由 skim-rs 社区积极维护。

# INSTALL

```pacman: sudo pacman -S skim```

```apk: sudo apk add skim```

```zypper: sudo zypper install skim```

```brew: brew install sk```

```nix: nix profile install nixpkgs#skim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [grep](/man/grep)(1), [find](/man/find)(1), [rg](/man/rg)(1), [fd](/man/fd)(1)
