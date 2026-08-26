# TAGLINE

使用小型神经网络的智能 shell 历史搜索工具

# TLDR

**在 bash 中初始化 mcfly**

```eval "$(mcfly init bash)"```

**在 zsh 中初始化 mcfly**

```eval "$(mcfly init zsh)"```

**在 fish 中初始化 mcfly**

```mcfly init fish | source```

**按模式搜索历史**

```mcfly search [pattern]```

**向历史添加一条命令**

```mcfly add "[command]"```

**训练建议引擎**

```mcfly train```

# SYNOPSIS

**mcfly** _command_ [_options_]

# DESCRIPTION

**mcfly** 是一个用 Rust 编写的智能 shell 历史搜索工具，它利用小型神经网络根据上下文建议最可能的命令。它会考虑工作目录、最近的命令、退出状态和命令模式。

该工具取代 Ctrl+R，提供更智能的搜索，依据相关性而非单纯的时间先后对命令排序。历史记录存储在 SQLite 数据库中，删除后可以重建。

# PARAMETERS

**search** [_pattern_]
> 在历史中搜索匹配的命令。

**add** _command_
> 将命令添加到 mcfly 历史数据库。

**train**
> 训练神经网络建议引擎。

**move**
> 记录某目录已被移动。

**init** _shell_
> 输出 shell 初始化脚本（bash、zsh 或 fish）。

**--mcfly-history** _path_
> 添加或搜索时读取的 shell 历史文件。

**--session-id** _id_
> 用于记录或搜索的会话 ID。

**-d**, **--debug**
> 启用调试输出。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# CAVEATS

需要 shell 集成才能取代 Ctrl+R。神经网络需要时间学习使用模式；初始建议可能并不理想。SQLite 数据库会随使用增长。设置 **MCFLY_FUZZY**（整数，建议 2-5）可启用模糊匹配。设置 **MCFLY_RESULTS** 可控制显示的结果数量（默认：10）。设置 **MCFLY_HISTORY_LIMIT** 可限制搜索深度。

# HISTORY

**mcfly** 由 **Andrew Cantino** 创建，旨在为 shell 带来智能的命令建议。它运用机器学习原理提供具备上下文感知能力的历史搜索，超越了简单的文本匹配。

# INSTALL

```pacman: sudo pacman -S mcfly```

```apk: sudo apk add mcfly```

```zypper: sudo zypper install mcfly```

```brew: brew install mcfly```

```nix: nix profile install nixpkgs#mcfly```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hstr](/man/hstr)(1), [fzf](/man/fzf)(1), [atuin](/man/atuin)(1), [history](/man/history)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1)
