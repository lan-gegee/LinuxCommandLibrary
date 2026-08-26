# TAGLINE

在 Linux 终端显示 GPU 使用统计的工具

# TLDR

**启动 GPU 监控 TUI**

```qmassa```

**将统计数据保存到 JSON 文件**

```qmassa --json [output.json]```

**从 JSON 文件回放数据**

```qmassa --replay [stats.json]```

**根据 JSON 文件绘制 SVG 图表**

```qmassa --plot [stats.json]```

# SYNOPSIS

**qmassa** [_options_]

# PARAMETERS

**--json** _FILE_
> 将 GPU 统计数据保存到 JSON 文件。

**--replay** _FILE_
> 在 TUI 中回放先前记录的统计数据。

**--plot** _FILE_
> 根据记录的 JSON 数据生成 SVG 图表。

# DESCRIPTION

**qmassa** 是一个基于终端的工具，用于在 Linux 上显示 GPU 使用统计。它展示设备信息以及占用 GPU 的 DRM 客户端进程。它支持将统计数据记录到 JSON、回放已记录的数据，以及生成 SVG 图表用于可视化。

# CAVEATS

要获取完整的使用统计需要 Linux 内核 6.8 或更高版本。编译时需要 libudev 开发包。

# HISTORY

**qmassa** 由 **Ulisses Furquim**（ulissesf）创建，使用 **Rust** 编写。

# SEE ALSO

[nvtop](/man/nvtop)(1), [nvidia-smi](/man/nvidia-smi)(1), [radeontop](/man/radeontop)(1)
