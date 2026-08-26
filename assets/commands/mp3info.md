# TAGLINE

显示和编辑 MP3 文件的 ID3 标签

# TLDR

**显示 MP3 信息**

```mp3info [file.mp3]```

**设置标题标签**

```mp3info -t "[Song Title]" [file.mp3]```

**设置艺术家标签**

```mp3info -a "[Artist Name]" [file.mp3]```

**设置专辑标签**

```mp3info -l "[Album Name]" [file.mp3]```

**设置年份标签**

```mp3info -y [2024] [file.mp3]```

**设置音轨编号**

```mp3info -n [1] [file.mp3]```

**删除所有标签**

```mp3info -d [file.mp3]```

# SYNOPSIS

**mp3info** [_options_] _files_

# PARAMETERS

_FILES_
> 要处理的 MP3 文件。

**-t** _TITLE_
> 设置标题标签。

**-a** _ARTIST_
> 设置艺术家标签。

**-l** _ALBUM_
> 设置专辑标签。

**-y** _YEAR_
> 设置年份标签。

**-n** _NUM_
> 设置音轨编号。

**-d**
> 删除所有 ID3 标签。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mp3info** 用于显示和编辑 MP3 文件的 ID3 标签，是一个轻量级的标签编辑器。

该工具读取 ID3v1 标签，并显示比特率、时长等技术信息。

# CAVEATS

以 ID3v1 为主。对 ID3v2 的支持有限。高级编辑建议使用 id3v2。

# HISTORY

mp3info 作为一个简单的 **ID3 标签**查看器和编辑器而创建，用于命令行下的 MP3 管理。

# INSTALL

```apt: sudo apt install mp3info```

```brew: brew install mp3info```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [ffprobe](/man/ffprobe)(1)
