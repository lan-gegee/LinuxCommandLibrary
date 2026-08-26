# TAGLINE

字符编码检测与转换

# TLDR

**检测文件**编码

```enca [file.txt]```

**带语言**提示进行检测

```enca -L [czech] [file.txt]```

**转换编码**

```enca -x [UTF-8] [file.txt]```

**检测并显示**置信度

```enca -d [file.txt]```

**处理多个文件**

```enca -L [russian] [*.txt]```

# SYNOPSIS

**enca** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要分析的文件。

**-L** _LANGUAGE_
> 提示检测所用语言。

**-x** _ENCODING_
> 转换为指定编码。

**-d**
> 显示详细的检测信息。

**-g**, **--guess**
> 仅输出最佳猜测。

**-i**, **--info**
> 显示可用的编码。

**--help**
> 显示帮助信息。

# DESCRIPTION

**enca**（Extremely Naive Charset Analyser）基于语言的统计启发式方法检测文本文件的字符编码，并可通过管道调用 **iconv** 在编码之间转换文件。它尤其擅长处理斯拉夫语及中/东欧语言使用的传统 8 位字符集（ISO-8859-2/5、KOI8-R、CP1250/1251、Mazovia、T.61 等），而 **file -i** 这类更简单的工具在这些场景下往往力不从心。

通过 **-L** 提供语言提示时检测效果最好；否则 **enca** 会退回到通用配置文件，可能返回含糊的结果。默认情况下每个文件输出一行检测到的编码，使用 **-d** 或 **-v** 则输出扩展信息。**-x** _ENCODING_ 就地执行转换，底层调用 **iconv**；当目标字符集缺少某些字符时，可搭配 **--cstocs** 进行转写。

# CAVEATS

检测是启发式的，并非确定无疑。短文件可能出现歧义。配合具体的语言提示效果最佳。某些编码无法相互区分。

# HISTORY

enca 为应对中/东欧计算环境中的编码多样性而生——历史上同一语言曾被许多互不兼容的字符集所表示。

# INSTALL

```apt: sudo apt install enca```

```dnf: sudo dnf install enca```

```pacman: sudo pacman -S enca```

```apk: sudo apk add enca```

```zypper: sudo zypper install enca```

```brew: brew install enca```

```nix: nix profile install nixpkgs#enca```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file](/man/file)(1), [iconv](/man/iconv)(1), [chardet](/man/chardet)(1)
