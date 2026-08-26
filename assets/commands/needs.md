# TAGLINE

检查系统是否安装了所需的可执行文件

# TLDR

**检查工具是否已安装并显示其版本**

```needs [tool1] [tool2] [tool3]```

**检查但不获取版本信息**

```needs --no-versions [tool1] [tool2]```

**显示完整版本字符串而非简短版本**

```needs --full-versions [tool1] [tool2]```

**静默运行，仅通过退出码报告结果**

```needs -q [tool1] [tool2]```

**带详细日志检查**

```needs -vvv [tool1] [tool2]```

# SYNOPSIS

**needs** [_options_] [_executables_...]

# PARAMETERS

**-n**, **--no-versions**
> 跳过版本检查，只验证二进制文件是否存在。

**-f**, **--full-versions**
> 显示每个二进制文件的完整版本字符串而非缩短的版本。

**-q**, **--quiet**
> 保持静默，仅通过退出码传达结果（全部找到为 0，有缺失为 1）。

**-v**, **--verbosity**
> 提高详细程度。可重复使用以获得更多信息（如 -vvv 输出日志，-vvvv 输出计时信息）。

**--help**
> 显示帮助信息。

**--version**
> 显示 needs 自身的版本号。

# DESCRIPTION

**needs** 是一款命令行工具，用于验证指定的可执行文件是否已安装在系统上，并可选择获取它们的版本信息。它使用多线程执行来加速检查，提供彩色输出，且支持适合管道处理的输出。

二进制名称可以通过命令行参数提供，也可以列在 `needsfile` 中（每行一个或多个二进制名称）。

退出码表明所有必需的工具是否齐备（0 表示成功，1 表示有缺失），因此非常适合在脚本和 CI 流水线中使用。

# CAVEATS

版本检测依赖于每个工具支持标准的版本标志（`--version` 或 `-v`）。某些工具的版本可能无法被正确检测。`--no-versions` 和 `--full-versions` 标志仅在编译时启用 `version-retrieval` 特性（默认启用）时可用。

# HISTORY

**needs** 由 **NQMVD** 创建，使用 **Rust** 编写。

# SEE ALSO

[which](/man/which)(1), [command](/man/command)(1), [has](/man/has)(1), [type](/man/type)(1), [whereis](/man/whereis)(1)
