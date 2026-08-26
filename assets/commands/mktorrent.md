# TAGLINE

创建 BitTorrent 元信息文件

# TLDR

**从文件创建种子**

```mktorrent -a [http://tracker.example.com/announce] [file]```

**从目录创建种子**

```mktorrent -a [http://tracker.example.com/announce] [directory/]```

**使用多个 tracker 创建**

```mktorrent -a [tracker1] -a [tracker2] [file]```

**创建私有种子**

```mktorrent -p -a [http://tracker.example.com/announce] [file]```

**指定分块长度**

```mktorrent -l [20] [file]```

**添加 Web 种子**

```mktorrent -w [http://example.com/file] -a [tracker] [file]```

**带注释创建**

```mktorrent -c "[My torrent]" -a [tracker] [file]```

**指定输出文件名**

```mktorrent -o [output.torrent] -a [tracker] [file]```

**详细输出**

```mktorrent -v -a [tracker] [file]```

# SYNOPSIS

**mktorrent** [_-a tracker_] [_-p_] [_-l piece_length_] [_-o output.torrent_] [_options_] _path_

# PARAMETERS

**-a** _URL_
> Tracker 的 announce URL。

**-o** _FILE_
> 输出的 torrent 文件。

**-p**
> 私有种子（禁用 DHT/PEX）。

**-l** _N_
> 分块长度，以 2 的幂表示（默认 18，即 256KB）。

**-c** _TEXT_
> 注释。

**-n** _NAME_
> 种子中的名称（默认：路径的基名）。

**-w** _URL_
> Web 种子 URL。

**-s** _TEXT_
> 供私有 tracker 使用的来源标签。

**-v**
> 详细输出。

**-t** _THREADS_
> 哈希计算线程数。

**-d**
> 不写入创建日期。

**-h**
> 显示帮助界面。

# DESCRIPTION

**mktorrent** 创建 BitTorrent 元信息（.torrent）文件。它对内容进行哈希计算，并将文件信息与 tracker 详情打包在一起。

该工具为文件校验计算分块哈希。分块长度影响 swarm 效率——更大的分块可减少开销但会延迟初始分享。自动选择通常效果良好。

多个 tracker 提供冗余。当某个 tracker 宕机时，客户端会尝试其他 tracker。私有种子禁用 DHT 和节点交换，只能通过 tracker 运行。

Web 种子在对等节点不可用时提供 HTTP 后备。它们对初始做种或冷门种子很有用。

来源标签帮助私有 tracker 识别来自其站点的种子。它嵌入 info 字典中，成为 info hash 的一部分。

小文件的创建很快，但由于需要进行哈希计算，大型数据集可能耗时较长。

# CAVEATS

创建后更改任何内容都会使种子失效。私有 tracker 的种子与公开种子不互通。较大的分块大小会延迟首个分块的完成。

# HISTORY

**mktorrent** 编写的目标是成为轻量、快速的种子制作工具。它提供命令行方式的种子创建能力，无需完整的 BitTorrent 客户端。

# INSTALL

```apt: sudo apt install mktorrent```

```dnf: sudo dnf install mktorrent```

```pacman: sudo pacman -S mktorrent```

```apk: sudo apk add mktorrent```

```zypper: sudo zypper install mktorrent```

```brew: brew install mktorrent```

```nix: nix profile install nixpkgs#mktorrent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-create](/man/transmission-create)(1), [rtorrent](/man/rtorrent)(1), [aria2c](/man/aria2c)(1)
