# TAGLINE

MuseScore 乐谱制作软件

# TLDR

**打开 MuseScore**

```mscore```

**打开乐谱文件**

```mscore [score.mscz]```

**转换为 PDF**

```mscore [score.mscz] -o [output.pdf]```

**导出为 MIDI**

```mscore [score.mscz] -o [output.mid]```

**导出为音频**

```mscore [score.mscz] -o [output.mp3]```

**以无界面模式运行**

```mscore --no-gui [score.mscz] -o [output.pdf]```

# SYNOPSIS

**mscore** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的乐谱文件。

**-o** _FILE_
> 输出文件（格式由扩展名决定）。

**--no-gui**
> 不使用图形界面运行。

**-S** _STYLE_
> 使用样式文件。

**-r** _DPI_
> 设置图像分辨率。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mscore** 是 MuseScore 乐谱制作软件。它用于创建和编辑乐谱。

该工具支持 MIDI、MusicXML 和音频导出。具备专业级的记谱功能。

# CAVEATS

GUI 应用程序。依赖体积较大。音频输出需要 soundfont。

# HISTORY

MuseScore 作为**开源乐谱软件**而创建，于 2002 年首次发布。

# INSTALL

```apt: sudo apt install musescore```

```dnf: sudo dnf install musescore```

```pacman: sudo pacman -S musescore```

```apk: sudo apk add musescore```

```zypper: sudo zypper install musescore```

```nix: nix profile install nixpkgs#musescore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[musescore](/man/musescore)(1), [lilypond](/man/lilypond)(1), [timidity](/man/timidity)(1)
