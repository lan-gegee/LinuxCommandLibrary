# TAGLINE

用于快速增量类型检查的 mypy 守护进程

# TLDR

**启动 mypy 守护进程**

```dmypy start```

**通过守护进程运行类型检查**

```dmypy run [file.py]```

**检查整个项目**

```dmypy run -- --strict [.]```

**停止守护进程**

```dmypy stop```

**检查守护进程状态**

```dmypy status```

**重启守护进程**

```dmypy restart```

**强制终止守护进程**

```dmypy kill```

# SYNOPSIS

**dmypy** _command_ [_options_] [_files_...]

# PARAMETERS

_COMMAND_
> 操作类型：start、stop、run、status、restart、kill。

**start**
> 启动 mypy 守护进程。

**stop**
> 平滑地停止守护进程。

**run** [_FILES_]
> 通过守护进程对文件做类型检查。

**status**
> 显示守护进程状态。

**restart**
> 重启守护进程。

**kill**
> 强制终止守护进程。

**--status-file** _FILE_
> 自定义状态文件位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dmypy** 是 mypy（Python 静态类型检查器）的守护进程接口。它让 mypy 作为后台进程持续运行，通过在多次运行之间维护缓存状态来大幅缩短类型检查时间。

守护进程会预先计算并缓存类型信息，使增量检查几乎瞬时完成。这对大型代码库尤其有价值——完整的 mypy 检查在这种场景下会很慢。

dmypy 可集成到需要频繁执行快速类型检查的编辑器和 CI 系统中。它负责守护进程的生命周期管理，并将类型检查请求转发给正在运行的 mypy 实例。

# CAVEATS

配置变更后必须重启守护进程。内存占用随项目规模增长。mypy 版本变化时可能需要重启。不适合并行类型检查。

# HISTORY

dmypy 作为 **mypy** 的组成部分推出，mypy 最初由 **Jukka Lehtosalo** 在 Dropbox 开发。守护进程模式是为了解决大型代码库在开发过程中需要频繁进行类型检查的性能问题而添加的。

# INSTALL

```apk: sudo apk add py3-mypy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mypy](/man/mypy)(1), [python](/man/python)(1), [pyright](/man/pyright)(1)

# RESOURCES

```[Source code](https://github.com/python/mypy)```

```[Homepage](https://mypy-lang.org/)```

```[Documentation](https://mypy.readthedocs.io/en/stable/mypy_daemon.html)```

<!-- verified: 2026-07-11 -->
