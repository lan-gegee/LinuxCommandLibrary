# TAGLINE

向服务管理器导入环境变量

# TLDR

**导入**环境变量

```systemctl import-environment [VARIABLE]```

导入**多个**变量

```systemctl import-environment [VAR1 VAR2 ...]```

为**用户**服务导入

```systemctl import-environment [VARIABLE] --user```

# SYNOPSIS

**systemctl import-environment** _VARIABLE_...

# PARAMETERS

**--user**
> 导入到用户服务管理器环境

**--system**
> 导入到系统管理器环境（默认）

# DESCRIPTION

**systemctl import-environment** 将当前 shell 会话中的环境变量导入 systemd 服务管理器的环境中。这些导入的变量对该服务管理器启动的所有 unit 可见。

这通常与 `--user` 一起使用，将显示相关的变量（如 DISPLAY、WAYLAND_DISPLAY 或 XDG_SESSION_ID）从登录会话传递给用户服务。

# CAVEATS

只影响导入之后启动的服务，不影响已在运行的服务。系统服务管理器通常运行在最小化环境中；导入用户会话变量可能并不合适。

# HISTORY

**import-environment** 子命令实现了登录会话与 systemd 用户服务的正确集成，解决了用户服务无法访问会话环境变量的问题。

# SEE ALSO

[systemctl-show-environment](/man/systemctl-show-environment)(1), [systemctl-set-environment](/man/systemctl-set-environment)(1), [systemctl](/man/systemctl)(1)
