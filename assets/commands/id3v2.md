# TAGLINE

查看和编辑 MP3 文件中 ID3v2 标签的命令行工具

# TLDR

**列出**所有可用的流派

```id3v2 -L```

**列出**指定文件的所有标签

```id3v2 -l [path/to/file.mp3]```

从文件中**删除** id3v2 标签

```id3v2 --delete-v2 [path/to/file.mp3]```

从文件中**删除** id3v1 标签

```id3v2 --delete-v1 [path/to/file.mp3]```

显示**帮助**

```id3v2 -h```

# SYNOPSIS

**id3v2** [_options_] [_files_]

# PARAMETERS

**-L**, **--list-genres**
> 列出所有可用的流派代码

**-l**, **--list**
> 列出指定文件中的所有标签

**--delete-v2**
> 删除所有 id3v2 标签

**--delete-v1**
> 删除所有 id3v1 标签

**-a**, **--artist** _ARTIST_
> 设置艺术家标签

**-A**, **--album** _ALBUM_
> 设置专辑标签

**-t**, **--song** _TITLE_
> 设置歌曲标题标签

**-g**, **--genre** _GENRE_
> 设置流派（编号或名称）

**-y**, **--year** _YEAR_
> 设置年份标签

**-T**, **--track** _NUM/TOTAL_
> 设置音轨号

# DESCRIPTION

**id3v2** 是一个查看和编辑 MP3 文件中 ID3v2 标签的命令行工具。它也能处理 ID3v1 标签，并可在两个版本之间转换。

ID3 标签在 MP3 文件内存储艺术家、专辑、标题、年份和流派等元数据。id3v2 格式支持扩展信息，包括专辑封面、歌词和自定义帧。

# CAVEATS

一些编码不佳的文件可能存在损坏的标签。ID3v2 标签可能位于文件开头或结尾。编辑标签不会重新编码音频。某些播放器可能会缓存标签信息。

# HISTORY

ID3v2 是对原始 ID3v1 标签格式的扩展，后者每个字段最多只有 30 个字符。ID3v2 于 **1998 年**推出，支持 Unicode、内嵌图片以及几乎不限长度的字段。

# INSTALL

```apt: sudo apt install id3v2```

```dnf: sudo dnf install id3v2```

```pacman: sudo pacman -S id3v2```

```zypper: sudo zypper install id3v2```

```brew: brew install id3v2```

```nix: nix profile install nixpkgs#id3v2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mid3v2](/man/mid3v2)(1), [ffmpeg](/man/ffmpeg)(1)
