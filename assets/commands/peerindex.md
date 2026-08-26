# TAGLINE

从 BitTorrent 文件中提取并分析节点信息

# TLDR

**分析种子节点数据**

```peerindex [file.torrent]```

**显示详细输出**

```peerindex -v [file.torrent]```

**导出节点列表**

```peerindex -o [peers.txt] [file.torrent]```

**分析多个种子**

```peerindex [file1.torrent] [file2.torrent]```

# SYNOPSIS

**peerindex** [_-v_] [_-o file_] [_options_] _torrent-files_

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

**-o**, **--output** _FILE_
> 输出文件。

**-q**, **--quiet**
> 最少输出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**peerindex** 从 BitTorrent 文件中提取并分析节点（peer）信息。它显示 tracker URL 和内嵌的节点数据。

种子文件可能包含缓存的节点地址。这可以在不连接 tracker 的情况下揭示 swarm 中的参与者。

Tracker 分析会显示所有 announce URL。多 tracker 配置则会显示层级信息。

该工具有助于理解种子的结构。对网络取证和研究很有用。

# CAVEATS

节点数据可能已过时。并非所有种子都包含节点缓存。分析过程是被动的，不会主动联网。

# HISTORY

**peerindex** 属于用于网络研究和取证的 BitTorrent 分析工具集。

# SEE ALSO

[transmission-show](/man/transmission-show)(1), [aria2c](/man/aria2c)(1), [btshowmetainfo](/man/btshowmetainfo)(1)
