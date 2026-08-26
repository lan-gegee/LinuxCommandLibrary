# TAGLINE

持久的 shell 会话管理器

# TLDR

**连接到命名会话**（不存在时自动创建）

```shpool attach [session_name]```

**列出所有活动会话**

```shpool list```

**从当前会话分离**

```shpool detach```

**终止指定会话**

```shpool kill [session_name]```

手动**启动守护进程**

```shpool daemon```

以会话超时时间**连接**

```shpool attach --ttl [2h] [session_name]```

# SYNOPSIS

**shpool** [_options_] _subcommand_ [_args_]

# SUBCOMMANDS

**daemon**
> 启动 shpool 守护进程，监听连接并管理 shell 会话。通常通过 systemd 或自动守护进程化启动。

**attach** _name_
> 连接到命名的 shell 会话。若该会话不存在，则创建新的 shell；若已存在，则重新连接并重绘屏幕。

**list**
> 显示守护进程管理的所有活动 shell 会话。

**detach** [_name_]
> 与一个或多个会话断开连接但不终止它们。不带参数时，分离当前会话。

**kill** _name_
> 终止指定的 shell 会话。

# PARAMETERS

**-f**
> 强制连接到某个会话，先分离已有的客户端。与 **attach** 搭配使用。

**--ttl** _duration_
> 设置会话超时。超过该时长后会话会被自动终止。与 **attach** 搭配使用。

**-d**
> 启用自动守护进程化（默认行为）。

**-D**
> 禁用自动守护进程化；在前台运行守护进程。

# DESCRIPTION

**shpool** 是一个轻量级的 shell 会话持久化工具。它让命名的 shell 会话在断开连接后依然存活，之后可以重新连接，类似于 **tmux** 或 **screen**，但没有窗口拆分或平铺等终端复用功能。

Shpool 通过将 shell 的原始输出直接发送到本地终端模拟器来保留原生终端行为，包括回滚缓冲区和复制粘贴。它使用 VT100 仿真维护内存中的终端状态，因此重新连接时能够重绘屏幕，让你看到断连期间产生的输出。

守护进程会自动检测 bash、zsh 和 fish shell，并注入显示会话名的提示符前缀以便识别。每个会话同一时间只支持一个客户端。

# CONFIGURATION

配置文件位于 **~/.config/shpool/config.toml**。可用选项包括：

**nodaemonize**
> 运行 attach 时禁用守护进程自动启动。

**keybinding**
> 自定义分离快捷键（默认：**Ctrl-Space Ctrl-q**）。

Bash 用户应在 **~/.bashrc** 中添加 **shopt -s huponexit**，以防止后台进程在守护进程的进程树中不断累积。

# CAVEATS

单客户端会话模型意味着一个会话同一时间只能被一个终端连接。不提供窗口拆分、窗格管理或会话共享功能。在 macOS 上部分功能可能无法完全正常工作。需要先运行守护进程（通过 systemd、homebrew services 或自动守护进程化），才能创建会话。

# HISTORY

**shpool** 作为 **tmux** 和 **GNU screen** 的更简单替代方案而诞生，专注于会话持久化而不做终端复用。它使用 **Rust** 编写，由 GitHub 上的 shell-pool 社区开发。该项目强调保留原生终端体验，同时为远程工作提供可靠的重连能力。

# INSTALL

```nix: nix profile install nixpkgs#shpool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [dtach](/man/dtach)(1), [abduco](/man/abduco)(1), [mosh](/man/mosh)(1)
