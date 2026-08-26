# TAGLINE

快速的增量文件传输与同步工具

# TLDR

**将本地目录同步到另一位置**

```rsync -av [source/] [destination/]```

**通过 SSH 同步到远程服务器**

```rsync -av [source/] [user]@[host]:[destination/]```

**从远程服务器同步**

```rsync -av [user]@[host]:[source/] [destination/]```

**删除目标中**源里没有的文件

```rsync -av --delete [source/] [destination/]```

**试运行**以预览更改

```rsync -avn [source/] [destination/]```

传输时**显示进度**

```rsync -av --progress [source/] [destination/]```

**排除匹配某模式的文件**

```rsync -av --exclude="*.log" [source/] [destination/]```

传输过程中**压缩数据**（适合慢速网络）

```rsync -avz [source/] [user]@[host]:[destination/]```

# SYNOPSIS

**rsync** [_options_] _source_... _destination_

# PARAMETERS

**-a**, **--archive**
> 归档模式；等同 -rlptgoD（递归、链接、权限、时间戳、组、所有者、设备文件）

**-v**, **--verbose**
> 输出更详细的信息

**-z**, **--compress**
> 传输期间压缩文件数据

**-n**, **--dry-run**
> 显示将要传输的内容但不实际改动

**--delete**
> 删除目标中不存在于源里的文件

**--exclude**=_pattern_
> 排除匹配模式的文件

**--include**=_pattern_
> 包含匹配模式的文件（在排除规则之后生效）

**--progress**
> 传输期间显示进度

**-P**
> 等同于 --partial --progress

**--partial**
> 保留传输了一部分的文件

**-r**, **--recursive**
> 递归进入子目录

**-u**, **--update**
> 跳过目标端较新的文件

**-c**, **--checksum**
> 按校验和而非修改时间与大小进行比较

**-e** _command_
> 指定要使用的远程 shell（例如 -e ssh）

**--bwlimit**=_KBPS_
> 限制带宽（KB/s）

**-h**, **--human-readable**
> 以人类可读的格式输出数字

# DESCRIPTION

**rsync** 是一款快速而多功能的文件复制工具，可在不同位置之间同步文件。它使用增量传输算法，只传输源和目标之间的差异，因此在增量备份和镜像场景下非常高效。

源路径末尾的斜杠非常关键：**source/** 复制的是目录内容，而 **source** 复制的是目录本身。这是一个常见的困惑点。

rsync 既能在本地工作，也能通过网络使用 SSH（默认）、RSH 或其自身的守护进程协议。远程传输的写法是 **user@host:path**；守护进程模式则为 **rsync://user@host/path**。

**-a**（归档）标志最常被使用，因为它会保留权限、时间戳和符号链接，并递归处理目录——适合大多数备份场景。

# CAVEATS

**结尾斜杠很重要**：**rsync -a source/ dest/** 复制内容；**rsync -a source dest/** 则把整个目录复制到 dest 里。

**--delete** 会从目标端删除文件。请务必先加 **-n**（试运行）确认将要删除哪些内容。

符号链接默认按链接本身复制。如需跟随符号链接并复制其指向的目标，请使用 **-L**。

在不稳定的连接上传输大量数据时，使用 **-P**（--partial --progress）可以支持中断续传。

# HISTORY

Rsync 由 **Andrew Tridgell** 和 **Paul Mackerras** 于 **1996 年**创建，名字来自 "remote sync"。增量传输算法源自 Tridgell 的博士论文。Rsync 已成为 Unix 系统管理、备份与镜像工作的基础工具。

# INSTALL

```apt: sudo apt install rsync```

```dnf: sudo dnf install rsync```

```pacman: sudo pacman -S rsync```

```apk: sudo apk add rsync```

```zypper: sudo zypper install rsync```

```brew: brew install rsync```

```nix: nix profile install nixpkgs#rsync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [cp](/man/cp)(1), [rclone](/man/rclone)(1), [tar](/man/tar)(1)
