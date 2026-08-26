# TAGLINE

使用 c-ares 库的 DNS 查询工具

# TLDR

显示主机名的 **A 记录**（默认）

```adig [example.com]```

显示额外的**调试**输出

```adig -d [example.com]```

连接到**指定的 DNS 服务器**

```adig -s [1.2.3.4] [example.com]```

使用指定的 **TCP 端口**连接 DNS 服务器

```adig -T [port] [example.com]```

使用指定的 **UDP 端口**连接 DNS 服务器

```adig -U [port] [example.com]```

# SYNOPSIS

**adig** [_-d_] [_-s server_] [_-T port_] [_-U port_] [_-t type_] _hostname_

新版 c-ares（1.34 及更高版本）：

**adig** [_@server_] [_-c class_] [_-p port_] [_-q name_] [_-t type_] [_-x addr_] _name_ [_type_] [_class_]

# DESCRIPTION

**adig** 打印从域名系统（DNS）服务器接收到的信息。它执行 DNS 查询并显示结果，与 **dig** 类似，但构建在 c-ares 异步解析器库之上。

该工具支持查询特定记录类型，如 A、AAAA、MX、NS、CNAME、SOA 等。它可以把查询定向到某个特定 DNS 服务器，并为连接使用自定义端口号。还提供调试输出，便于排查解析问题。

从 c-ares 1.34 起，命令行界面经过重构以高度模仿 BIND 的 **dig**，因此服务器需以 **@server** 形式给出；下面列出的旧式 **-d**、**-T** 和 **-U** 标志适用于更早的版本。

# PARAMETERS

**-d**
> 显示额外的调试输出（旧接口）

**-s server**
> 连接到指定的 DNS 服务器 IP 地址。c-ares 1.34 及更高版本建议改用 **@server** 语法

**-T port**
> 使用指定的 TCP 端口连接 DNS 服务器（旧接口）

**-U port**
> 使用指定的 UDP 端口连接 DNS 服务器（旧接口）

**-p port**
> 将查询发送到 53 以外的端口（c-ares 1.34 及更高版本）

**-t type**
> 查询特定记录类型（A、AAAA、MX、NS 等）

**-c class**
> 设置查询类别；默认为 IN，也可以是 HS 或 CH（c-ares 1.34 及更高版本）

**-x addr**
> 执行简化的反向查询：把类型设为 PTR 并构造 in-addr.arpa 查询字符串（c-ares 1.34 及更高版本）

# CAVEATS

属于 c-ares 库的工具集。与 BIND 中更常用的 **dig** 命令相比，功能可能有所差异。不同版本的标志集合并不相同：c-ares 1.34 重构了接口以对齐 **dig**，取代了旧的 **-d**、**-T** 和 **-U** 选项。

# HISTORY

属于 **c-ares** 异步 DNS 解析器库，最初从 ares 库分叉而来，目前持续活跃维护。在 1.34.0 版本中，**adig** 的命令行参数被重构以模仿 BIND 的 **dig**，同时该工具新增了从 **~/.adigrc** 文件读取默认参数的支持。

# INSTALL

```apk: sudo apk add c-ares-utils```

```zypper: sudo zypper install c-ares-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ahost](/man/ahost)(1), [acountry](/man/acountry)(1), [dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1)

# RESOURCES

```[Source code](https://github.com/c-ares/c-ares)```

```[Homepage](https://c-ares.org/)```

<!-- verified: 2026-06-11 -->
