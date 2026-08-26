# TAGLINE

为开发提供快速文件同步和网络转发

# TLDR

**创建同步会话**

```mutagen sync create [/local/path] [user@host:/remote/path]```

**列出同步会话**

```mutagen sync list```

**暂停同步会话**

```mutagen sync pause [session_name]```

**恢复同步会话**

```mutagen sync resume [session_name]```

**终止同步会话**

```mutagen sync terminate [session_name]```

**以忽略模式创建**

```mutagen sync create --ignore "*.log" [/local] [remote:/path]```

**刷新待处理的更改**

```mutagen sync flush [session_name]```

**监控会话**

```mutagen sync monitor```

# SYNOPSIS

**mutagen** [_sync_] [_forward_] [_create_] [_list_] [_terminate_] [_options_] [_args_]

# PARAMETERS

**sync create** _LOCAL_ _REMOTE_
> 创建同步会话。

**sync list**
> 列出同步会话。

**sync monitor**
> 实时监控会话。

**sync pause** _SESSION_
> 暂停同步。

**sync resume** _SESSION_
> 恢复同步。

**sync flush** _SESSION_
> 刷新待处理的更改。

**sync terminate** _SESSION_
> 结束同步会话。

**forward create** _LOCAL_ _REMOTE_
> 创建端口转发。

**--ignore** _PATTERN_
> 忽略匹配的文件。

**--sync-mode** _MODE_
> 同步模式（two-way-safe、one-way-safe 等）。

**--name** _NAME_
> 会话名称。

# DESCRIPTION

**mutagen** 为开发工作流提供快速文件同步和网络转发。它的设计目标是同步本地与远程环境之间的代码。

同步过程会监视文件系统变更并双向传播。与 rsync 不同，它维护持久会话，能实时响应变化。

该工具能智能处理冲突。two-way-safe 模式会生成冲突文件而不是直接覆盖。单向模式只沿单一方向同步。

Docker 集成可将文件同步到容器中。SSH 连接可与远程服务器同步。两者可以同时运行，满足复杂的开发环境需求。

端口转发会对网络连接建立隧道，让你在本地访问远程服务，或将本地服务暴露到远端。

性能优化包括压缩、缓存和差异传输。大型代码库也能高效同步。

# CAVEATS

远程系统上需要 agent（通过 SSH 自动安装）。文件数量很大时初始扫描可能变慢。冲突需要手动解决。macOS/Windows 上的 Docker Desktop 可能存在文件系统限制。

# HISTORY

**Mutagen** 由 **Jacob Howard** 约 **2018 年**创建，旨在解决容器化开发环境中的文件同步问题。它针对的是 Docker Desktop 在 macOS 和 Windows 上文件共享的性能问题。

# INSTALL

```nix: nix profile install nixpkgs#mutagen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [unison](/man/unison)(1), [syncthing](/man/syncthing)(1), [docker](/man/docker)(1)
