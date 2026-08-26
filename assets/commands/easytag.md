# TAGLINE

图形化音频文件元数据编辑器

# TLDR

**启动 EasyTAG**

```easytag```

**打开指定目录**

```easytag [/path/to/music]```

# SYNOPSIS

**easytag** [_options_] [_directory_]

# PARAMETERS

_directory_
> 要打开的音乐目录。

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# CONFIGURATION

**~/.config/easytag/easytag.conf**
> 应用设置，包括默认目录、标签格式偏好和界面选项。

# DESCRIPTION

**EasyTAG** 是一个用于查看和编辑音频文件元数据（标签）的图形应用。它支持 MP3、MP2、MP4/AAC、FLAC、Ogg Vorbis、Ogg Speex、Ogg Opus、MusePack、Monkey's Audio 和 WavPack 文件。

该应用提供批量打标签、文件名转标签、标签转文件名重命名，以及通过 CDDB 自动获取元数据的功能。它适合用来整理音乐库并修复错误或缺失的标签。

# FEATURES

- 编辑 ID3v1、ID3v2、Vorbis、APE 等标签格式
- 批量为多个文件打标签
- 按文件名模式自动填充
- 基于标签重命名文件
- CDDB/freedb 查询
- 嵌入封面图

# CAVEATS

GUI 应用；不支持命令行标签编辑。某些标签格式支持有限。大型音乐库扫描可能耗时。较老的标签可能出现字符编码问题。

# HISTORY

EasyTAG 由 **Jérôme Couderc** 于 **2000 年**启动开发，此后由 GNOME 社区维护。它从早期的命令行标签编辑器演化而来，为音乐元数据管理提供了友好的图形界面。

# INSTALL

```apt: sudo apt install easytag```

```dnf: sudo dnf install easytag```

```pacman: sudo pacman -S easytag```

```apk: sudo apk add easytag```

```zypper: sudo zypper install easytag```

```nix: nix profile install nixpkgs#easytag```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id3v2](/man/id3v2)(1), [kid3](/man/kid3)(1), [picard](/man/picard)(1)
