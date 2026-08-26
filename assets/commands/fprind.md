# TAGLINE

指纹读取器守护进程

# TLDR

**启动指纹守护进程**

```fprind```

**在前台运行**

```fprind -f```

**调试模式**

```fprind -d```

**指定设备**

```fprind --device [/dev/bus/usb/001/002]```

# SYNOPSIS

**fprind** [_options_]

# PARAMETERS

**-f**, **--foreground**
> 在前台运行。

**-d**, **--debug**
> 启用调试输出。

**--device** _PATH_
> 指纹读取器设备。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**fprind**（fingerprint daemon，指纹守护进程）管理用于生物识别认证的指纹读取器设备。它与指纹硬件通信，并提供录入和验证服务。

该守护进程通过 PAM 接入系统认证，支持指纹登录和 sudo 验证。它会安全地保存已录入的指纹模板。

fprind 通过 libfprint 支持多种 USB 指纹读取器。

# CAVEATS

需要受支持的硬件。并非所有读取器都有 Linux 驱动。安全性取决于具体实现的质量。

# HISTORY

fprind 与 **libfprint** 及 fprintd 协同工作，为 Linux 提供指纹认证。这一生态让多种 Linux 发行版都能使用生物识别登录。

# SEE ALSO

[fprintd](/man/fprintd)(1)
