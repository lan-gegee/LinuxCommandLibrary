# TAGLINE

通过 S.M.A.R.T. 显示硬盘温度

# TLDR

显示 SATA 硬盘的**温度**

```hddtemp SATA:/dev/sda```

以**华氏度**显示

```hddtemp -u F SATA:/dev/sda```

仅显示**数值**

```hddtemp -n SATA:/dev/sda```

每 N 秒记录到 **syslog**

```hddtemp -S 60 SATA:/dev/sda```

读取温度前先**唤醒**硬盘

```hddtemp -w SATA:/dev/sda```

以**守护进程**模式运行

```hddtemp -d SATA:/dev/sda```

显示**调试**信息

```hddtemp -D SATA:/dev/sda```

# SYNOPSIS

**hddtemp** [_options_] [_type_]:_device_

# DESCRIPTION

**hddtemp** 通过 S.M.A.R.T.（Self-Monitoring, Analysis and Reporting Technology，自我监测、分析及报告技术）显示硬盘温度。它可以显示支持 S.M.A.R.T. 的 SATA、PATA 和 SCSI 硬盘的温度。

# PARAMETERS

**-n, --numeric**
> 只打印数字形式的温度值，不带单位

**-u, --unit=UNIT**
> 设置温度单位（C 为摄氏度，F 为华氏度）

**-S, --syslog=SECONDS**
> 每 N 秒把温度记录到 syslog

**-d, --daemon**
> 以守护进程方式运行（TCP/IP 服务器模式）

**-l, --listen=ADDR**
> 守护进程模式下监听指定地址

**-p, --port=PORT**
> 守护进程模式下监听指定端口（默认：7634）

**-w, --wake-up**
> 读取温度前先唤醒硬盘

**-q, --quiet**
> 抑制硬盘型号兼容性警告

**-D, --debug**
> 显示 S.M.A.R.T. 字段及其取值

**-f, --file=FILE**
> 使用指定的硬盘数据库文件

# CAVEATS

访问硬盘的 S.M.A.R.T. 数据需要 root 权限。必须提供硬盘类型前缀（SATA、PATA、SCSI）才能正常工作。并非所有硬盘都支持通过 S.M.A.R.T. 监测温度。

# HISTORY

**hddtemp** 的开发目标是利用 S.M.A.R.T. 数据为硬盘提供简单的温度监测，常用于系统健康监控。

# INSTALL

```dnf: sudo dnf install hddtemp```

```pacman: sudo pacman -S hddtemp```

```nix: nix profile install nixpkgs#hddtemp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smartctl](/man/smartctl)(8), [sensors](/man/sensors)(1)
