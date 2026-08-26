# TAGLINE

基于 Rust 的 TLDR 页面客户端

# TLDR

**显示页面**

```tldrl [command]```

**更新缓存**

```tldrl --update```

**列出所有页面**

```tldrl --list```

**显示特定平台内容**

```tldrl --platform [linux] [command]```

**搜索页面**

```tldrl --search "[keyword]"```

# SYNOPSIS

**tldrl** [_--update_] [_--platform os_] [_options_] [_command_]

# PARAMETERS

**--update**
> 更新缓存。

**--list**
> 列出页面。

**--platform** _OS_
> 平台过滤。

**--search** _TERM_
> 搜索页面。

**--help**
> 显示帮助。

# DESCRIPTION

**tldrl** 是一个基于 Rust 的快速 TLDR 页面客户端。TLDR 是社区维护的精简命令行文档集，以实用示例为核心。它将页面缓存在本地，支持离线访问和快速查询。

该客户端支持 Linux、macOS 和 Windows 的平台专属页面，并提供按关键字搜索相关命令的功能。可通过 **--update** 更新缓存，从 TLDR 仓库获取最新页面。

# CAVEATS

更新需要联网。缓存需要刷新。非官方 tldr 客户端。

# HISTORY

**tldrl** 是一个用 Rust 实现的 TLDR 客户端，用于访问社区维护的精简版 man page。

# SEE ALSO

[tldr](/man/tldr)(1), [man](/man/man)(1), [cheat](/man/cheat)(1)
