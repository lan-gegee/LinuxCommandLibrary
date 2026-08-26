# TAGLINE

利用 mDNS 发现机制在本地网络的两台机器之间传输管道数据

# TLDR

**等待**对等端连接（将收到的数据打印到 stdout）

```airpaste```

向等待中的对等端发送**文本**

```echo "Hello" | airpaste```

发送一个**文件**

```airpaste < [file.txt]```

接收并**保存**到文件

```airpaste > [received.txt]```

使用**命名通道**，只有同名对等端才会互相连接

```airpaste [channel_name]```

# SYNOPSIS

**airpaste** [_name_]

# DESCRIPTION

**airpaste** 是一条一对一的网络管道，它使用 mDNS（多播 DNS）自动发现同一本地网络上的另一个对等端，因此你不需要知道对方机器的 IP 地址。数据通过 TCP 传输。

在两台机器上运行 **airpaste**：凡是输入到其中一端的数据都会流式传输到另一端。可以传入一个可选的通道名称，使只有使用相同名称的对等端互相连接。它可以跨不同操作系统工作，并且无需任何服务器设置。

# PARAMETERS

_name_
> 可选的通道名称；只有使用相同名称的对等端才会互相连接

# CAVEATS

只能在 mDNS 多播可达的本地网络上工作。数据在网络中明文传输且可能被截获，因此仅适合在可信网络中使用。它一次只连接两个对等端，不支持一对多广播。

# HISTORY

**airpaste** 由 Mathias Buus（mafintosh）创建，作为开发期间在机器之间传输数据和文件的简便方式，借助 mDNS 实现零配置组网。它用 JavaScript 编写并通过 npm 分发。

# SEE ALSO

[nc](/man/nc)(1), [wormhole](/man/wormhole)(1), [croc](/man/croc)(1)

# RESOURCES

```[Source code](https://github.com/mafintosh/airpaste)```

```[Homepage](https://github.com/mafintosh/airpaste)```

<!-- verified: 2026-06-11 -->
