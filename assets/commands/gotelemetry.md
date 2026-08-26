# TAGLINE

Go 工具链遥测管理

# TLDR

**查看遥测配置**

```gotelemetry```

**启用遥测**

```gotelemetry on```

**禁用遥测**

```gotelemetry off```

**设置为本地模式**

```gotelemetry local```

**查看已收集的数据**

```gotelemetry view```

# SYNOPSIS

**gotelemetry** [_command_]

# PARAMETERS

**on**
> 启用遥测数据上传。

**off**
> 禁用遥测。

**local**
> 仅在本地收集。

**view**
> 启动本地 Web 查看器，以图表形式展示已收集的遥测数据。

**env**
> 打印当前的遥测环境（模式和数据目录）。

**clean**
> 删除所有本地遥测数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gotelemetry** 用于管理 Go 工具链的遥测设置。它控制是否收集使用统计和崩溃报告，以及是否（可选）将其上传，以帮助 Go 团队确定工具链改进工作的优先级。

不带参数运行该命令会显示当前模式。共支持三种模式：**local**（默认）会把计数器和报告收集到磁盘上但从不上传；**on** 会在此基础上把获得批准的计数器上传到 telemetry.go.dev；**off** 则完全关闭收集。**view** 命令可在浏览器中以图表形式呈现本地存储的报告。

自 Go 1.23 起，相同的功能也可以通过 go 工具的子命令 **go telemetry** [_on|off|local_] 使用，不再需要单独的 gotelemetry 二进制文件。

# CAVEATS

上传属于自愿开启的功能；只有经过公开提案流程批准的计数器才会上传，且不包含堆栈跟踪或其他敏感数据。该工具随 Go 1.21 推出（当时仅限本地收集），上传支持于 Go 1.23 加入。

# HISTORY

gotelemetry 随 **Go 1.21** 引入，用于开启可选的遥测收集以改进 Go 工具链；**go telemetry** 子命令及上传能力则在 **Go 1.23** 中落地。

# SEE ALSO

[go](/man/go)(1)

# RESOURCES

```[Source code](https://go.googlesource.com/telemetry)```

```[Documentation](https://go.dev/doc/telemetry)```

<!-- verified: 2026-07-17 -->
