# TAGLINE

向 MP3 文件写入 ID3 标签的命令行工具

# TLDR

**设置歌曲标题**

```id3tag -s "[title]" [file.mp3]```

**设置艺术家**

```id3tag -a "[artist]" [file.mp3]```

**设置专辑**

```id3tag -A "[album]" [file.mp3]```

**设置年份和音轨号**

```id3tag -y [2024] -t [1] [file.mp3]```

**按编号设置流派**

```id3tag -g [17] [file.mp3]```

**一次性设置多个标签**

```id3tag -a "[artist]" -s "[title]" -A "[album]" -y [2024] -t [1] [file.mp3]```

**只写入 ID3v2 标签**

```id3tag -2 -a "[artist]" -s "[title]" [file.mp3]```

# SYNOPSIS

**id3tag** [_options_] _file_...

# PARAMETERS

**-1**, **--v1tag**
> 只生成 id3v1 标签。

**-2**, **--v2tag**
> 只生成 id3v2 标签。

**-a**, **--artist** _ARTIST_
> 设置艺术家名称。

**-s**, **--song** _SONG_
> 设置歌曲标题。

**-A**, **--album** _ALBUM_
> 设置专辑名称。

**-y**, **--year** _NUM_
> 设置发行年份。

**-t**, **--track** _NUM_
> 设置音轨号。

**-T**, **--total** _NUM_
> 设置专辑总音轨数。

**-g**, **--genre** _NUM_
> 按编号设置流派。

**-c**, **--comment** _COMMENT_
> 设置注释。

**-C**, **--desc** _DESCRIPTION_
> 设置注释描述。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**id3tag** 是一个向 MP3 文件写入 ID3 标签的命令行工具，属于 id3lib/libid3-tools 软件包。默认同时生成 ID3v1 和 ID3v2 标签；使用 **-1** 或 **-2** 可只生成其中一种。可设置标题、艺术家、专辑、年份、音轨号、流派和注释。适合配合 shell 脚本进行批量打标签。使用 **id3info** 可查看已有标签。

# INSTALL

```apt: sudo apt install libid3-tools```

```dnf: sudo dnf install id3lib```

```pacman: sudo pacman -S id3lib```

```apk: sudo apk add id3lib```

```brew: brew install id3lib```

```nix: nix profile install nixpkgs#id3lib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [mp3info](/man/mp3info)(1)

