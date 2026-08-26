# TAGLINE

跨重启休眠并恢复 Claude Code 会话

# TLDR

关机前**对所有**正在运行的 Claude Code 会话**做快照**

```claude-hibernate hibernate --all```

仅对当前仓库 worktree 中的会话**做快照**

```claude-hibernate hibernate```

**预览**将被快照的内容（不写入）

```claude-hibernate hibernate --dry-run```

**列出**已保存快照中的会话

```claude-hibernate list```

重启后**唤醒**所有已快照的会话

```claude-hibernate wake```

**预览**唤醒命令而不启动终端

```claude-hibernate wake --dry-run```

端到端**验证**环境与检测功能

```claude-hibernate doctor```

**安装** Claude Code 钩子以获取精确的会话 ID

```claude-hibernate hooks install```

**启用**每 10 分钟一次的自动快照

```claude-hibernate auto enable```

# SYNOPSIS

**claude-hibernate** _command_ [_options_]

# PARAMETERS

**hibernate**
> 将正在运行的 Claude Code 会话捕获到快照文件。范围：**--repo**（默认，当前仓库的 worktree）、**--here**（仅 **$PWD**）、**--all**（整台机器）。**--dry-run** 只预览不写入。**--quiet** 减少输出。

**wake**
> 重新打开并恢复快照中的所有会话。**--dry-run** 仅打印恢复命令。**--fork** 以 **--fork-session**（全新 ID）恢复。**--live** 以当前正在运行的会话而非快照为来源。**--launcher** _name_ 强制指定终端后端（**tmux**、**iterm2**、**terminal**、**kitty**、**wezterm**、**alacritty**、**gnome-terminal**、**konsole**、**print**）。

**list**
> 显示快照。**--live** 改为列出当前正在运行的会话。

**doctor**
> 运行环境检查（**ok** / **warn** / **FAIL**）。

**hooks** **install** | **uninstall** | **status**
> 管理 Claude Code 的 **SessionStart** 钩子，用于精确跟踪会话 ID。

**auto** **enable** | **disable** | **status**
> 管理周期性自动快照（macOS 上用 launchd，Linux 上用 systemd 用户定时器或 crontab）。**enable --interval** _N_ 设置快照间隔分钟数（默认 **10**）。

# DESCRIPTION

**claude-hibernate** 相当于 Anthropic **Claude Code** 会话的系统休眠。Claude Code 不会持久记录哪些会话在运行；重启会杀死所有进程，让你不得不重新回想之前打开了什么。该工具在断电前将活动会话集合快照到磁盘，开机后恢复——每个会话回到原目录、使用原会话 ID，并带上捕获的启动标志（如 **--model** 和 **--dangerously-skip-permissions**），在你偏好的终端中打开。

会话发现采用多种启发式方法（进程名、二进制路径、项目关联、命令行参数），因为 Claude Code 的进程名因安装类型和平台而异。可选的 **hooks install** 让 Claude Code 在启动时报告精确的会话 ID。没有钩子时，ID 可能来自进程参数中的 **--resume**（macOS）或最新转录（transcript）启发式。

**wake** 会自动检测终端（或使用 **CLAUDE_HIBERNATE_LAUNCHER** / **--launcher**）。在 tmux 内部时 tmux 永远优先；否则后端包括 iTerm2 窗格网格、Terminal.app、kitty/wezterm/alacritty、GNOME Terminal/Konsole 以及 **print**（仅打印命令）。若某会话仍在运行，**wake** 会跳过它以避免两个进程共用一个 ID（**--fork** 可覆盖此行为）。

状态保存在 **${XDG_STATE_HOME:-~/.local/state}/claude-hibernate/** 下（**snapshot.json**、**history/** 各代快照、**live/** 钩子记录）。需要 **bash** 3.2+、**python3** 和标准 Unix 工具。可通过 Homebrew tap、项目的 **install.sh** 安装，或将 **scripts/claude-hibernate.sh** 复制到 **PATH**。

# CONFIGURATION

**CLAUDE_HIBERNATE_STATE_DIR**
> 覆盖状态目录（默认 **~/.local/state/claude-hibernate**）。

**CLAUDE_HIBERNATE_FILE**
> 覆盖快照文件路径。

**CLAUDE_CONFIG_DIR**
> Claude Code 配置目录，用于项目/转录关联。

**CLAUDE_HIBERNATE_HISTORY_KEEP**
> 在 **history/** 中保留的时间戳快照代数（默认 **10**）。

**CLAUDE_HIBERNATE_LAUNCHER**
> **wake** 的默认终端后端（名称与 **--launcher** 相同）。

# CAVEATS

Claude Code 的转录与进程内部机制属于不受官方支持的层面，可能随更新而失效——升级后请运行 **doctor**。在 Linux 上，Claude 会重写进程参数，因此只有钩子追踪的会话才能可靠恢复启动标志。**hibernate** 不会停止会话，只对其做快照。Codex 及其他代理不在支持范围内。macOS 上首次 **wake** 可能提示授权对 iTerm2 或 Terminal.app 的自动化访问。

# HISTORY

由 **Steve Vitali** 编写，是一个自包含的 bash 工具（配合 python3 处理 JSON），专注于跨重启恢复 Claude Code 会话。MIT 许可证。从更大的 agent-skills 合集中抽取为独立仓库。

# SEE ALSO

[claude](/man/claude)(1), [claude-thermos](/man/claude-thermos)(1), [tmux](/man/tmux)(1)

# RESOURCES

```[Source code](https://github.com/SteveVitali/claude-hibernate)```

```[Documentation](https://github.com/SteveVitali/claude-hibernate#readme)```

<!-- verified: 2026-07-24 -->
