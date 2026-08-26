# TAGLINE

MP3 文件的 ID3 标签编辑器

# TLDR

**查看** MP3 文件的信息

```eyeD3 [filename.mp3]```

设置 MP3 文件的**标题**

```eyeD3 [-t|--title] "[A Title]" [filename.mp3]```

设置目录中所有 MP3 文件的**专辑**

```eyeD3 [-A|--album] "[Album Name]" [*.mp3]```

为 MP3 文件设置正面**封面图**

```eyeD3 --add-image [front_cover.jpeg]:FRONT_COVER: [filename.mp3]```

# SYNOPSIS

**eyeD3** [_options_] _files_

# DESCRIPTION

**eyeD3** 读取和处理 MP3 文件中的 ID3 元数据。它支持 ID3 v1.x 和 v2.x 标签，包括文本、图像和自定义帧。

适合用于整理音乐库和批量标记 MP3 收藏。

# PARAMETERS

**-t, --title** _text_
> 设置曲目标题。

**-A, --album** _text_
> 设置专辑名称。

**-a, --artist** _text_
> 设置艺人名称。

**-b, --album-artist** _text_
> 设置专辑艺人（合辑、多艺人专辑）。

**-n, --track** _num_
> 设置曲目编号。

**-N, --track-total** _num_
> 设置曲目总数。

**-d, --disc-num** _num_
> 设置唱片编号。

**-G, --genre** _genre_
> 设置流派（名称或数字 ID3v1 代码）。

**-Y, --release-year** _year_
> 设置发行年份。

**-c, --comment** _text_
> 添加注释。

**--add-image** _path:type[:description]_
> 添加图像（APIC 帧）；TYPE 取自 `--list-image-types`（如 FRONT_COVER）。

**--remove-all-images**
> 移除所有内嵌图像。

**--write-images** _dir_
> 将图像提取到目录。

**--to-v2.3**, **--to-v2.4**, **--to-v1.1**
> 将标签转换为指定的 ID3 版本。

**--remove-v1**, **--remove-v2**, **--remove-all**
> 移除 ID3 v1.x、v2.x 或所有标签。

**--preserve-file-times**
> 保留原始文件修改时间戳。

**-Q, --quiet**
> 抑制输出。

# CAVEATS

只能处理 MP3 文件。部分播放器可能不支持所有 ID3v2 特性。Unicode 支持取决于标签版本。

# INSTALL

```nix: nix profile install nixpkgs#eyed3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [mp3info](/man/mp3info)(1), [ffmpeg](/man/ffmpeg)(1)
