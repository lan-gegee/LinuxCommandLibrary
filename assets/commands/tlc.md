# TAGLINE

在 Linux 上通过 USB 配置兼容的腾龙镜头

# TLDR

**列出**已连接的腾龙镜头

```tlc devices```

显示默认设备的**镜头信息**

```tlc info```

按**序列号或端口**指定镜头

```tlc --device [SERIAL|/dev/ttyUSB0] info```

**获取**对焦环设置

```tlc ring get```

**反转**对焦环方向

```tlc ring set direction reverse```

**获取** Focus Set Button / Custom Switch 分配

```tlc button get```

**保存**当前全部设置到备份文件

```tlc settings save [file.tlc]```

从备份**加载**设置（仅限同一镜头型号）

```tlc settings load [file.tlc]```

# SYNOPSIS

**tlc** [**-v**|**-vv**] [**--device** _SERIAL_|_PORT_] _command_ [_subcommand_] [_args_]

# DESCRIPTION

**tlc**（Tamron Lens Control）是一个仅限 Linux 的命令行工具，用于查看和修改通过 USB 连接的兼容腾龙镜头的设置。它旨在覆盖官方 Tamron Lens Utility 在该应用不可用平台上的相同功能范围。

每次调用都会连接镜头、执行一项操作然后断开连接。子命令涵盖对焦环配置、按钮/开关分配、对焦校准、设备列表、镜头信息以及设置的备份/恢复。特定镜头型号可能只支持部分操作；使用 **tlc** _command_ **--help** 查看可接受的值和型号相关要求。

镜头必须以 USB 串口设备（cp210x）的形式出现。兼容硬件使用的厂商/产品 ID 包括 **2cd1:0002** 和 **2cd1:0005**。如果镜头出现在 **lsusb** 中但不在 **tlc devices** 中，请加载 **cp210x** 并绑定这些 ID（一次性及持久化 udev 规则见项目 README）。访问串口节点可能需要 **dialout** 组成员身份或 **uaccess** udev 标签。

这是一个独立的社区项目（GPL-3.0-or-later），与 Tamron Co., Ltd. 无关联。尚不支持固件更新和在线固件检查。

# PARAMETERS

**devices**
> 列出已连接的兼容镜头及其端口/序列号。

**info**
> 显示所选镜头的信息。

**ring** **get** | **set** ...
> 读取或更改对焦环设置（例如方向）。

**button** **get** | **set** ...
> 读取或更改 Focus Set Button 和 Custom Switch 的分配。

**focus-calibration** **set** _value_
> 微调自动对焦精度（范围依型号而定）。

**settings** **save**|_load_ _file_
> 备份或恢复当前全部设置。恢复仅在同一镜头型号上有效。

**--device** _SERIAL_|_PORT_
> 连接多个镜头时选择要使用的镜头。

**-v**
> 详细输出：显示发送到镜头的每项操作。

**-vv**
> 更加详细：还以十六进制打印原始收发字节。

**--help**
> 显示帮助（也可用于任何子命令之后）。

# CAVEATS

仅限 Linux；需要直连 USB 到兼容的腾龙镜头以及可用的串口（通常是 **/dev/ttyUSB***）。驱动配置错误或不完整是常见的失败原因。

更改镜头设置可能影响自动对焦行为；请在 **set** 之前用 **get** 核对，保持镜头连接直到命令完成，并在批量更改或重置前先执行 **settings save**。风险自负——错误配置或缺陷可能使镜头处于不良状态。

备份文件是型号相关的，不得加载到不同型号上。

# SEE ALSO

[gphoto2](/man/gphoto2)(1), [lsusb](/man/lsusb)(1), [exiftool](/man/exiftool)(1)

# RESOURCES

```[Source code](https://github.com/yikerman/tamron-lens-control)```

<!-- verified: 2026-08-08 -->
