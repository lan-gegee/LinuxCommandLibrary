# TAGLINE

重新加载 systemd unit 配置

# TLDR

**重新加载** systemd 配置

```systemctl daemon-reload```

# SYNOPSIS

**systemctl daemon-reload**

# DESCRIPTION

**systemctl daemon-reload** 重新加载 systemd 管理器配置，扫描新增或修改过的 unit 文件。创建、修改或删除 unit 文件之后必须运行该命令，更改才能生效。

重新加载会重新扫描所有 unit 文件目录，更新依赖树，并重载被修改的 unit。正在运行的服务不受影响；只有它们的配置会在下次启动时更新。

# CAVEATS

不会重启或影响当前运行的服务。要将配置更改应用到运行中的服务，请在重载后使用 `systemctl restart`。unit 文件中的错误会被报告，但不会阻止其他 unit 的重载。

# HISTORY

**daemon-reload** 子命令是 **systemd** 工作流程的基础部分。它提供了一种在不中断运行服务的情况下安全更新配置的方式。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-daemon-reexec](/man/systemctl-daemon-reexec)(1), [systemctl-reload](/man/systemctl-reload)(1)
