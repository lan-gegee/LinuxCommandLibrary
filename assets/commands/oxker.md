# TAGLINE

用于查看和控制 Docker 容器的终端用户界面

# TLDR

**启动 Docker 容器查看器**

```oxker```

将更新间隔**设为 500 毫秒**

```oxker -d 500```

**显示原始日志**（不带 ANSI 格式）

```oxker -r```

**连接到自定义的 Docker 套接字**

```oxker --host [/path/to/docker.sock]```

# SYNOPSIS

**oxker** [_options_]

# PARAMETERS

**-d** _MILLISECONDS_
> 设置更新间隔（毫秒）。默认：1000。

**-r**
> 显示不带 ANSI 格式的原始日志。

**-c**
> 尝试对日志着色。

**-t**
> 从日志条目中移除时间戳。

**--host** _STRING_
> 自定义 Docker 套接字连接路径。

**--timezone** _STRING_
> 按指定时区显示日志。

# DESCRIPTION

**oxker** 是一个用于查看和控制 Docker 容器的终端用户界面。它在单个界面中显示容器列表、日志和资源统计。你可以直接在 TUI 中暂停、启动、停止、重启和删除容器。

# CAVEATS

需要访问 Docker 套接字。若在 Docker 内部运行，则需要把宿主机的 Docker 套接字作为卷挂载进来。

# HISTORY

**oxker** 由 **mrjackwills** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install oxker```

```nix: nix profile install nixpkgs#oxker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [lazydocker](/man/lazydocker)(1), [ctop](/man/ctop)(1)
