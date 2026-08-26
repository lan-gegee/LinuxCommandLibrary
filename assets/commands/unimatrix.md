# TAGLINE

终端中的 Matrix 落码动画

# TLDR

**启动 Matrix 雨效果**

```unimatrix```

**自定义速度**

```unimatrix -s [90]```

**颜色**

```unimatrix -c [green]```

**异步滚动**

```unimatrix -a```

**粗体字符**

```unimatrix -b```

**指定字符集**

```unimatrix -u "[abc123]"```

# SYNOPSIS

**unimatrix** [_-s speed_] [_-c color_] [_-a_] [_-b_] [_options_]

# PARAMETERS

**-s** _SPEED_
> 滚动速度，0-100（默认 85）。

**-c** _COLOR_
> 前景色（green、red、blue、white、yellow、cyan、magenta、black）。

**-a**
> 异步滚动，每一列独立移动。

**-b**
> 仅使用粗体字符。

**-f**
> 启用闪烁字符。

**-n**
> 禁用粗体字符。

**-u** _CHARS_
> 使用自定义字符集。

**-l** _PRESETS_
> 使用预设字符组（例如 S=符号、k=片假名、l=字母、n=数字、c=西里尔字母）。

# DESCRIPTION

**unimatrix** 是一个 Python 脚本，可直接在终端中模拟《黑客帝国》电影中标志性的落码雨效果。它显示以不同速度向下滚动的多列字符，营造出独特的黑底绿色瀑布流效果。

该动画高度可定制，可控制滚动速度、颜色、字符粗细以及用于下落流的字符集。它支持包括拉丁文、希腊文、西里尔文和 CJK 文字在内的各种 Unicode 字符，可以呈现传统片假名之外的多样视觉效果。

unimatrix 可用作屏幕保护程序、终端装饰，或纯粹为了娱乐。它支持每列独立移动的异步滚动，产生类似电影中更自然的视觉效果。

# CAVEATS

需要 Python。仅限终端。性能因环境而异。

# HISTORY

**unimatrix** 作为对 Matrix 落码动画的 Python 重制版而创建，并加入了 Unicode 支持。

# INSTALL

```nix: nix profile install nixpkgs#unimatrix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [pipes.sh](/man/pipes.sh)(1), [asciiquarium](/man/asciiquarium)(1)
