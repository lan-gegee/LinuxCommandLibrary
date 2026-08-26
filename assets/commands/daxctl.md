# TAGLINE

管理 Device DAX 与持久内存的工具

# TLDR

**列出所有 DAX 设备和区域**

```daxctl list```

**列出设备并包含区域信息等详细输出**

```daxctl list -d -r```

**将设备重新配置为 system-ram 模式**

```daxctl reconfigure-device --mode=system-ram [dax0.0]```

**重新配置为 devdax 模式**

```daxctl reconfigure-device --mode=devdax [dax0.0]```

**将 system-ram 模式设备的内存上线**

```daxctl online-memory [dax0.0]```

**将 system-ram 模式设备的内存下线**

```daxctl offline-memory [dax0.0]```

**启用 devdax 设备**

```daxctl enable-device [dax0.0]```

**禁用 devdax 设备**

```daxctl disable-device [dax0.0]```

# SYNOPSIS

**daxctl** _command_ [_options_] [_device_]

# PARAMETERS

**list** [_options_]
> 以 JSON 格式列出 DAX 设备和区域。

**reconfigure-device** _device_
> 更改设备模式（devdax 或 system-ram）。

**online-memory** _device_
> 将 DAX 内存上线供系统使用（设备必须处于 system-ram 模式）。

**offline-memory** _device_
> 将 DAX 内存下线（设备必须处于 system-ram 模式）。

**enable-device** _device_
> 启用 devdax 设备。

**disable-device** _device_
> 禁用 devdax 设备。

**create-device**
> 在区域内创建新的 devdax 设备。

**destroy-device** _device_
> 销毁 devdax 设备。

**migrate-device-model**
> 选择加入 /sys/bus/dax 设备模型，允许使用替代的 Device-DAX 实例驱动。

**-d**, **--devices**
> 列表中包含设备详情。

**-r**, **--regions**
> 列表中包含区域详情。

**-m**, **--mode** _mode_
> 设备模式：devdax 或 system-ram。

**-s**, **--size** _size_
> 对支持创建设备的区域，设置设备大小（支持 k、m、g、t 后缀）。

**-a**, **--align** _align_
> 设置大页映射的对齐方式（默认：2M）。

**-N**, **--no-online**
> 切换到 system-ram 模式时不自动将内存区段上线。

**--no-movable**
> 将新内存上线为不可移动类型（允许内核使用这块内存）。

**-C**, **--check-config**
> 从全局 daxctl 配置文件读取重配置参数。

**-f**, **--force**
> 强制下线内存区段，或覆盖内核的自动上线策略。

**-u**, **--human**
> 以带单位的人类可读字符串显示存储大小。

**-v**, **--verbose**
> 输出调试消息。

# DESCRIPTION

**daxctl** 管理 Device DAX（Direct Access，直接访问）设备，这类设备提供对持久内存（PMEM）或 CXL 内存区域的直接内存映射访问。它配置这些内存如何呈现给系统。

在 **devdax** 模式下，内存通过字符设备访问，适用于需要直接访问的应用（数据库、内存映射文件）。在 **system-ram** 模式下，内存呈现为普通系统 RAM，任何应用都可使用。

该工具配合 **ndctl**（NVDIMM）或 **cxl**（CXL 内存）创建的区域工作。它是现代服务器系统中管理分离式内存和持久内存的关键工具。

# MODES

**devdax**: 直接字符设备访问（/dev/daxX.Y）
> 用于显式 mmap 该设备的应用程序

**system-ram**: 热插拔的系统内存
> 被视为普通 RAM，任何进程都可使用

# CAVEATS

更改模式可能要求先取消设备的内存映射。system-ram 模式的内存可能与普通 RAM 有不同的 NUMA 特性。需要内核支持 DAX（Device-DAX）。持久内存处于 system-ram 模式时会失去持久化优势。

# HISTORY

daxctl 是 Intel 的 **Dan Williams** 主导的 **ndctl** 项目的一部分。它伴随 Linux 内核自 **2016 年**前后开始的持久内存（NVDIMM）支持一同开发。随着持久内存技术（Intel Optane、CXL 内存）的发展，daxctl 成为了管理这些内存如何与操作系统集成的必备工具。

# INSTALL

```apt: sudo apt install daxctl```

```dnf: sudo dnf install daxctl```

```pacman: sudo pacman -S ndctl```

```apk: sudo apk add ndctl```

```zypper: sudo zypper install ndctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ndctl](/man/ndctl)(1), [cxl](/man/cxl)(1), [numactl](/man/numactl)(8)
