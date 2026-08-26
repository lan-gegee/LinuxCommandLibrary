# TAGLINE

显示硬件传感器读数

# TLDR

**显示**所有传感器芯片的当前读数

```sensors```

**以华氏度显示**温度

```sensors --fahrenheit```

**以原始格式显示**输出

```sensors -u```

**仅显示**特定芯片

```sensors [chip_name]```

# SYNOPSIS

**sensors** [_options_] [_chip_...]

# PARAMETERS

**-f, --fahrenheit**
> 以华氏度显示温度

**-u**
> 原始输出格式

**-A**
> 不显示芯片适配器

**-j**
> 以 JSON 格式输出

**--no-adapter**
> 不显示适配器信息

# DESCRIPTION

**sensors** 显示 libsensors 支持的所有传感器芯片的当前读数。这包括 CPU 温度、风扇转速、电压以及其他硬件监控数据。

输出按芯片组织，显示适配器类型以及各个传感器的读数，包括当前值、限制值和报警状态。

# CONFIGURATION

**/etc/sensors3.conf**
> libsensors 的主配置文件，定义针对特定芯片的标签覆盖、计算表达式和报警限制。

**/etc/sensors.d/**
> 存放额外传感器配置文件的目录，用于补充主配置。

# CAVEATS

需要 lm-sensors 软件包。请先运行 **sensors-detect** 来检测并配置可用的传感器。部分传感器可能需要加载内核模块。属于 lm-sensors 软件包的一部分。

# INSTALL

```apt: sudo apt install lm-sensors```

```apk: sudo apk add lm-sensors```

```zypper: sudo zypper install sensors```

```brew: brew install lm-sensors```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sensors-detect](/man/sensors-detect)(8)
