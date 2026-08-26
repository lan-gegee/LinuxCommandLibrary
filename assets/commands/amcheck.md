# TAGLINE

在备份运行前验证 Amanda 备份配置

# TLDR

为某个配置**运行全部检查**（客户端与服务器）

```amcheck [config_name]```

仅**运行服务器端检查**（本地与磁带）

```amcheck -s [config_name]```

仅**运行客户端主机检查**

```amcheck -c [config_name]```

在服务器上**运行本地测试**（权限等）

```amcheck -l [config_name]```

在服务器上**运行磁带测试**

```amcheck -t [config_name]```

仅**检查特定客户端**

```amcheck -c [config_name] [client1] [client2]```

**覆盖某个配置选项**

```amcheck -o [tapetype=EXABYTE] [config_name]```

# SYNOPSIS

**amcheck** [**-am**] [**-w**] [**-sclt**] [**-M** _address_] [**--client-verbose**] [**-o** _configoption_] _config_ [_host_ [_disk_]...]

# PARAMETERS

**-s**
> 运行服务器端检查（等同于 -lt）

**-c**
> 运行客户端主机检查；可选指定具体客户端

**-l**
> 在服务器主机上运行本地测试（权限、配置）

**-t**
> 在服务器主机上运行磁带测试（确认已装入正确的磁带）

**-m**
> 通过电子邮件将结果发送到 amanda.conf 中指定的地址

**-M** _address_
> 将结果发送到指定的电子邮件地址

**-w**
> 启用更彻底的磁带检查，会覆盖磁带标签

**-a**
> 客户端检查失败时跳过

**--client-verbose**
> 打印详细的客户端输出

**-o** _name=value_
> 覆盖 amanda.conf 中的某个配置选项

_config_
> 要检查的 Amanda 配置名称

_host_
> 要检查的特定客户端主机名

_disk_
> 要检查的特定磁盘表达式

# DESCRIPTION

**amcheck** 在备份运行前对 Amanda 备份服务器和客户端主机执行自检。它有助于发现可能导致备份失败的问题，例如磁带装入错误、权限问题或客户端不可达。

在服务器端，amcheck 会验证下一次计划备份是否装入了正确的磁带，并检查本地配置和权限。在客户端主机上，它会确认 Amanda 客户端守护进程正在运行，且备份服务器拥有访问计划备份文件系统的适当权限。

该工具通常在计划备份之前运行，或由管理员手动运行以验证备份基础设施就绪。结果显示在标准输出上，也可通过 **-m** 选项以电子邮件发送。默认行为是同时运行客户端和服务器检查（**-cs**）。

客户端检查具有可配置的超时时间（默认 30 秒），由 amanda.conf 中的 **ctimeout** 设置控制。

# CONFIGURATION

**/etc/amanda/<config>/amanda.conf**
> Amanda 服务器配置，定义磁带设备、暂存盘、转储类型和调度参数。

**/etc/amanda/<config>/disklist**
> 要备份的客户端主机和文件系统列表。

# CAVEATS

**-w** 选项会执行破坏性磁带检查并覆盖磁带标签；请谨慎使用。客户端检查需要网络连通性以及客户端上正在运行的 amandad 服务。服务器检查需要访问磁带设备和配置文件的适当权限。

# HISTORY

Amanda（Advanced Maryland Automatic Network Disk Archiver）由 James da Silva 于 **1991** 年起在**马里兰大学**开发。它是 Unix 系统上使用最广泛的开源备份解决方案之一。该项目由 Amanda 社区和 **Zmanda**（后被 Carbonite 收购）维护，目前仍在积极开发中。

# INSTALL

```apt: sudo apt install amanda-server```

```dnf: sudo dnf install amanda-server```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amdump](/man/amdump)(8), [amrecover](/man/amrecover)(8)
