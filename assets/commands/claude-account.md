# TAGLINE

在 Linux 上切换隔离的 Claude Code 账户

# TLDR

**安装**发行版二进制并接好 PATH 垫片

```./claude-account install```

**添加**一个命名的账户配置（打开官方 Claude 登录）

```claude account add [name]```

**切换**活动配置

```claude account use [name]```

**列出**所有配置并显示当前配置

```claude account list```

```claude account current```

**移除**一个配置（可选清除本地数据）

```claude account remove [name]```

切换后照常运行 Claude —— 垫片会设置一个隔离的配置目录

```claude```

# SYNOPSIS

**claude-account** **install**

**claude** **account** _subcommand_ [_options_]

# DESCRIPTION

**claude-account** 是一个仅限 Linux 的 Claude Code 配置切换器。执行 **install** 后，它会在 **PATH** 中靠前的位置放置一个 **claude** 垫片，为每个命名账户设置独立的 **CLAUDE_CONFIG_DIR**，并把其余参数转发给真正的 Claude Code 可执行文件。

登录、登出、凭据和令牌刷新仍由 Claude Code 自身完成。**claude-account** 从不读取或复制凭据内容。它是一个独立的社区项目，与 Anthropic 无关，也不受其支持或认可。

默认存储使用 **~/.config/claude-account/** 和 **~/.local/share/claude-account/** 下的 XDG 路径。**CLAUDE_ACCOUNT_HOME** 可以迁移全部应用数据。为实现配置隔离，除非设置了 **CLAUDE_ACCOUNT_PRESERVE_AUTH_ENV=1**，包装器会从子进程环境中清除 **ANTHROPIC_API_KEY**、**ANTHROPIC_AUTH_TOKEN** 和 **CLAUDE_CODE_OAUTH_TOKEN**。

# COMMANDS

**install**

> 安装垫片目录，并打印需要添加到 shell 配置文件中的 **export PATH=...** 行。

**account add** _name_ [**--email** _addr_] [**--sso**] [**--console**]

> 注册一个配置并为其运行 Claude Code 的官方登录。第一个注册的配置会成为活动配置。

**account use** _name_

> 将 _name_ 设为新启动的 Claude 进程的活动配置。

**account list**

> 列出已注册的配置。

**account current**

> 只打印活动配置名（适合脚本调用）。

**account remove** _name_ [**--purge**] [**--yes**] [**--force**]

> 登出并注销一个配置。**--purge** 会删除设置、会话、插件和历史记录。移除活动配置需要 **--force**。

# CAVEATS

仅支持 Linux。需要已安装的 Claude Code。切换不影响已在运行的 Claude 会话。安装的二进制名为 **claude-account**；日常的配置命令通过垫片以 **claude account ...** 的形式调用。

# SEE ALSO

[claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/hamzarehmandeveloper/claude-account)```

<!-- verified: 2026-07-30 -->
