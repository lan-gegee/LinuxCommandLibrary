# TAGLINE

支持 MP3、Ogg Vorbis、FLAC、MPC、MP4/AAC 等格式的音频标签编辑器

# TLDR

**启动 Kid3**

```kid3```

**打开目录**

```kid3 [/path/to/music]```

**命令行打标签**

```kid3-cli -c "[get title]" [file.mp3]```

**设置标签值**

```kid3-cli -c "[set title 'My Song']" [file.mp3]```

**批量转换**

```kid3-cli -c "[fromtag '%{artist} - %{title}' 2]" [*.mp3]```

# SYNOPSIS

**kid3** [_options_] [_directory_]

**kid3-cli** [_options_] [_files_...]

# PARAMETERS

_directory_
> 要打开的音乐目录。

**-c** _command_
> 执行命令（kid3-cli）。

# DESCRIPTION

**Kid3** 是一款音频标签编辑器，支持 MP3、Ogg Vorbis、FLAC、MPC、MP4/AAC 等格式。它可以编辑 ID3v1、ID3v2、APE、Vorbis 等标签格式。

该应用提供批量编辑、文件名与标签互相转换，以及从 MusicBrainz 和 Discogs 等在线数据库导入的功能。

# CLI COMMANDS

```bash
# Get tag
kid3-cli -c "get artist" song.mp3

# Set multiple tags
kid3-cli -c "set artist 'Band'" -c "set album 'Album'" song.mp3

# Rename from tags
kid3-cli -c "fromtag '%{track} - %{title}' 2" *.mp3

# Export to CSV
kid3-cli -c "export export.csv 'CSV'" .
```

# CAVEATS

不同的标签版本可能相互冲突。批量操作前应先预览。某些格式存在标签方面的限制。

# HISTORY

Kid3 由 **Urs Fleisch** 创建，最初是 KDE 下的一个简单标签编辑器。后来逐步支持多种格式，并可在多个平台上使用。

# INSTALL

```apt: sudo apt install kid3```

```dnf: sudo dnf install kid3```

```pacman: sudo pacman -S kid3```

```zypper: sudo zypper install kid3```

```nix: nix profile install nixpkgs#kid3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [easytag](/man/easytag)(1)
