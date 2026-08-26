# TAGLINE

快速扫描本地网络中主机、厂商和服务的 TUI 扫描器

# TLDR

**启动交互式 TUI**并选择网络接口

```nibble```

在无头模式下扫描**指定子网**

```nibble -i [192.168.1.0/24]```

扫描从文件读取的**多个目标**

```nibble -i [targets.txt]```

将扫描限制在**自定义端口范围**

```nibble -i [192.168.1.0/24] -p [22,80,443,8000-8100]```

扫描单台主机的**全部 65535 个端口**

```nibble -i [192.168.1.10/32] -p -```

将结果写入 **JSON 文件**而非标准输出

```nibble -i [10.0.0.0/24] -o [results.json]```

# SYNOPSIS

**nibble** [**-i** _targets_] [**-p** _ports_] [**-o** _file_]

# DESCRIPTION

**nibble** 是一款单二进制文件的本地网络扫描器，带有可用鼠标点击的终端用户界面。不带参数运行时，它会请你选择一个网络接口，然后扫描所在子网内的存活主机，利用内置的 4 万条目数据库把每个 MAC 地址映射到最可能的设备厂商，探测常见 TCP 端口，并读取服务横幅（banner）来识别每个开放端口背后的软件。结果展示在一个对鼠标友好的 TUI 中，还支持回查历史扫描记录。

在无头模式下（给定 **-i**、**-p** 或 **-o** 任意参数），**nibble** 会以非交互方式运行，并把 JSON 写入标准输出或 **-o** 指定的文件，因而适合编写脚本。它可以在 Linux、macOS 和 Windows 上运行，包括 Docker 和 WSL 环境，并且不需要 root 或管理员权限。

# PARAMETERS

**-i** _targets_
> 要扫描的 IP 或 CIDR 范围（逗号分隔），或者一个文件路径，文件中每行一个目标。

**-p** _ports_
> 自定义端口规格。接受逗号分隔的列表和范围（例如 **22,80,8000-8100**），或用 **-** 表示所有端口。

**-o** _file_
> 将扫描结果以 JSON 写入 _file_，而不是打印到屏幕。

# CAVEATS

探测**仅支持 TCP**；DNS、SNMP 等 UDP 服务不会被检出。抓取服务横幅可能触发受监控网络上的入侵检测系统——请只扫描你有权评估的网络。厂商识别依赖随附的 OUI 列表，对于伪装 MAC 地址的设备可能识别错误。

# HISTORY

**nibble** 由 **backendsystems** 团队于 **2025 年**发布在 **GitHub 上**，定位于日常局域网侦察场景中 **nmap** 的小巧快速替代品。它可通过 **apt**、**dnf**、**brew**、**winget**、**npm**、**pip** 和 **go install** 分发渠道获取，另附三大平台的预编译二进制文件。

# SEE ALSO

[nmap](/man/nmap)(1), [arp-scan](/man/arp-scan)(1), [masscan](/man/masscan)(1), [netdiscover](/man/netdiscover)(8)
