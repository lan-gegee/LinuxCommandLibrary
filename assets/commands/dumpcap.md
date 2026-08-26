# TAGLINE

网络数据包捕获引擎

# TLDR

**在默认接口上捕获**

```dumpcap -i [eth0] -w [capture.pcapng]```

**列出可用接口**

```dumpcap -D```

**使用环形缓冲区捕获**

```dumpcap -i [eth0] -b filesize:100000 -w [capture.pcapng]```

**带时长限制捕获**

```dumpcap -i [eth0] -a duration:60 -w [capture.pcapng]```

**不使用混杂模式捕获**（默认是开启的）

```dumpcap -i [eth0] -p -w [capture.pcapng]```

**带数据包数量限制捕获**

```dumpcap -i [eth0] -c [1000] -w [capture.pcapng]```

**应用捕获过滤器**

```dumpcap -i [eth0] -f "[tcp port 443]" -w [capture.pcapng]```

# SYNOPSIS

**dumpcap** [_options_]

# PARAMETERS

**-i** _interface_
> 要捕获的接口。可重复使用以同时在多个接口上捕获。

**-w** _file_
> 将数据包写入此文件。用 **-** 表示标准输出。

**-D**
> 列出可用接口并退出。

**-L**
> 列出接口支持的链路层类型并退出。

**-c** _count_
> 捕获指定数量的数据包后停止。

**-a** _condition_:_value_
> 自动停止条件：**duration**:_secs_、**filesize**:_kB_、**files**:_n_ 或 **packets**:_n_。

**-b** _condition_:_value_
> 环形缓冲区：在 **filesize**:_kB_、**duration**:_secs_、**interval**:_secs_ 或 **packets**:_n_ 条件下轮转到新文件，最多保留 **files**:_n_ 个文件。

**-f** _filter_
> BPF 语法的捕获过滤器。在内核中过滤远比全部捕获之后再丢弃便宜。

**-p**
> **不要**将接口置于混杂模式。混杂模式默认开启，所以这个标志的作用是关闭它。

**-s** _snaplen_
> 快照长度：每个数据包捕获的字节数。适合只保留头部而丢弃载荷。

**-P**
> 以 pcap 格式而非默认的 pcapng 格式写入输出。

**-q**
> 安静：不打印不断增长的数据包计数。

# DESCRIPTION

**dumpcap** 是 Wireshark 项目的网络流量捕获工具。它捕获数据包并以 pcapng 或 pcap 格式写入文件。与 Wireshark 或 tshark 不同，dumpcap 只专注于捕获，不做协议解析。

它存在的全部理由就是**权限分离**。捕获数据包需要提升的权限，而解析数据包意味着让庞大的解析代码处理来自网络的恶意输入——这是你最不想赋予特权的事情。因此 Wireshark 和 tshark 并不自己捕获：它们以一个独立的小型特权辅助程序运行 dumpcap，再以非特权身份读回结果。直接运行 dumpcap 不过是单独使用那个辅助程序而已。

由于不做任何解析，它也是整个工具套件中最快的捕获路径，是在长时间运行或高速率捕获（tshark 会丢包）场景下的正确选择。

# RING BUFFER

每 100 MB 轮转到新文件，保留最近的 10 个：

```dumpcap -i [eth0] -b filesize:100000 -b files:10 -w [capture.pcapng]```

这是持续捕获而不填满磁盘的标准做法：每打开一个新文件就丢弃最旧的文件。注意 **filesize** 的单位是 **kB**，所以 `filesize:100000` 约为 100 MB，而不是 100 kB。

# CAVEATS

捕获需要 root 权限，或给二进制文件赋予 `CAP_NET_RAW` 和 `CAP_NET_ADMIN` 能力。发行版通常把 dumpcap 安装为具备 setuid 能力并将其限制在 `wireshark` 组内；把自己加入该组是无 root 捕获的受支持方式，这也是以 root 运行 `wireshark` 既无必要又不明智的原因。

注意这个反向的标志：**-p** 是*禁用*混杂模式的，后者默认开启。另外，混杂模式在交换网络中的作用远小于人们的预期——在这种网络里你无论如何都能看到自己的流量和广播，想看到别人的流量则需要镜像端口或分流器（tap）。

请用 **-f** 而不是稍后过滤。捕获过滤器会被编译成 BPF 在内核中运行，不需要的数据包根本不会被复制到用户空间；而 Wireshark 里的显示过滤器要等数据包写入磁盘之后才把它们丢弃。

在繁忙的链路上，捕获文件的增长速度快得惊人。环形缓冲区、快照长度，或两者兼用，决定了你得到的是一次有用的捕获还是一块写满的磁盘。

# HISTORY

dumpcap 是 **Wireshark** 项目的一部分，该项目由 **Gerald Combs** 于 **1998 年**以 **Ethereal**之名启动。协议解析器长期接连曝出安全公告，使"特权单体"的风险变得难以承受之后，它才从主应用中拆分出来：拆分后只有实际接触网络的那几百行代码以提升权限运行，数百万行的协议解析代码则不然。

# INSTALL

```apt: sudo apt install wireshark-common```

```apk: sudo apk add wireshark-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1), [tcpdump](/man/tcpdump)(1), [editcap](/man/editcap)(1)

# RESOURCES

```[Source code](https://gitlab.com/wireshark/wireshark)```

```[Homepage](https://www.wireshark.org)```

```[Documentation](https://www.wireshark.org/docs/man-pages/dumpcap.html)```

<!-- verified: 2026-07-14 -->
