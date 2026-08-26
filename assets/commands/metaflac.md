# TAGLINE

命令行 FLAC 元数据编辑器

# TLDR

**列出所有元数据**

```metaflac --list [file.flac]```

**显示所有标签**

```metaflac --export-tags-to=- [file.flac]```

**设置标签值**

```metaflac --set-tag="[ARTIST=Name]" [file.flac]```

**移除标签**

```metaflac --remove-tag="[COMMENT]" [file.flac]```

**从文件导入标签**

```metaflac --import-tags-from=[tags.txt] [file.flac]```

**导出封面图**

```metaflac --export-picture-to=[cover.jpg] [file.flac]```

**导入封面图**

```metaflac --import-picture-from=[cover.jpg] [file.flac]```

# SYNOPSIS

**metaflac** [_options_] _files_...

# PARAMETERS

**--list**
> 列出元数据块。

**--export-tags-to** _file_
> 导出标签。

**--import-tags-from** _file_
> 导入标签。

**--set-tag** _tag=value_
> 设置标签。

**--remove-tag** _tag_
> 移除标签。

**--remove-all-tags**
> 移除所有标签。

**--export-picture-to** _file_
> 将内嵌图片（封面图）导出到文件。

**--import-picture-from** _file_
> 向文件导入图片（PNG/JPEG；规范语法为 _TYPE\|MIME\|DESC\|WIDTHxHEIGHTxDEPTH/COLORS\|FILE_）。

**--show-md5sum**
> 打印音频数据的未编码 MD5 校验和。

**--show-min-blocksize** / **--show-max-blocksize** / **--show-sample-rate** / **--show-channels** / **--show-bps** / **--show-total-samples**
> 打印单个 STREAMINFO 字段，便于脚本使用。

**--add-replay-gain**
> 为一个或多个文件计算并添加 ReplayGain 标签（传入多个文件时视为同一张专辑）。

**--remove-replay-gain**
> 移除 ReplayGain 标签。

**--block-type** / **--except-block-type** _types_
> 将后续操作限定到特定的元数据块类型（例如 _VORBIS\_COMMENT_、_PICTURE_、_SEEKTABLE_）。

# DESCRIPTION

**metaflac** 是 FLAC 的命令行元数据编辑器。它可以列出、添加、移除和修改 FLAC 文件中的元数据，包括 Vorbis 注释和内嵌图片。

# TAG FORMAT

```
# tags.txt
ARTIST=Artist Name
ALBUM=Album Name
TITLE=Track Title
TRACKNUMBER=01
```

# CAVEATS

仅适用于 FLAC 文件。修改立即生效（无法撤销）。标签名不区分大小写。导入图片需要正确的 MIME 类型。

# HISTORY

metaflac 属于 **Josh Coalson** 于 **2000 年**创建的 **FLAC** 项目——一种免费的无损音频编解码器。

# INSTALL

```apt: sudo apt install flac```

```dnf: sudo dnf install flac```

```pacman: sudo pacman -S flac```

```apk: sudo apk add flac```

```zypper: sudo zypper install flac```

```brew: brew install flac```

```nix: nix profile install nixpkgs#flac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flac](/man/flac)(1), [ffmpeg](/man/ffmpeg)(1), [mid3v2](/man/mid3v2)(1)
