# TAGLINE

为 PlatformIO 嵌入式项目启动调试会话

# TLDR

**启动调试会话**

```pio debug```

**调试特定环境**

```pio debug -e [uno]```

**使用 GDB 接口调试**

```pio debug --interface=gdb```

**使用指定的项目目录调试**

```pio debug -d [path/to/project]```

# SYNOPSIS

**pio debug** [_options_]

# PARAMETERS

**-e**, **--environment** _name_
> platformio.ini 中的目标环境。

**--interface** _type_
> 调试器接口 (gdb)。

**-d**, **--project-dir** _dir_
> PlatformIO 项目目录路径（默认：当前目录）。

**--upload-port** _port_
> 目标开发板的上传端口。

**-v**, **--verbose**
> 用于故障排查的详细输出。

**--project-conf** _path_
> 指定的 platformio.ini 文件路径。

# DESCRIPTION

**pio debug** 为 PlatformIO 项目准备调试环境或启动调试服务器。它连接片上调试器（JTAG/SWD），支持设置断点、单步执行代码以及在嵌入式硬件上检查变量。

二进制快捷方式 **piodebuggdb** 等价于 `pio debug --interface=gdb`。调试构建使用 platformio.ini 中的 `debug_build_flags`（通常为 `-O0 -g3 -ggdb3`，以获得完整的符号信息）。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-test](/man/pio-test)(1), [gdb](/man/gdb)(1)
