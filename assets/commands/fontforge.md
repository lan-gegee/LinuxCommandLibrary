# TAGLINE

用于创建和修改字体的综合性字体编辑器

# TLDR

**打开 FontForge 图形界面**

```fontforge```

**打开字体文件**

```fontforge [font.ttf]```

**转换字体格式**

```fontforge -c 'Open($1); Generate($2)' [input.otf] [output.ttf]```

**运行脚本**

```fontforge -script [convert.pe]```

将字体**导出为 Web** 字体

```fontforge -c 'Open($1); Generate($2)' [font.ttf] [font.woff2]```

# SYNOPSIS

**fontforge** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打开的字体文件。

**-c** _SCRIPT_
> 执行脚本命令。

**-script** _FILE_
> 运行脚本文件。

**-lang** _LANGUAGE_
> 脚本语言（ff、py）。

**-nosplash**
> 启动时不显示启动画面。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fontforge** 是一个支持 OpenType、TrueType 及许多其他格式的综合性字体编辑器。它提供创建、编辑和转换字体的工具。

该应用提供字形编辑、度量调整、字距微调（kerning）、hinting 以及 OpenType 特性开发等功能。脚本支持使批量操作和自动化字体处理成为可能。

FontForge 涵盖从初步设计到可投产输出的专业字体开发全流程。

# CAVEATS

字体设计学习曲线陡峭。图形界面可能较为复杂。部分格式的支持有限。

# HISTORY

FontForge（最初名为 PfaEdit）由 **George Williams** 于 2000 年起开发。它是最强大的开源字体编辑器，被世界各地的字体设计师和字体开发者使用。

# INSTALL

```apt: sudo apt install fontforge```

```dnf: sudo dnf install fontforge```

```pacman: sudo pacman -S fontforge```

```apk: sudo apk add fontforge```

```zypper: sudo zypper install fontforge```

```brew: brew install fontforge```

```nix: nix profile install nixpkgs#fontforge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-query](/man/fc-query)(1)
