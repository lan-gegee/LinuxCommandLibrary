# TAGLINE

将基于文本的乐谱编译为印刷乐谱的音乐制谱程序

# TLDR

**编译乐谱**为 PDF（默认）

```lilypond [score.ly]```

**显式选择 PDF 输出**

```lilypond --pdf [score.ly]```

**输出 PNG 图片**（每页一张）

```lilypond --png [score.ly]```

**输出 PostScript**

```lilypond --ps [score.ly]```

**输出 SVG**（使用 SVG 后端）

```lilypond -dbackend=svg [score.ly]```

**将输出写入目录**并自定义文件前缀

```lilypond -o [output/name] [score.ly]```

**添加共享库文件的 include 路径**

```lilypond -I [/path/to/includes] [score.ly]```

**禁用点击定位**以生成可分发的 PDF

```lilypond -dno-point-and-click [score.ly]```

**排版 LaTeX 内嵌的乐谱**（通过 lilypond-book）

```lilypond-book [document.lytex]```

# SYNOPSIS

**lilypond** [_options_] _file_.ly...

# PARAMETERS

_FILE_
> LilyPond 源文件（`.ly`）。可以给出多个文件；每个文件独立处理。

**--pdf**
> 生成 PDF 输出（未指定后端时的默认值）。

**--png**
> 生成 PNG 图片（每页一张）。

**--ps**
> 生成 PostScript。`--pdf` 会隐含此选项。

**-f**, **--format=**_FORMAT_
> 输出格式的另一种语法（`pdf`、`ps`、`png`、`svg`）。

**-o**, **--output=**_FILE_
> 输出文件前缀（或目录）。会追加 `.pdf`/`.png`/`.ps` 后缀。

**-I**, **--include=**_DIR_
> 将 _DIR_ 加入 include 搜索路径。可以重复使用。

**-d**_SETTING_[=_VALUE_]
> 设置 `ly:set-option` 程序选项。例如：`-dbackend=svg`、`-dno-point-and-click`、`-dpreview`、`-ddelete-intermediate-files`、`-dcrop`、`-dembed-source-code`。

**-e**, **--evaluate=**_EXPR_
> 在读取 `.ly` 文件之前先以 Scheme 求值 _EXPR_。

**-j**, **--jail=**_USER,GROUP,JAIL,DIR_
> 在 chroot 监狱中运行（对服务器部署有用）。

**-s**, **--silent**
> 抑制进度消息。

**-V**, **--verbose**
> 详细输出（打印正在读取的每个文件）。

**-w**, **--warranty**
> 显示保修 / GPL 信息。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# COMMON -d OPTIONS

**-dno-point-and-click**
> 禁用 PDF 中的点击定位链接。对任何要发布的内容都推荐使用——点击定位会嵌入你机器上的绝对路径。

**-dpreview**
> 只渲染第一个谱表系统，作为"预览"PNG/PDF。

**-dcrop**
> 生成仅围绕音乐内容裁剪的 PDF/PNG。

**-dbackend=**_NAME_
> 选择后端：`ps`（默认）、`svg`、`scm`、`null`。

**-ddelete-intermediate-files**
> 在生成 PDF 后删除 `.ps` / `-systems.*` 文件。

**-dembed-source-code**
> 将 `.ly` 源码嵌入到输出的 PDF 中。

# DESCRIPTION

**LilyPond** 将纯文本形式的音乐描述编译成出版质量的雕版乐谱。它的灵感来自 **TeX** 的排版理念：用户编写逻辑内容（音符、节奏、歌词、力度记号），而 LilyPond 负责处理间距、符杠、分页和碰撞规避。

同一份源文件可以输出为 PDF、PostScript、SVG 或 PNG。后端通过 `-dbackend=` 选择。相关工具有：

- **lilypond-book** — 将 `.ly` 片段嵌入 LaTeX/HTML/DocBook 并内联渲染。
- **midi2ly** / **abc2ly** / **musicxml2ly** — 将其他格式转换为 LilyPond 源码。
- **convert-ly** — 将旧版 `.ly` 语法升级到当前编译器支持的版本。

# CAVEATS

学习曲线陡峭——输入语言功能丰富，且不同于所见即所得工具。大型乐谱的编译可能很慢；编辑时可使用 `-dpreview`。分享 PDF 前务必加上 `-dno-point-and-click`，以免泄露文件系统路径。

# HISTORY

**LilyPond** 由 **Han-Wen Nienhuys** 和 **Jan Nieuwenhuizen** 于 **1996 年**发起，灵感来自 TeX 的排版质量以及 MusiXTeX 的音乐输入语言。它现在是 GNU 项目的一员，以 GPL 许可证发布，用 C++ 和 Scheme（GNU Guile）编写。

# INSTALL

```apt: sudo apt install lilypond```

```dnf: sudo dnf install lilypond```

```pacman: sudo pacman -S lilypond```

```apk: sudo apk add lilypond```

```zypper: sudo zypper install lilypond```

```brew: brew install lilypond```

```nix: nix profile install nixpkgs#lilypond```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[abc2ly](/man/abc2ly)(1), [musescore](/man/musescore)(1)
