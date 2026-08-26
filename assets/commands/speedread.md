# TAGLINE

基于 RSVP 的终端快速阅读工具

# TLDR

以**指定速度**阅读文本

```cat [path/to/file.txt] | speedread -w [250]```

从指定行**继续阅读**

```cat [path/to/file.txt] | speedread -resume [5]```

一次显示**多个单词**

```cat [path/to/file.txt] | speedread -multiword```

# SYNOPSIS

**speedread** [_OPTIONS_]

# PARAMETERS

**-w, -wpm** _words_
> 设置阅读速度，单位为每分钟词数（默认：250）

**-resume** _line_
> 从指定的行号继续

**-multiword**
> 一次显示多个单词

# INTERACTIVE CONTROLS

**[**
> 减速 10%

**]**
> 提速 10%

**Space**
> 暂停并显示上下文行

**q**
> 退出

# DESCRIPTION

**speedread** 是一款基于终端的快速阅读工具，采用 RSVP（Rapid Serial Visual Presentation，快速序列视觉呈现）技术。它一次显示一个单词，并将其对齐到最佳识别点，从而在保持理解的前提下实现更快的阅读速度。

这一技术减少了眼球移动和默读，训练有素的读者可以达到每分钟 400-1000+ 词的速度。文本通过 stdin 管道输入，便于与 cat、curl 或邮件客户端等其他工具集成。

# CAVEATS

效果因人而异；快速阅读是需要练习的技能。过高的速度可能降低理解程度。复杂或技术性文本可能需要较慢的速度。终端必须支持相应的显示格式。

# HISTORY

**speedread** 由 **Petr Baudis**（pasky）创建并以开源软件发布。其灵感来自 **Spritz**——一项商业快速阅读技术。用于快速阅读的 RSVP 技术自 **20 世纪 70 年代**起就有人研究，数字实现在 **2010 年代**开始流行。

# INSTALL

```brew: brew install speedread```

```nix: nix profile install nixpkgs#speedread```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1), [cat](/man/cat)(1), [curl](/man/curl)(1)
