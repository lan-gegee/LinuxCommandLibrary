# TAGLINE

基于温度的自动风扇转速控制

# TLDR

使用**默认**配置文件启动（/etc/fancontrol）

```sudo fancontrol```

使用**自定义**配置文件启动

```sudo fancontrol [path/to/config_file]```

# SYNOPSIS

**fancontrol** [_config_file_]

# PARAMETERS

_config_file_
> 配置文件路径（默认：/etc/fancontrol）。

# DESCRIPTION

**fancontrol** 是 lm-sensors 软件包中的一个 shell 脚本，基于温度读数自动管理风扇转速。它从配置文件读取设置，根据温度计算风扇转速，并将相应的 PWM 输出设置为计算出的值。

该守护进程持续监控硬件温度传感器，并调整 PWM 控制的风扇以维持预期的温度水平。配置通常由 pwmconfig 工具生成：它会检测可用的风扇和传感器，然后创建相应的映射关系和阈值。

# CONFIGURATION

**/etc/fancontrol**
> 主配置文件，包含以下关键变量：

**FCTEMPS**
> 将 PWM 输出映射到温度传感器。

**FCFANS**
> 将 PWM 输出与用于监控的风扇转速输入关联。

**MINTEMP / MAXTEMP**
> 用于风扇转速计算的温度区间。

**MINPWM / MAXPWM**
> 与温度区间对应的 PWM 取值范围。

**MINSTART**
> 风扇开始转动的最小 PWM 值。

**MINSTOP**
> 风扇仍在转动的最小 PWM 值（低于此值风扇停止）。

**AVERAGE**
> 参与平均的温度读数个数（默认：1，不做平均）。

# CAVEATS

需要已配置好的硬件监控（lm-sensors）。请先运行 pwmconfig 来检测风扇和传感器并生成配置文件。由于要访问硬件 PWM 控制，需要 root 权限。守护进程默认在前台运行；要用 systemd 服务或 init 脚本将其作为后台服务运行。

# INSTALL

```apk: sudo apk add lm-sensors-fancontrol```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sensors](/man/sensors)(1), [hwinfo](/man/hwinfo)(1)
