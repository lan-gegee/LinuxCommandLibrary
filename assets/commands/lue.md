# TAGLINE

支持文字转语音的终端电子书阅读器

# TLDR

**阅读电子书**

```lue [path/to/book.epub]```

**继续阅读上次打开的书**

```lue```

**启动导航指南**

```lue --guide```

**使用指定的 TTS 模型阅读**

```lue --tts [kokoro] [path/to/book.epub]```

**使用指定的音色和速度阅读**

```lue --voice [en-US-AriaNeural] --speed [1.5] [path/to/book.epub]```

**阅读 PDF 并应用清理过滤器**（移除页码、页眉）

```lue --filter [path/to/book.pdf]```

# SYNOPSIS

**lue** [_options_] [_file_]

# PARAMETERS

**-k**, **--key** _LAYOUT_
> 指定要使用的键盘布局。

**--guide**
> 启动交互式导航指南。

**--tts** _MODEL_
> 使用指定的 TTS 模型（edge、kokoro 或 none）。

**--voice** _VOICE_
> 使用指定的音色（例如 "en-US-AriaNeural"）。

**--speed** _SPEED_
> 设置语音速度（例如 1.5）。

**--lang** _CODE_
> 指定语言代码。

**--over** _SECONDS_
> 句子之间的重叠秒数。

**--filter**
> 启用 PDF 清理过滤器（移除页码、页眉、脚注）。

# DESCRIPTION

**lue** 是一个基于终端的电子书阅读器，具有有声书质量的文字转语音功能。它支持多种格式，包括 **EPUB**、**PDF**、**DOCX**、**HTML**、**RTF**、**TXT** 和 **MD**。

界面提供三种 UI 复杂度模式（Minimal、Medium 和 Full），可通过 **v** 键循环切换。内置两种用于导航的键盘布局。

# CAVEATS

文字转语音的质量取决于系统的 TTS 引擎。终端中的 PDF 渲染可能无法保留复杂版式。

# HISTORY

**lue** 由 **superstarryeyes** 创建，使用 **Python** 编写。可以通过 pip 安装：`pip install lue-reader`。

# INSTALL

```nix: nix profile install nixpkgs#lue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bat](/man/bat)(1), [less](/man/less)(1)
