# TAGLINE

显示种子文件的元数据

# TLDR

**显示种子信息**

```transmission-show [file.torrent]```

**显示磁力 URI**

```transmission-show -m [file.torrent]```

**显示文件列表**

```transmission-show -f [file.torrent]```

**仅显示 info hash**

```transmission-show -i [file.torrent]```

**显示总大小**

```transmission-show -s [file.torrent]```

**向 tracker 查询节点数量**

```transmission-show --scrape [file.torrent]```

# SYNOPSIS

**transmission-show** [_options_] _torrent-file_

# PARAMETERS

**-m**, **--magnet**
> 输出该种子的磁力 URI。

**-i**, **--info**
> 仅输出 info hash。

**-s**, **--size**
> 输出所有文件的总大小。

**-f**, **--files**
> 输出详细的文件列表，包括路径和大小。

**-c**, **--comment**
> 输出元数据中的注释字段。

**-t**, **--tracker**
> 输出 tracker URL 列表。

**--scrape**
> 向 tracker 查询节点数和做种者数量。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**transmission-show** 无需下载或做种即可显示 .torrent 文件中的元数据。它解析种子文件并展示相关信息，包括文件列表、tracker、分块数量、创建日期和 info hash。

该工具适用于在把种子添加到客户端之前进行检查、验证种子内容、提取磁力链接，或编写种子管理脚本。scrape 选项可向 tracker 查询当前的集群统计信息。

输出格式兼顾人类可读性和脚本解析，具体取决于所使用的选项。

# CAVEATS

scrape 查询需要网络访问且 tracker 可用。某些 tracker 可能不支持或不响应 scrape 请求。私有 tracker 可能要求认证才能获取 scrape 数据。

# HISTORY

**transmission-show** 隶属于 Transmission BitTorrent 客户端套件，提供对种子文件的命令行检查能力。Transmission 创建于 2005 年，其命令行工具支持自动化和无头服务器运行。

# INSTALL

```apt: sudo apt install transmission-cli```

```dnf: sudo dnf install transmission-cli```

```pacman: sudo pacman -S transmission-cli```

```apk: sudo apk add transmission-extra```

```brew: brew install transmission-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-create](/man/transmission-create)(1), [transmission-daemon](/man/transmission-daemon)(1), [transmission-remote](/man/transmission-remote)(1)
