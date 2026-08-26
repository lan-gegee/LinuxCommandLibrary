# TAGLINE

ABC 音乐记谱法到 LilyPond 的转换器

# TLDR

**将 ABC 文件转换**为 LilyPond 格式

```abc2ly [input.abc]```

**指定输出文件**

```abc2ly -o [output.ly] [input.abc]```

转换时**保留 ABC 的符杠（beaming）**约定

```abc2ly -b [input.abc]```

安静地**转换**，不输出进度信息

```abc2ly -q -o [output.ly] [input.abc]```

# SYNOPSIS

**abc2ly** [_OPTION_]... _FILE_

# PARAMETERS

**-o**, **--output=**_FILE_
> 将输出写入指定的 FILE 而不是标准输出。

**-b**, **--beams**
> 在输出中保留 ABC 对符杠的定义。

**-s**, **--strict**
> 对转换是否成功采取严格态度。

**-q**, **--quiet**
> 转换过程中抑制进度消息。

**-h**, **--help**
> 显示帮助信息并退出。

**--version**
> 显示版本号并退出。

# DESCRIPTION

**abc2ly** 是随 LilyPond 附带的转换脚本，它把 ABC 音乐记谱文件转换为 LilyPond 输入格式。ABC 记谱法是一种简单的基于文本的音乐记谱系统，在民谣和传统音乐圈很流行；而 LilyPond 是一个功能强大的音乐雕版程序，能生成高品质乐谱。

该工具读取符合 ABC 标准的文件，输出等价的 LilyPond 标记，随后交由 LilyPond 处理即可生成出版级 PDF 或其他格式的输出。这让拥有现成 ABC 曲目库的音乐人和档案工作者能够利用 LilyPond 更强的排版能力。

# CAVEATS

并非所有 ABC 特性都能完美映射到 LilyPond。复杂的 ABC 结构或非标准扩展可能需要在生成的 LilyPond 文件中手动调整。转换会保留音乐内容，但排版偏好可能需要微调。

# HISTORY

**abc2ly** 由 Han-Wen Nienhuys、Laura Conrad 和 Roy Rankin 作为 LilyPond 项目的组成部分开发。自项目早期起它就随 LilyPond 发行版一起提供，成为民间音乐社区流行的简易 ABC 记谱法与 LilyPond 专业雕版系统之间的桥梁。

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

[lilypond](/man/lilypond)(1)
