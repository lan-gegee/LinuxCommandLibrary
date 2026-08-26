# TAGLINE

从 Linux 输入设备读取原始输入事件并输出到 stdout

# TLDR

**独占式**读取原始输入事件（系统将看不到这些事件）

```sudo intercept -g [/dev/input/eventX]```

**非独占式**读取原始输入事件（系统也能看到）

```sudo intercept [/dev/input/eventX]```

# SYNOPSIS

**intercept** [_options_] _device_

# PARAMETERS

**-g**
> 独占地抓取设备，阻止其他程序读取事件

_device_
> 输入设备文件（如 /dev/input/event0）

# DESCRIPTION

**intercept** 从 Linux 输入设备读取原始输入事件并输出到 stdout。它是 Interception Tools 项目的一部分，旨在构建输入设备处理管道。

其输出可以通过管道传给转换工具，再通过 uinput 送回虚拟输入设备，从而在底层实现按键重映射、宏创建和其他输入修改。

# CAVEATS

访问输入设备需要 root 权限。使用 -g 标志会独占捕获输入；如果拦截键盘输入却没有正确处理输出，可能把自己锁在门外。属于 interception-tools 软件包。

# HISTORY

intercept 是 Interception Tools 项目的一部分。该项目是一组可组合的实用工具，利用 evdev 和 uinput 接口拦截和操纵 Linux 上的输入事件。

# INSTALL

```brew: brew install intercept```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evtest](/man/evtest)(1), [uinput](/man/uinput)(4), [libinput](/man/libinput)(1)
