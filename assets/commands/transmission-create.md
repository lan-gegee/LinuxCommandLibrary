# TAGLINE

创建 BitTorrent 种子文件

# TLDR

**创建带 tracker 的种子**

```transmission-create -o [output.torrent] -t [http://tracker.example.com/announce] [file_or_directory]```

**创建带多个 tracker 的种子**

```transmission-create -o [output.torrent] -t [tracker1] -t [tracker2] [file_or_directory]```

**创建私有种子**

```transmission-create -p -o [output.torrent] -t [tracker] [file_or_directory]```

**创建带注释的种子**

```transmission-create -c "[My torrent description]" -o [output.torrent] -t [tracker] [file]```

**创建自定义分块大小的种子**

```transmission-create -s [2048] -o [output.torrent] -t [tracker] [file]```

**创建自定义名称的种子**

```transmission-create -n "[Custom Name]" -o [output.torrent] -t [tracker] [file]```

# SYNOPSIS

**transmission-create** [_options_] _file_|_directory_

# PARAMETERS

**-o**, **--outfile** _file_
> 将生成的 .torrent 保存为该文件名。

**-t**, **--tracker** _url_
> 添加 tracker 通告 URL。可多次使用。

**-p**, **--private**
> 将种子标记为私有（用于私有 tracker）。

**-c**, **--comment** _text_
> 在种子元数据中添加一条注释。

**-s**, **--piecesize** _KiB_
> 设置分块大小，单位 KiB（默认自动计算）。

**-n**, **--name** _name_
> 覆盖根据源内容生成的默认种子名称。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**transmission-create** 根据文件或目录生成 .torrent 文件。它是 Transmission BitTorrent 客户端套件的一部分，无需图形界面即可在命令行创建种子。

该工具为源内容的所有分块计算 SHA1 校验和，并将其与 tracker 信息一起打包进种子文件。分块大小会根据内容大小自动选择，但也可以手动覆盖。

可添加多个 tracker 以实现冗余。私有种子会禁用 DHT 和节点交换，要求用户只能从指定的 tracker 获取对等节点。

# CAVEATS

大文件的哈希计算需要时间。多数使用场景下至少需要一个 tracker。创建后无法再更改私有标志。分块大小会影响种子文件大小和下载粒度。

# HISTORY

**transmission-create** 隶属于 Transmission 项目——一个始于 2005 年的开源 BitTorrent 客户端。这些命令行工具的开发目的是在没有图形界面的情况下实现自动化和服务器端的种子管理。

# INSTALL

```apt: sudo apt install transmission-cli```

```dnf: sudo dnf install transmission-cli```

```pacman: sudo pacman -S transmission-cli```

```apk: sudo apk add transmission-extra```

```brew: brew install transmission-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-show](/man/transmission-show)(1), [transmission-daemon](/man/transmission-daemon)(1), [transmission-remote](/man/transmission-remote)(1), [mktorrent](/man/mktorrent)(1)
