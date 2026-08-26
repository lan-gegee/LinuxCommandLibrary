# TAGLINE

Linux 上 Sony DualShock 4 手柄的命令行监视器

# TLDR

**监视**第一个已连接的 DualShock 4 手柄

```ds4```

**监视指定的** hidraw 设备

```ds4 [/dev/hidraw0]```

**显示**内嵌帮助

```ds4 --help```

# SYNOPSIS

**ds4** [_device_]

# DESCRIPTION

**ds4** 是一款小型命令行监视器，面向通过 USB 或蓝牙连接到 Linux 机器的 **Sony DualShock 4**（PS4）手柄。它打开手柄的 **hidraw** 节点，解析传入的 HID 输入报告，并持续打印每个摇杆、扳机、按钮、触摸板触点、陀螺仪轴、加速度计轴和电量指示的解码状态。

与通过 **uinput** 创建虚拟游戏杆和鼠标设备的 **ds4drv** 不同，**ds4** 不模拟任何输入设备——它只读取和打印。这使它适合用来验证手柄是否被检测到、在配置 **antimicrox** 或 **AntiMicroX** 等封装工具之前调试按键映射、逆向分析厂商专属的 HID 报告，或刻画 IMU 的传感器漂移。

该工具用 Go 编写，以源码形式通过 Go 模块路径 **github.com/kenshaw/ds4** 分发。第一个位置参数可以覆盖自动检测到的 hidraw 设备路径。

# CAVEATS

读取 **/dev/hidraw\*** 通常需要 **root** 权限或一条授予 **input** 组访问权的 udev 规则；否则程序在打开设备时会报权限错误。解码器面向第一代 DS4（CUH-ZCT1U）和改版 CUH-ZCT2U；DualShock 3 和 DualSense（PS5）手柄使用不同的报告布局，不受支持。蓝牙连接的手柄发送的报告比 USB 的大——两种都能处理，但两种传输方式的字节偏移不同。

# HISTORY

**ds4** 由 **Kenneth Shaw**（kenshaw）编写并发布在 GitHub 上，是一款用于在 Linux 上检视 DualShock 4 协议的小型 Go 实用程序。它与更广泛的 Linux PS4 手柄生态（**ds4drv**、**hid-playstation** 内核驱动、**DualSense Tools**）互补，提供了一个极简、零依赖的监视器。

# SEE ALSO

[evtest](/man/evtest)(1), [jstest](/man/jstest)(1)
