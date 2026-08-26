# TAGLINE

自动化多线程网络侦察工具

# TLDR

扫描**目标**主机

```sudo autorecon 192.168.1.1```

从**文件**读取目标进行扫描

```sudo autorecon -t targets.txt```

指定**输出**目录

```sudo autorecon -o /path/to/results 192.168.1.1```

扫描特定**端口**

```sudo autorecon -p T:21-25,80,443,U:53 192.168.1.1```

# SYNOPSIS

**autorecon** [_OPTIONS_] _targets_

# DESCRIPTION

**autorecon** 是一款多线程网络侦察工具，可对服务执行自动化枚举。它并行运行各种扫描工具，并按主机和服务类型整理结果。

该工具先用 **nmap** 进行端口扫描，然后根据检测到的开放端口启动针对特定服务的枚举脚本。结果按目标分别存入各自目录，每个扫描阶段都有结构化的输出。它支持自定义扫描配置档和基于插件的服务枚举，可适配不同的渗透测试方法论。

# PARAMETERS

**-t, --target-file** _file_
> 从文件读取目标

**-o, --output** _dir_
> 将结果输出到指定目录（默认：./results）

**-p, --ports** _ports_
> 将扫描限制到特定端口（T: TCP，U: UDP，B: 两者）

**--single-target**
> 结果直接放入输出目录，而不是为每个目标建子目录

**-v, --verbose**
> 启用详细输出；重复使用（-vv、-vvv）可获得更多细节

**--heartbeat** _seconds_
> 状态更新消息之间的间隔（默认：60）

**-m, --max-scans** _number_
> 并发扫描的最大数量

**--nmap** _options_
> 覆盖用于端口扫描的默认 nmap 选项

# CONFIGURATION

**~/.config/AutoRecon/**
> 存放自定义扫描配置档和插件配置的目录。

# CAVEATS

某些扫描类型需要 root 权限。结果保存到按目标组织的 results 目录中。此工具只能用于你获得扫描授权的系统。

# HISTORY

**autorecon** 为渗透测试和 CTF 竞赛而创建，用于自动化初始侦察阶段。

# SEE ALSO

[nmap](/man/nmap)(1), [nikto](/man/nikto)(1)

# RESOURCES

```[Source code](https://github.com/Tib3rius/AutoRecon)```

<!-- verified: 2026-06-17 -->
