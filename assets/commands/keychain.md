# TAGLINE

管理 SSH 和 GPG agent 进程

# TLDR

**启动 SSH agent**

```eval $(keychain --eval [id_rsa])```

**添加多个密钥**

```eval $(keychain --eval [id_rsa] [id_ed25519])```

**包含 GPG 密钥**

```eval $(keychain --eval --agents ssh,gpg [id_rsa] [GPGKEY])```

**清除缓存的密钥**

```keychain --clear```

**安静模式**

```eval $(keychain -q --eval [id_rsa])```

**显示状态**

```keychain -l```

# SYNOPSIS

**keychain** [_options_] [_keys_...]

# PARAMETERS

_KEYS_
> 要管理的 SSH 或 GPG 密钥。

**--eval**
> 输出可供 shell eval 的命令。

**--agents** _LIST_
> agent 类型（ssh、gpg）。

**--clear**
> 清除缓存的密钥。

**-q**, **--quiet**
> 抑制输出。

**-l**, **--list**
> 列出已缓存的密钥。

**--noask**
> 设置 agent 文件，但如果密钥尚未加载也不提示添加。

**--stop** _which_
> 终止 agent 进程。取值：**mine**（keychain 启动的 agent）、**others** 或 **all**。

**--timeout** _MINUTES_
> 为添加到 ssh-agent 的身份设置超时时间（分钟）。

**--nogui**
> 禁用 SSH_ASKPASS，强制 ssh-add 在终端上提示。

**--ignore-missing**
> 找不到指定密钥时不发出警告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**keychain** 是 ssh-agent 和 gpg-agent 的前端，用于跨登录会话管理长期运行的 agent 进程。它不会在每次打开 shell 时都启动新的 agent，而是检查是否已有 agent 存在：找到则复用，只在必要时才启动新的，并将 agent 的环境变量保存在 `~/.keychain` 下的文件中，使任何 shell 都能继承它们。

这种方式意味着重启后你只需输入一次密码短语，之后所有的终端会话、cron 任务和脚本都可以使用缓存的密钥而无需再次提示。该工具通过 `--agents` 标志支持同时管理 SSH 和 GPG 密钥，并输出可由 shell eval 的命令来设置相应的 `SSH_AUTH_SOCK` 和 `GPG_AGENT_INFO` 环境变量。

# CAVEATS

需要集成到 shell 中，即在 shell 配置文件（如 `.bash_profile` 或 `.zshrc`）里加入一行 `eval $(keychain --eval ...)`。agent 环境变量保存在 `~/.keychain/` 下。

# HISTORY

keychain 由 **Daniel Robbins**（Funtoo）创建，用于简化跨会话的 SSH agent 管理。

# INSTALL

```dnf: sudo dnf install keychain```

```pacman: sudo pacman -S keychain```

```apk: sudo apk add keychain```

```zypper: sudo zypper install keychain```

```brew: brew install keychain```

```nix: nix profile install nixpkgs#keychain```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-agent](/man/ssh-agent)(1), [ssh-add](/man/ssh-add)(1), [ssh](/man/ssh)(1), [gpg](/man/gpg)(1)
