# TAGLINE

在 Linux 上用 bwrap 沙箱运行编码代理

# TLDR

在沙箱中**运行**受支持的代理

```agent-run [claude]
agent-run [codex]
agent-run [opencode]
agent-run [pi]```

使用显式指定的**配置**文件

```agent-run --config [path/to/config.toml] [claude]```

# SYNOPSIS

**agent-run** [_options_] _agent_ [_agent-args_...]

# DESCRIPTION

**agent-run** 在 **bubblewrap**（**bwrap**）沙箱内启动编码代理（Claude Code、Codex、OpenCode、pi 以及其他按工具名配置的代理）。主机文件系统以只读方式挂载；选定的路径可以按工具单独设为可写。配置采用 TOML 格式：既有全局默认值，也有每个工具各自的 **mount**、**env**、**network** 和 **inherit_env** 设置。

配置取自 **--config** 参数，或从当前目录向上查找最近的 **.agent-run/config.toml**。若两者都不存在，默认设置允许网络访问和环境变量继承。这个二进制文件是一个小型独立可执行程序，内嵌 bwrap 并通过 memfd 执行它。

# PARAMETERS

**--config** _path_
> TOML 配置文件的路径

_agent_
> 与配置中 **tools.<name>** 相匹配的工具名（以第一个参数的 basename 选择对应的工具配置）

# CONFIGURATION

配置片段示例：

```
[global]
network = true
inherit_env = true
mount = ["~/.cache", ".."]

[tools.claude]
mount = ["~/.claude", "~/.claude.json"]
```

编辑器用的 JSON schema 见项目内的 **schema.json**。把 **RUST_LOG** 设为 **debug** 或 **trace** 可启用诊断日志。

# CAVEATS

仅支持 Linux；需要非特权用户命名空间。它旨在拦截代理的操作失误，而不是彻底隔离恶意代码：整个主机文件系统均以只读方式可见，而且一旦启用网络，数据外泄仍然可能发生。想要更强的隔离，请优先选择 microVM。

# SEE ALSO

[bwrap](/man/bwrap)(1), [clawk](/man/clawk)(1)

# RESOURCES

```[Source code](https://github.com/sin-ack/agent-run)```

<!-- verified: 2026-07-14 -->
