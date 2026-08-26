# TAGLINE

MusicBrainz 的音乐标签编辑应用

# TLDR

**启动 MusicBrainz Picard**

```picard```

**打开文件**

```picard [file1.mp3] [file2.flac]```

**打开目录**

```picard [/path/to/music/]```

**显示版本**

```picard --version```

**调试模式**

```picard -d```

# SYNOPSIS

**picard** [_-d_] [_-c config_] [_-N_] [_options_] [_files_]

# PARAMETERS

**-d**, **--debug**
> 启用调试模式。

**-c** _FILE_, **--config-file** _FILE_
> 使用指定的配置文件。

**-N**, **--no-restore**
> 不恢复已保存的窗口状态。

**-M**, **--no-player**
> 禁用内置播放器。

**-P**, **--no-plugins**
> 禁用插件。

**-s** _PLUGIN_, **--stand-alone-instance** _PLUGIN_
> 以独立实例运行插件。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**picard** 是 MusicBrainz 出品的音乐标签编辑应用。它通过音频指纹识别音乐文件，并用准确的元数据为其打标签。

该应用将音乐与 MusicBrainz 数据库（最大的开放音乐百科）进行匹配。即使文件没有现成的标签，指纹识别也能确定曲目。

聚类（Cluster）模式按专辑对文件分组。查找（Lookup）向 MusicBrainz 查询匹配结果。扫描（Scan）使用 AcoustID 指纹进行识别。

封面图片会自动从多个来源下载。多个封面提供方保证了良好的覆盖率。

插件可扩展功能：额外的打标签特性、格式支持以及与其他服务的集成。

该标签编辑器支持多种格式：MP3、FLAC、OGG、M4A、WMA 等。原始文件会被原地修改或按照命名模式重命名。

# CAVEATS

查询需要联网。匹配精度取决于 MusicBrainz 的收录情况。大型曲库处理耗时较长。某些冷门发行版本可能找不到。

# HISTORY

**MusicBrainz Picard** 自 **2003 年**起由 MusicBrainz 社区开发。它以《星际迷航》中的角色命名，取代了早期的标签工具，成为 MusicBrainz 官方的标签编辑器。

# INSTALL

```apt: sudo apt install picard```

```dnf: sudo dnf install picard```

```pacman: sudo pacman -S picard```

```apk: sudo apk add picard```

```zypper: sudo zypper install picard```

```nix: nix profile install nixpkgs#picard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[beets](/man/beets)(1), [kid3](/man/kid3)(1), [easytag](/man/easytag)(1), [mid3v2](/man/mid3v2)(1)
