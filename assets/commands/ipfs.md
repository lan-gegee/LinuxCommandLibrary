# TAGLINE

星际文件系统（IPFS）分布式点对点命令行工具

# TLDR

**初始化 IPFS 仓库**

```ipfs init```

**启动 IPFS 守护进程**

```ipfs daemon```

**将文件添加到 IPFS**

```ipfs add [file]```

**递归添加目录**

```ipfs add -r [directory]```

**按 CID 获取文件**

```ipfs get [CID]```

**查看文件内容**

```ipfs cat [CID]```

**固定一个文件**

```ipfs pin add [CID]```

**列出已固定的文件**

```ipfs pin ls```

**显示节点信息**

```ipfs id```

# SYNOPSIS

**ipfs** _command_ [_options_]

# SUBCOMMANDS

**init**
> 初始化本地仓库。

**daemon**
> 启动 IPFS 守护进程。

**add** _file_
> 将文件添加到 IPFS。

**get** _cid_
> 按 CID 下载文件。

**cat** _cid_
> 显示文件内容。

**pin add** _cid_
> 在本地固定内容。

**pin ls**
> 列出已固定的内容。

**id**
> 显示节点身份信息。

**swarm peers**
> 列出已连接的对等节点。

**files**
> 管理 MFS（可变文件系统）。

# PARAMETERS

**-r**, **--recursive**
> 递归添加目录。

**-q**, **--quiet**
> 精简输出。

**-w**, **--wrap-with-directory**
> 将文件包装进目录。

# DESCRIPTION

**ipfs** 是 **Kubo** 实现（InterPlanetary File System，星际文件系统）的命令行界面。IPFS 是一种点对点的内容寻址存储与分发网络。每个文件或块都由基于其内容加密哈希派生的 CID（Content Identifier，内容标识符）标识，因此相同的数据可以从任何持有它的节点获取，无需固定的主机或 URL。

本地 **ipfs daemon** 充当用户与全球 IPFS 群集之间的网关：它连接对等节点、抓取数据块、固定内容以便长期保留，并同时提供 HTTP 网关和 JSON-RPC API。**add** 子命令将文件存入本地数据存储并输出得到的 CID；**cat** 和 **get** 用于检索内容；**pin add** 防止内容被垃圾回收；**files** 则在不可变的 IPLD 对象之上提供一个类似 POSIX 的可变文件系统（MFS）。

# CAVEATS

大多数子命令都需要守护进程正在运行；每位用户必须先执行一次 **ipfs init** 以在 **~/.ipfs/** 中创建配置。内容默认不是私有的——任何知道 CID 的人都可以通过任意 IPFS 节点获取底层数据。默认端口分配（群集 4001 TCP/UDP、API 5001、网关 8080）需要考虑防火墙设置以获得良好的连通性。

# HISTORY

**IPFS** 由 **Protocol Labs** 的 **Juan Benet** 在 **2014 年**的白皮书中提出。首个 Go 参考实现（后更名为 **Kubo**）于 **2016 年**发布 **0.4.0** 版本，并于 **2023 年**达到 **1.0.0**。随后出现了 Rust 实现（**iroh**）和 JavaScript 实现（**js-ipfs**，后更名 **Helia**）。

# INSTALL

```pacman: sudo pacman -S kubo```

```apk: sudo apk add kubo```

```zypper: sudo zypper install kubo```

```brew: brew install kubo```

```nix: nix profile install nixpkgs#kubo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [rsync](/man/rsync)(1)
