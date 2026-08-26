# TAGLINE

带上下文、可同步查询的 Shell 历史记录工具

# TLDR

**安装并启用** hishtory

```hishtory install```

**查询 shell 历史**

```hishtory query [search_term]```

**启用 Control+R 集成**

```hishtory config-set enable-control-r true```

**借助 AI 搜索**（以 ? 为前缀）

```hishtory query ?[how to find large files]```

**导出全部历史条目**

```hishtory export```

**显示同步与配置状态**

```hishtory status```

**删除匹配查询的历史条目**

```hishtory redact [search_term]```

**暂时停用记录功能**

```hishtory disable```

# SYNOPSIS

**hishtory** _command_ [_options_] [_arguments_]

# DESCRIPTION

**hishtory** 是一个 shell 历史记录工具，它用一个可同步、可查询且带上下文的方案取代默认的历史记录。它会挂接到你的 shell 以跟踪所有运行过的命令，并将它们连同工作目录、退出码和耗时等附加上下文一起保存到本地 **SQLite** 数据库中。

历史记录使用 AES-GCM 进行**端到端加密**，可以在你的所有设备之间同步。当你按下 **Control+R** 或运行 **hishtory query** 时，一条 SQL 查询会在本地数据库中找到匹配的条目。查询也可以加上 **?** 前缀，借助 ChatGPT 进行自然语言命令搜索。

# PARAMETERS

**install**
> 安装并配置 hishtory

**query** _term_
> 搜索 shell 历史

**export**
> 导出全部历史条目

**status**
> 显示同步与配置状态

**config-set** _key_ _value_
> 设置某个配置项

**config-get** _key_
> 获取某个配置值

**redact** _query_
> 在本地及所有已同步设备上删除匹配的历史条目。

**update**
> 安全地下载并应用最新的 hishtory 更新。

**disable**
> 暂时停止记录 shell 历史。

**enable**
> 恢复记录 shell 历史。

# CAVEATS

需要有活动的 shell 会话才能记录命令。跨设备同步需要互联网连接。AI 搜索功能需要 ChatGPT API 连接。端到端加密意味着加密密钥一旦丢失，数据将无法恢复。按照 shell 的惯例，以空格开头的命令不会被记录。

# HISTORY

**hishtory** 由 **David Dworken** 创建，使用 **Go** 编写。其设计目标是通过增加加密、跨设备同步和上下文元数据，弥补内置 shell 历史功能的不足。

# INSTALL

```brew: brew install hishtory```

```nix: nix profile install nixpkgs#hishtory```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[history](/man/history)(1), [atuin](/man/atuin)(1), [fzf](/man/fzf)(1)
