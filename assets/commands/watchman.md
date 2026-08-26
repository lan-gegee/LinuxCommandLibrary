# TAGLINE

面向大型代码库的文件监视服务

# TLDR

**监视某个目录**

```watchman watch [/path/to/dir]```

**列出正在监视的目录**

```watchman watch-list```

**停止监视某个目录**

```watchman watch-del [/path/to/dir]```

**获取监视状态**

```watchman watch-project [/path/to/project]```

**查找匹配模式的文件**

```watchman find [/path/to/dir] -p ["*.js"]```

**文件变化时触发命令**

```watchman -- trigger [/path/to/dir] [triggername] ["*.js"] -- [command]```

**关闭 watchman**

```watchman shutdown-server```

**检查版本**

```watchman version```

# SYNOPSIS

**watchman** _command_ [_options_] [_arguments_]

# PARAMETERS

**watch** _PATH_
> 开始监视目录。

**watch-del** _PATH_
> 停止监视目录。

**watch-list**
> 列出所有监视项。

**watch-project** _PATH_
> 监视项目根目录。

**find** _ROOT_ [_ARGS_]
> 查找符合条件的文件。

**query** _ROOT_ _EXPR_
> 用表达式查询文件。

**since** _ROOT_ _CLOCK_
> 查找自某个时钟以来发生变化的文件。

**trigger** _ROOT_ _NAME_ _PATTERN_ **--** _CMD_
> 设置触发命令。

**trigger-del** _ROOT_ _NAME_
> 移除触发器。

**trigger-list** _ROOT_
> 列出触发器。

**log-level** _LEVEL_
> 设置日志级别。

**get-config** _ROOT_
> 获取监视配置。

**shutdown-server**
> 停止 watchman 守护进程。

**version**
> 显示版本和能力。

# DESCRIPTION

**watchman** 是一个文件监视服务，它监视目录并在文件变化时触发操作。它是为需要高效文件变化检测的大型代码库设计的。

守护进程维护 inotify/FSEvents 监视并记录文件变化。客户端可以高效地查询变化——即使面对数百万个文件，查询也能在毫秒内返回。

触发器会在匹配的文件变化时执行命令，从而实现自动化测试、构建或同步。触发器可以按文件模式过滤，并使用模板化命令。

查询系统使用 JSON 表达式语言进行复杂的文件匹配。查询可以按名称、类型、大小、修改时间等条件过滤。结果包含文件元数据。

时钟值用于跟踪变更历史。订阅自某个时钟以来的变化可以实现增量处理——只处理新的变化而不是全量扫描。

Watchman 与构建工具（Buck、Bazel）、IDE 和测试框架集成。它为其他工具提供其构建所依赖的文件监视层。

# CAVEATS

必须运行守护进程才能进行监视。系统对被监视文件数量的限制可能需要调大。并非所有文件系统都支持高效监视。配置在重启后仍然保留。内存占用随文件数量增长。

# HISTORY

**watchman** 由 **Facebook**（Meta）开发，于 **2012 年**发布。它的设计初衷是应对 Facebook 庞大的代码库，仅靠 inotify 无法满足需求。该项目已成为众多需要高效文件变化检测的开发工具的基础设施。

# INSTALL

```brew: brew install watchman```

```nix: nix profile install nixpkgs#watchman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inotifywait](/man/inotifywait)(1), [entr](/man/entr)(1), [fswatch](/man/fswatch)(1)
