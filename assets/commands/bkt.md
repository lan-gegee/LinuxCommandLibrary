# TAGLINE

为开销较大的命令输出提供子进程缓存

# TLDR

**缓存**某个命令 1 分钟

```bkt --ttl=1m -- [expensive-command]```

**将当前目录**纳入缓存键

```bkt --ttl=5m --cwd -- [command]```

**强制刷新**

```bkt --ttl=1m --force -- [command]```

**丢弃过期缓存并运行**

```bkt --ttl=30s -- [command]```

# SYNOPSIS

**bkt** [*options*] **--** *command* [*args*...]

# DESCRIPTION

**bkt** 运行一个命令并将其 stdout/stderr/退出状态缓存一段生存时间（**--ttl**）。之后以相同键发起的调用会复用缓存结果而不再重新运行进程——这对缓慢的测试、网络查询或提示符片段很有用。缓存键可以纳入工作目录、环境变量子集以及其他作用范围。

# PARAMETERS

**--ttl** *duration*

> 成功结果的保留时长（如 **30s**、**5m**、**1h**）。

**--** *command*...

> 要执行/缓存的命令及参数（必需的分隔符）。

**--force**

> 忽略现有缓存并刷新。

**--cwd**

> 将当前工作目录纳入缓存键。

**--env** *name*

> 将指定的环境变量纳入缓存键。

**--stale** *duration* / **--discard-failures** 及相关标志

> 控制 stale-while-revalidate 和失败结果缓存（见 **bkt --help**）。

# CAVEATS

如果外部状态在 TTL 内发生变化，缓存的输出可能不再正确。除非你理解其影响，否则不要缓存有必须生效的副作用的命令。缓存位置位于用户缓存目录之下。

# INSTALL

```apt: sudo apt install bkt```

```brew: brew install bkt```

```nix: nix profile install nixpkgs#bkt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[time](/man/time)(1), [chronic](/man/chronic)(1), [memoize](/man/memoize)(1)

# RESOURCES

```[Source code](https://github.com/dimo414/bkt)```

<!-- verified: 2026-07-19 -->
