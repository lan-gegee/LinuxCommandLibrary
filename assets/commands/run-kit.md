# TAGLINE

面向 tmux 会话的远程浏览器控制台

# TLDR

**启动**仪表盘守护进程（默认端口 3000）

```run-kit daemon start```

在浏览器中**打开**仪表盘

```open http://localhost:3000```

在 git worktree 中**创建**智能体工作区（必须在 tmux 内）

```run-kit riff```

**创建**三个并行工作区

```run-kit riff -N 3```

出现故障时**检查**依赖

```run-kit doctor```

向已订阅的设备**发送** Web Push 通知

```run-kit notify "deploy finished" --title "CI"```

# SYNOPSIS

**run-kit** \<command\> [_options_]

# DESCRIPTION

**run-kit**（简写别名 **rk**）是一个远程的、手机优先的 **tmux** 控制台。它把每个会话和窗格都以活动终端的形式呈现在浏览器侧边栏中——无需数据库；状态直接从 tmux 和文件系统推导而来。同一个仪表盘也可以在手机上通过 Tailscale HTTPS 访问。

两个组成部分彼此独立：

* **run-kit riff** — 创建一个 git worktree（通过姊妹工具 **wt**），打开一个 tmux 窗口并启动窗格（默认为一个编码智能体；也允许任意 **--cmd**）。
* **run-kit serve** / **run-kit daemon** — 监视 tmux 的 HTTP 仪表盘（默认 **127.0.0.1:3000**）。守护进程运行在专用的 tmux 服务器（**rk-daemon**）中，因此重启不会杀死用户会话。

可选的 **run-kit agent-setup** 会安装 harness 钩子，让窗格报告智能体的忙碌/等待/空闲状态。看板可以并排固定多个窗格；**run-kit notify** 会将 Web Push 扇出到已订阅的浏览器。Shell 补全：**eval "$(run-kit shell-init zsh)"**。

可通过 shll 工具箱安装器或 Homebrew 安装（**sahil87/tap/run-kit**）。**rk** 是 **run-kit** 的完整可互换别名。

# PARAMETERS

**riff** [_preset_] [**--skill** _slash_] [**--cmd** _command_] [**-N** _count_] [**--layout** _layout_] [**--** _wt-flags_]
> 创建 worktree + tmux 窗口 + 一个或多个窗格。必须在已有的 tmux 会话内运行。**--skill** 和 **--cmd** 可重复指定（形成窗格数组）。**-N** 会创建并行工作区。

**serve**
> 在前台启动 HTTP 服务器。**RK_HOST**（默认 **127.0.0.1**）、**RK_PORT**（默认 **3000**）。

**daemon start|stop|restart|status**
> 管理后台仪表盘守护进程。

**doctor**
> 检查运行时依赖（tmux、**wt**、启动器、端口）。

**agent-setup** [**--uninstall**]
> 安装或移除用于窗格状态上报的 agent-harness 钩子。

**notify** _message_ [**--title** _title_]
> 发送 Web Push 通知（服务器不可用时静默失败）。

**status**
> 汇总 tmux 会话信息。

**url**
> 打印已配置的服务器 URL。

**update**
> 通过 Homebrew 升级并重启守护进程。

**shell-init** \<shell\>
> 为 zsh、bash、fish 或 powershell 输出可供 eval 的补全脚本。

**help**
> 任意子命令的帮助。

# CAVEATS

**riff** 需要 **$TMUX**、**PATH** 中的 **wt** 以及已配置的智能体/启动器。智能体状态圆点需要一次性运行 **agent-setup**，并在安装后开启新的智能体会话。Web Push 需要安全上下文（HTTPS 或 localhost）。绑定 **RK_HOST=0.0.0.0** 会把终端仪表盘暴露在网络上——请限制访问（VPN/Tailscale、防火墙）。

# INSTALL

```brew: brew install run-kit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [git](/man/git)(1), [git-worktree](/man/git-worktree)(1), [tailscale](/man/tailscale)(1)

# RESOURCES

```[Source code](https://github.com/sahil87/run-kit)```

```[Homepage](https://shll.ai/run-kit)```

```[Documentation](https://shll.ai/tools/run-kit/commands/)```

<!-- verified: 2026-07-22 -->
