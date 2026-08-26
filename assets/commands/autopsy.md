# TAGLINE

基于 Web 的数字取证分析界面

# TLDR

**启动** Autopsy 服务器

```autopsy```

在**指定端口**启动

```autopsy -p [9999]```

限制访问来自**特定主机**

```autopsy [localhost]```

指定**证据柜**目录

```autopsy -d [path/to/locker]```

# SYNOPSIS

**autopsy** [_-c_] [_-C_] [_-d evid_locker_] [_-i device filesystem mnt_] [_-p port_] [_addr_]

# DESCRIPTION

**autopsy** 是 The Sleuth Kit 取证分析工具的图形界面。它启动一个本地 Web 服务器，提供基于浏览器的界面，用于磁盘分析、文件恢复和取证调查。

该工具让调查人员无需命令行知识即可分析文件系统、恢复已删除的文件、创建时间线和搜索证据。

# PARAMETERS

**-p** _port_
> HTTP 服务器端口（默认：9999）

**-c**
> 强制在 URL 中包含 cookie（即使对 localhost 也如此）

**-C**
> 强制 URL 中不含 cookie

**-d** _dir_
> 指定证据柜目录（覆盖默认值）

**-i** _device filesystem mnt_
> 启用实时分析模式（需指定设备、文件系统类型和挂载点）

_addr_
> 用于限制哪些客户端可以连接的 IP 地址或主机名

# FEATURES

- 文件系统分析
- 已删除文件的恢复
- 时间线创建
- 关键字搜索
- 哈希过滤
- 镜像挂载

# CAVEATS

仅限经授权的取证调查使用。Web 界面需要浏览器。这是旧版本（v2）；Autopsy 4 是独立的 Java 桌面应用。必须先安装 The Sleuth Kit 工具。

# HISTORY

**Autopsy** 由 **Brian Carrier** 创建，作为 The Sleuth Kit 的 Web 前端，于 **2001 年**首次发布。第 4 版（2015 年）转为 Java 桌面应用。

# INSTALL

```aur: yay -S autopsy```

```nix: nix profile install nixpkgs#autopsy```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[foremost](/man/foremost)(1), [bulk_extractor](/man/bulk_extractor)(1)
