# TAGLINE

命令行交互式速查表工具

# TLDR

**浏览**所有可用的速查表

```navi```

浏览 **navi 自身的速查表**

```navi fn welcome```

**打印**命令而不执行

```navi --print```

输出 **shell 小部件**源代码

```navi widget [bash|zsh|fish]```

为查询**自动选择**最佳匹配项

```navi -q '[query]' --best-match```

**添加**新的速查表仓库

```navi repo add [url]```

# SYNOPSIS

**navi** [**--print**] [**--query** _query_] [**--best-match**] [_command_]

# PARAMETERS

**--print**
> 打印所选命令而不执行

**-q, --query _query_**
> 按查询字符串过滤速查表

**--best-match**
> 自动选择最匹配的片段

**--path _path_**
> 使用指定的速查表路径

**--fzf-overrides _opts_**
> 覆盖 fzf 选项

# COMMANDS

**fn welcome**
> 显示 navi 自带的速查表

**widget _shell_**
> 输出用于集成的 shell 小部件代码

**repo add _url_**
> 添加速查表仓库

**repo browse**
> 浏览可用仓库

**info cheats-path**
> 显示速查表目录路径

# DESCRIPTION

**navi** 是一个命令行交互式速查表工具。它支持按分类浏览命令片段，具备模糊搜索、变量替换和直接执行功能。

速查表以特定格式的纯文本文件存储。该工具与 shell 快捷键集成（默认 Ctrl+G）以便快速访问。自定义速查表可以在本地添加，也可以来自社区仓库。

# CAVEATS

需要 fzf 提供模糊查找界面。安装 shell 小部件需要在 shell 配置中添加 source 命令。速查表使用特定的变量占位符语法。

# HISTORY

**navi** 由 **Denis Isidoro** 创建，是传统速查表工具的现代替代品。它强调交互性、模糊搜索和社区贡献的速查表。使用 Rust 编写以保证性能。

# INSTALL

```dnf: sudo dnf install navi```

```pacman: sudo pacman -S navi```

```apk: sudo apk add navi```

```brew: brew install navi```

```nix: nix profile install nixpkgs#navi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tldr](/man/tldr)(1), [cheat](/man/cheat)(1), [fzf](/man/fzf)(1)
