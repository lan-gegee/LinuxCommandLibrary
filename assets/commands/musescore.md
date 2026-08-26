# TAGLINE

免费乐谱制作软件

# TLDR

**打开 MuseScore**

```musescore```

**打开乐谱文件**

```musescore [score.mscz]```

**导出为 PDF**

```musescore [score.mscz] -o [output.pdf]```

**导出为音频**

```musescore [score.mscz] -o [output.mp3]```

**批量转换文件**

```musescore -j [job.json]```

**不启动 GUI 运行**

```musescore --no-gui [score.mscz] -o [output.pdf]```

# SYNOPSIS

**musescore** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的乐谱文件。

**-o** _FILE_
> 输出文件。

**-j** _FILE_
> 批处理作业文件（JSON）。

**--no-gui**
> 无界面模式。

**-S** _FILE_
> 要使用的样式文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**musescore** 是一款免费的乐谱制作软件。它用于创建、播放和打印乐谱。

该工具支持多种格式，可导出 MIDI、MusicXML 和 PDF。具备专业级功能。

# CAVEATS

GUI 应用程序。回放需要 soundfont。大型乐谱对资源消耗较大。

# HISTORY

MuseScore 于 **2002 年**首次发布，是商业乐谱软件的开源替代品。

# INSTALL

```apt: sudo apt install musescore```

```dnf: sudo dnf install musescore```

```pacman: sudo pacman -S musescore```

```zypper: sudo zypper install musescore```

```nix: nix profile install nixpkgs#musescore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mscore](/man/mscore)(1), [lilypond](/man/lilypond)(1)
