# TAGLINE

测试 Video4Linux2 驱动的 API 合规性

# TLDR

**测试默认视频设备**

```v4l2-compliance```

**测试指定设备**

```v4l2-compliance -d [/dev/video0]```

**运行流测试**

```v4l2-compliance -s```

**测试所有视频格式**

```v4l2-compliance -f```

**测试色彩格式**

```v4l2-compliance -c```

**详细输出**

```v4l2-compliance -v```

**运行所有测试**

```v4l2-compliance -s -f -c```

# SYNOPSIS

**v4l2-compliance** [_options_]

# PARAMETERS

**-d**, **--device** _device_
> 要测试的视频设备（默认：/dev/video0）。

**-s**, **--streaming**
> 运行基本的流测试。

**-f**, **--stream-all-formats**
> 测试所有支持的视频格式。

**-c**, **--stream-all-colors**
> 测试所有色彩格式。

**-v**, **--verbose**
> 启用详细输出。

**-w**, **--wrapper**
> 使用 libv4l2 包装层。

**-T**, **--trace**
> 跟踪 ioctl 调用。

**-n**, **--no-warnings**
> 抑制警告。

**--help**
> 显示帮助。

# DESCRIPTION

**v4l2-compliance** 测试 Video4Linux2 驱动和设备的 API 合规性。它会验证几乎所有 V4L2 ioctl，并检查驱动是否正确实现了规范。

该工具可测试视频捕获与输出、VBI、广播（radio）以及软件广播（swradio）设备。它会验证必需的能力是否存在，以及已声明的可选功能是否正常工作。流测试会校验缓冲区处理和格式支持。

新的 V4L2 驱动必须通过合规性测试才能被收入内核。该工具会在测试前保存设备状态并在测试后恢复，即使被 Ctrl-C 中断也是如此。

# CAVEATS

进行驱动开发时请始终使用 git 上的最新版本。某些测试失败可能是工具本身的 bug 而非驱动问题。流测试需要有效的输入/输出信号。启用所有选项时测试可能耗时较长。

# HISTORY

**v4l2-compliance** 作为 v4l-utils 软件包的一部分开发，用于保障 V4L2 驱动质量。它与 V4L2 API 一同演进，现已覆盖约 90% 的规范。向 Linux 内核提交新驱动时，它已成为强制要求。

# INSTALL

```apt: sudo apt install v4l-utils```

```dnf: sudo dnf install v4l-utils```

```pacman: sudo pacman -S v4l-utils```

```apk: sudo apk add v4l-utils```

```zypper: sudo zypper install v4l-utils```

```nix: nix profile install nixpkgs#v4l-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-ctl](/man/v4l2-ctl)(1)
