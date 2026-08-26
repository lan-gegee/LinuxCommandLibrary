# TAGLINE

打印用户的登录名

# TLDR

**打印登录名**

```logname```

# SYNOPSIS

**logname** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**logname** 打印最初在控制终端上登录的用户名。它使用 `getlogin` 系统调用，该调用根据会话的 utmp 记录确定登录名，而不是依据环境变量（后者不可信）。

与报告当前有效用户的 **whoami** 不同，在 **su** 或 **sudo** 切换有效用户之后，**logname** 仍然显示原始登录名。

# CAVEATS

当没有控制终端时会报 "no login name" 错误（例如在某些 cron 任务或守护进程中）。在 **su** 之后与 **whoami** 结果不同。是 POSIX 标准命令。

# HISTORY

logname 是源自 POSIX 的传统 **Unix** 命令，显示登录系统所用的名称。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whoami](/man/whoami)(1), [who](/man/who)(1), [id](/man/id)(1)
