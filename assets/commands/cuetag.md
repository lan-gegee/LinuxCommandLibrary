# TAGLINE

将 CUE 文件中的元数据应用到音频文件

# TLDR

根据 CUE 文件**为 FLAC 文件写入标签**

```cuetag [album.cue] [track*.flac]```

为指定音轨**写标签**

```cuetag [album.cue] [track01.flac] [track02.flac]```

**为 Ogg Vorbis 文件写标签**

```cuetag [album.cue] [track*.ogg]```

**为 MP3 文件写标签**（需要 id3v2）

```cuetag [album.cue] [track*.mp3]```

# SYNOPSIS

**cuetag** _file.cue_ _audiofile_...

# DESCRIPTION

**cuetag** 将 CUE 文件中的元数据转移到音频文件。它从 CUE 文件读取音轨信息（标题、演奏者、ISRC 等），并把相应的标签写入对应的音频文件。

该工具会自动检测文件格式并使用相应的打标签方法：FLAC 用 metaflac，Ogg Vorbis 用 vorbiscomment，MP3 用 id3v2/id3tag。文件的命名必须保证音轨顺序对应（通常来自 shnsplit 的输出）。

转移的标签包括：title、artist/performer、album、track number、genre、date，以及 CUE 文件中存在的 ISRC 码。

# SUPPORTED FORMATS

**FLAC**：使用 metaflac（标准标签）
**Ogg Vorbis**：使用 vorbiscomment
**MP3**：使用 id3v2 或 id3tag

# CAVEATS

需要安装相应格式的打标签工具（metaflac、vorbiscomment、id3v2）。文件的顺序必须与 CUE 音轨一致。元数据较少的 CUE 文件只能产生稀疏的标签。非 ASCII 字符可能出现编码问题。

# HISTORY

cuetag 是 **cuetools** 的一部分，这是一组处理 CUE 文件的工具，由 **Svend Sorensen** 创建，用于简化 CD 镜像及其元数据的处理。在把单文件整轨抓轨处理成带标签的独立音轨时，这些工具至今仍是必备之选。

# INSTALL

```apt: sudo apt install cuetools```

```dnf: sudo dnf install cuetools```

```pacman: sudo pacman -S cuetools```

```brew: brew install cuetools```

```nix: nix profile install nixpkgs#cuetools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cuebreakpoints](/man/cuebreakpoints)(1), [shnsplit](/man/shnsplit)(1), [metaflac](/man/metaflac)(1), [id3v2](/man/id3v2)(1)

# RESOURCES

```[Source code](https://github.com/svend/cuetools)```

<!-- verified: 2026-06-26 -->
