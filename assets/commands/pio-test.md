# TAGLINE

为 PlatformIO 项目运行单元测试

# TLDR

**运行单元测试**

```pio test```

**为特定环境运行测试**

```pio test -e [native]```

**运行特定测试**

```pio test -f [test_example]```

**以详细输出运行测试**

```pio test -v```

# SYNOPSIS

**pio test** [_options_]

# PARAMETERS

**-e**, **--environment** _name_
> 测试环境。

**-f**, **--filter** _pattern_
> 测试过滤模式。

**-i**, **--ignore** _pattern_
> 忽略匹配模式的测试。

**--upload-port** _port_
> 设备测试的上传端口。

**--test-port** _port_
> 用作测试通信接口的串口/UART 端口。

**-d**, **--project-dir** _path_
> 指定项目目录路径。

**-c**, **--project-conf** _file_
> 使用自定义的 platformio.ini 文件。

**-v**, **--verbose**
> 详细输出（可重复使用：-vv、-vvv）。

**--without-building**
> 跳过构建阶段。

**--without-uploading**
> 跳过上传阶段。

**--without-testing**
> 跳过测试阶段。

**--list-tests**
> 仅列出测试而不运行。

**--json-output**
> 以 JSON 格式返回输出。

**--junit-output-path** _file_
> 在指定路径生成 JUnit XML 报告。

# DESCRIPTION

**pio test** 用于运行 PlatformIO 项目的单元测试，同时支持本机（桌面）测试和嵌入式测试。默认使用 Unity 测试框架。测试可以在真实硬件或模拟器上运行。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-debug](/man/pio-debug)(1)
