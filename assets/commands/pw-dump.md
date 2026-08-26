# TAGLINE

将 PipeWire 状态导出为 JSON

# TLDR

输出 PipeWire 当前状态的 **JSON 表示**

```pw-dump```

输出**特定对象**的 JSON 表示

```pw-dump [object_id]```

以**监控变更**的方式导出当前状态

```pw-dump -m```

将**远程实例**的状态导出到文件

```pw-dump -r [remote_name] > [path/to/dump.json]```

设置**颜色配置**

```pw-dump -C [never|always|auto]```

# SYNOPSIS

**pw-dump** [_options_] [_id_]

# PARAMETERS

_id_
> 只导出指定的对象 ID

**-m**, **--monitor**
> 监控变更并在更新时再次导出

**-r**, **--remote** _name_
> 连接到远程 PipeWire 实例

**-N**, **--no-colors**
> 禁用彩色输出。

**-C**, **--color** _mode_
> 颜色模式：never、always 或 auto。

**--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**pw-dump** 以 JSON 形式输出 PipeWire 的当前状态，包括节点、设备、模块、端口、链接和其他对象。这份完整的转储对调试、编写脚本以及了解当前音频/视频配置非常有用。

输出包含对象属性、格式、参数以及组件之间的关系。监控模式会持续运行，并在变化发生时输出这些变化。

# CAVEATS

在设备众多的系统上输出可能非常大。可使用对象 ID 过滤到特定对象。JSON 输出适合用 jq 或类似工具处理。

# HISTORY

**PipeWire** 的一部分，为该多媒体框架提供自省能力。与 pw-cli 互补，适合自动化和脚本化查询。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cli](/man/pw-cli)(1), [pw-dot](/man/pw-dot)(1), [pw-mon](/man/pw-mon)(1), [pw-top](/man/pw-top)(1)
