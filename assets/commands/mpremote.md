# TAGLINE

microPython 远程控制工具

# TLDR

**连接设备**

```mpremote```

**运行 Python 代码**

```mpremote exec "[print('hello')]"```

**复制文件到设备**

```mpremote cp [local.py] :[remote.py]```

**从设备复制文件**

```mpremote cp :[remote.py] [local.py]```

**在设备上运行脚本**

```mpremote run [script.py]```

**进入 REPL**

```mpremote repl```

**列出设备上的文件**

```mpremote ls```

**挂载本地目录**

```mpremote mount [.]```

# SYNOPSIS

**mpremote** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**connect** _DEVICE_
> 连接到指定设备。

**exec** _CODE_
> 执行 Python 代码。

**cp** _SRC_ _DST_
> 复制文件（设备侧加 : 前缀）。

**run** _FILE_
> 在设备上运行本地脚本。

**repl**
> 进入交互式 REPL。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mpremote** 是 MicroPython 的远程控制工具。它用于管理 MicroPython 设备。

该工具可以复制文件、运行代码，并提供 REPL 访问。通过 USB 串口工作。

# CAVEATS

需要 MicroPython 设备。需要串口连接。需要 Python 3。

# HISTORY

mpremote 由 **MicroPython** 项目开发，是官方的设备管理工具。

# INSTALL

```zypper: sudo zypper install mpremote```

```brew: brew install mpremote```

```nix: nix profile install nixpkgs#mpremote```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1)
