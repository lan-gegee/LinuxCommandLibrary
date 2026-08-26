# TAGLINE

从源代码中提取可翻译字符串

# TLDR

**从 C 中提取字符串**

```xgettext -o [messages.pot] [*.c]```

**从 Python 中提取**

```xgettext -L Python -o [messages.pot] [*.py]```

**使用关键字提取**

```xgettext -k_ -o [messages.pot] [*.c]```

**与现有文件合并**

```xgettext -j -o [messages.pot] [*.c]```

**添加注释**

```xgettext --add-comments=TRANSLATORS -o [messages.pot] [*.c]```

**设置软件包信息**

```xgettext --package-name=[MyApp] --package-version=[1.0] -o [messages.pot] [*.c]```

# SYNOPSIS

**xgettext** [_-L language_] [_-k keyword_] [_-o output_] [_options_] _files_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件。

**-L**, **--language** _LANG_
> 源语言。

**-k** _KEYWORD_
> 提取关键字。

**-j**, **--join-existing**
> 追加到现有文件。

**-c**, **--add-comments** _TAG_
> 提取注释。

**--package-name** _NAME_
> 软件包名称。

**--from-code** _ENC_
> 源编码。

# DESCRIPTION

**xgettext** 从源代码文件中提取可翻译字符串，并生成用于 GNU gettext 国际化工作流的便携对象模板（.pot）文件。它会扫描源文件中标记字符串以供翻译的函数调用，例如 **_()**、**gettext()** 和 **N_()**，并将它们收集到一个模板中，供译者作为起点使用。

该工具支持多种编程语言，包括 C、C++、Python、Shell、PHP、Java、Perl 等等。它可以根据文件扩展名自动检测源语言，也可以通过 **-L** 选项显式指定语言。可以使用 **-k** 定义自定义提取关键字，以匹配项目特有的翻译函数。

输出的 .pot 文件会保留源文件位置、译者注释（通过 **--add-comments** 提取）以及消息上下文。该模板是使用 **msginit** 创建各语言 .po 文件的基础，并在源代码演进时用 **msgmerge** 保持更新。

# CAVEATS

属于 gettext 的一部分。关键字必须与代码匹配。复杂字符串需谨慎处理。

# HISTORY

**xgettext** 是 GNU **gettext**（标准国际化系统）的一部分。它支撑着软件翻译工作流。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgfmt](/man/msgfmt)(1), [msginit](/man/msginit)(1), [msgmerge](/man/msgmerge)(1)
