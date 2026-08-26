# TAGLINE

显示 BitTorrent .torrent 文件的元数据

# TLDR

**显示种子文件信息**

```btshowmetainfo [file.torrent]```

**显示多个种子的详细信息**

```btshowmetainfo [file1.torrent] [file2.torrent]```

# SYNOPSIS

**btshowmetainfo** _torrent_file_...

# DESCRIPTION

**btshowmetainfo** 显示 BitTorrent .torrent 文件中的元数据。它展示种子的关键信息，包括 announce URL（tracker）、文件名、大小、分片长度和 info hash。

该工具解析 bencode 编码的种子文件，并以人类可读的格式呈现信息。对于多文件种子，它会列出其中所有文件及其各自的大小。info hash 在整个 BitTorrent 网络中唯一标识一个种子。

显示的信息包括：
- **Announce URL**：tracker 服务器地址
- **Name**：种子名称（多文件种子为目录名）
- **Files**：文件列表及大小
- **Piece length**：用于完整性检查的每个分片的大小
- **Info hash**：唯一的种子标识符

# CAVEATS

该工具属于最初的 BitTorrent 客户端软件包，现代系统上可能默认未安装。**transmission-show** 或 **aria2c --show-files** 等替代工具提供类似功能。它只显示静态元数据；无法获知做种者/下载者数量或下载状态。

# HISTORY

btshowmetainfo 随 **Bram Cohen** 编写的最初 **BitTorrent** 客户端一同发布。Cohen 于 **2001 年**发明了 BitTorrent 协议，该工具是用于演示和调试协议的参考实现的一部分。虽然原版客户端已被功能更丰富的替代品取代，这些实用工具在查看种子文件方面仍然有用。

# SEE ALSO

[transmission-show](/man/transmission-show)(1), [aria2c](/man/aria2c)(1), [qbittorrent](/man/qbittorrent)(1)

# RESOURCES

```[Source code](https://github.com/effigies/BitTornado)```

<!-- verified: 2026-06-22 -->
