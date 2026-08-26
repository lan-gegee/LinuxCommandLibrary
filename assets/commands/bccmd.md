# TAGLINE

向 CSR 蓝牙芯片发送 BlueCore 命令

# TLDR

**获取芯片版本号**

```bccmd chiprev```

**获取本地蓝牙时钟**

```bccmd clock```

**从设备获取随机数**

```bccmd rand```

**执行冷复位**

```bccmd coldreset```

**执行热复位**

```bccmd warmreset```

**读取 PS 键值**

```bccmd psget [key]```

**设置 PS 键值**

```bccmd psset [key] [value]```

**指定传输方式**

```bccmd -t [HCI|USB|BCSP|H4] [command]```

# SYNOPSIS

**bccmd** [_-t transport_] [_-d device_] _command_ [_args_]

# DESCRIPTION

**bccmd** 是 CSR BCCMD 接口的实用工具，用于向 Cambridge Silicon Radio（CSR）蓝牙设备发送 BlueCore 命令。它可以直接控制蓝牙芯片参数和持久存储（persistent store）的键值。

该工具是 BlueZ 蓝牙协议栈的一部分，提供对基于 CSR 的蓝牙控制器的底层访问。

# PARAMETERS

**-t** _transport_
> 传输类型：HCI（默认）、USB、BCSP、H4。可识别 3WIRE 但未实现

**-d** _device_
> 要使用的设备（默认：第一个 HCI 设备，串口则为 /dev/ttyS0）

**-h, --help**
> 显示帮助信息

# COMMANDS

**builddef**
> 获取构建定义

**buildname**
> 获取构建名称字符串

**chiprev**
> 获取芯片版本号

**memtypes**
> 获取内存类型

**clock**
> 获取本地蓝牙时钟

**rand**
> 获取随机数

**keylen** _handle_
> 获取当前加密密钥长度

**coldreset**
> 执行冷复位

**warmreset**
> 执行热复位

**disabletx**
> 禁用发射器

**enabletx**
> 启用发射器

**singlechan** _channel_
> 将射频锁定在指定信道上

**hoppingon**
> 恢复跳频

**radiotest** _test_
> 运行射频测试（测试 4、6 和 7 为发射测试）

**psget** _key_
> 读取某个 PS 键的值

**psset** _key_ _value_
> 设置某个 PS 键的值

**psclr** _key_
> 清除某个 PS 键的值

**pslist**
> 列出所有 PS 键

**psread**
> 读取所有 PS 键

**psload** _file_
> 从 PSR 文件加载所有 PS 键

**pscheck** _file_
> 检查 PSR 文件的语法

# CAVEATS

仅适用于基于 CSR 的蓝牙芯片组。修改 PS 键可能改变设备行为，包括蓝牙地址。部分命令需要特定的传输连接。更改设备设置可能导致保修失效。

# SEE ALSO

[hciconfig](/man/hciconfig)(1), [hcitool](/man/hcitool)(1), [bluetoothctl](/man/bluetoothctl)(1)

# RESOURCES

```[Source code](https://github.com/bluez/bluez)```

<!-- verified: 2026-06-19 -->
