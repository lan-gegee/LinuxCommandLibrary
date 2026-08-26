# TAGLINE

编辑 MP3 文件中的 ID3v2 标签

# TLDR

**查看 ID3 标签**

```mid3v2 [file.mp3]```

**设置标题**

```mid3v2 --title "[Song Title]" [file.mp3]```

**设置艺术家和专辑**

```mid3v2 --artist "[Artist]" --album "[Album]" [file.mp3]```

**设置音轨号**

```mid3v2 --track [5] [file.mp3]```

**设置年份**

```mid3v2 --year [2024] [file.mp3]```

**删除所有标签**

```mid3v2 --delete-all [file.mp3]```

**设置封面图**

```mid3v2 --picture "[cover.jpg]" [file.mp3]```

**列出所有帧**

```mid3v2 --list [file.mp3]```

# SYNOPSIS

**mid3v2** [_--title text_] [_--artist text_] [_--album text_] [_options_] _files_

# PARAMETERS

**-t**, **--title** _TEXT_
> 设置标题（TIT2）。

**-a**, **--artist** _TEXT_
> 设置艺术家（TPE1）。

**-A**, **--album** _TEXT_
> 设置专辑（TALB）。

**-T**, **--track** _NUM_
> 设置音轨号（TRCK）。

**-y**, **--year** _YEAR_
> 设置年份（TDRC）。

**-g**, **--genre** _GENRE_
> 设置流派（TCON）。

**-c**, **--comment** _TEXT_
> 设置注释（COMM）。

**--picture** _FILE_
> 设置封面图（APIC）。

**-l**, **--list**
> 列出所有标签。

**-D**, **--delete-all**
> 删除所有标签。

**-d**, **--delete-frames** _FRAMES_
> 删除指定的帧。

**--convert**
> 将 ID3v1 转换为 ID3v2。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**mid3v2** 编辑 MP3 文件中的 ID3v2 标签。它是基于 Mutagen 的 id3v2 替代品，对 Unicode 和 ID3v2.4 有更好的支持。

该工具可读写 ID3v2.3 和 ID3v2.4 标签。它可以将旧式 ID3v1 标签转换为现代格式。Unicode 文本能被正确处理。

常见标签有对应的短选项（--artist、--album、--title）。可以使用帧标识符设置任意 ID3v2 帧，例如 TPE2（专辑艺术家）或 TXXX（用户自定义文本）。

封面图将图片嵌入音频文件。支持 JPEG 和 PNG 格式。可以添加多张不同类型的图片（正面、背面、艺术家）。

批处理通过通配符处理多个文件。结合 Shell 脚本，可以为整个音乐库打标签。

# CAVEATS

仅适用于 MP3（ID3）。其他格式请使用其他工具。大图片会增加文件体积。部分播放器更偏好 ID3v2.3 而非 v2.4。

# HISTORY

**mid3v2** 是 **Mutagen** Python 音频标签库的一部分，由 **Michael Urman** 和 **Joe Wreschnig** 于 **2005 年**前后创建。它的设计目的是正确处理 ID3v2.4 和 Unicode——旧工具在这方面表现不佳。

# INSTALL

```apk: sudo apk add mutagen```

```nix: nix profile install nixpkgs#mutagen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [ffmpeg](/man/ffmpeg)(1)
