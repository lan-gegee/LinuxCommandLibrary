# TAGLINE

面向终端的现代 BitTorrent 客户端

# TLDR

**启动 TUI 客户端**

```superseedr```

**添加磁力链接**

```superseedr add "[magnet:?xt=urn:btih:...]"```

**添加种子文件**

```superseedr add [/path/to/file.torrent]```

**列出已配置的种子**

```superseedr torrents```

按 info hash **列出一个种子的文件**

```superseedr files [info_hash]```

**优雅地停止正在运行的客户端**

```superseedr stop-client```

# SYNOPSIS

**superseedr** [_command_] [_options_]

# DESCRIPTION

**superseedr** 是一款现代 BitTorrent 客户端，具有高性能的 60 FPS 终端 UI、带带宽图表和对等节点分析功能的实时 swarm 观测，以及 Docker 与 Gluetun VPN 集成。它支持 BitTorrent v2、RSS 订阅跟踪和 40 多个内置主题。

不带参数运行时，**superseedr** 会打开交互式终端 UI。运行期间可以通过粘贴磁力链接或种子路径添加内容，也可以从另一个终端运行 `add` 子命令，输入会被转交给正在运行的实例。其余子命令提供了可脚本化的接口，用于管理种子以及共享/独立配置。在任何子命令后加上 **--json** 即可获得结构化输出。

# COMMANDS

**add** [**--path** _PATH_] [**--validated**] _input_...
> 添加一个或多个种子文件路径或磁力链接。**--path** 为这些输入持久化已有的下载路径；重建目录时，**--validated** 会将数据视为已经校验过。

**torrents**
> 列出已配置的种子。

**info** _info_hash_|_path_
> 按 info hash 或唯一文件路径显示单个种子。

**files** _info_hash_|_path_
> 列出某个种子的文件，包括相对路径和解析后的完整路径。

**stop-client**
> 请求优雅关闭正在运行的客户端。

**to-shared** _PATH_ / **to-standalone**
> 在分层共享配置（以 _PATH_ 为根）和本地独立配置之间互相转换。

# HISTORY

**superseedr** 由 **Jagalite** 创建，使用 **Rust** 编写。可通过 `cargo install superseedr`、Homebrew、AUR 以及各平台安装程序获取。

# INSTALL

```brew: brew install superseedr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [transmission-remote](/man/transmission-remote)(1), [rtorrent](/man/rtorrent)(1), [aria2](/man/aria2)(1), [deluge](/man/deluge)(1)
