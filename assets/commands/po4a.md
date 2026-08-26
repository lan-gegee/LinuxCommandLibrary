# TAGLINE

通过 PO 文件维护文档翻译

# TLDR

**根据配置文件更新 PO 文件和已翻译的文档**

```po4a [path/to/config_file]```

**强制重新生成所有文件**

```po4a -f [path/to/config_file]```

**仅更新 PO 文件，跳过生成已翻译的文档**

```po4a --no-translations [path/to/config_file]```

**设置最低翻译百分比阈值**

```po4a -k [80] [path/to/config_file]```

# SYNOPSIS

**po4a** [_options_] _config_file_

# PARAMETERS

**-f**, **--force**
> 即使文件是最新的也强制处理。

**-v**, **--verbose**
> 提高详细程度。

**-q**, **--quiet**
> 降低详细程度。

**-d**, **--debug**
> 输出调试信息。

**--no-translations**
> 不生成已翻译的文档，仅更新 POT 和 PO 文件。

**--no-update**
> 不更新 POT 和 PO 文件，仅生成译文。

**-k**, **--keep** _threshold_
> 生成输出所需的最低翻译百分比（默认：80）。

**--keep-translations**
> 即使低于阈值也保留现有译文。

**--rm-translations**
> 移除低于阈值的已翻译文件。

**-o**, **--option** _opt_
> 格式插件的额外选项。

**-M**, **--master-charset** _charset_
> 源文档的字符编码。

**-L**, **--localized-charset** _charset_
> 已翻译文档的字符编码。

**--srcdir** _dir_
> 输入文档的基准目录。

**--destdir** _dir_
> 输出文档的基准目录。

**--msgmerge-opt** _options_
> 传递给 msgmerge 的额外选项。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**po4a**（PO for anything）使用 gettext PO 文件维护文档翻译。它从文档中提取可翻译的字符串，管理 PO 文件，并生成已翻译版本的文档。

该工具支持多种文档格式，包括 man page、POD、XML 等。它自动化了让译文与源文档保持同步的工作流程。

# CAVEATS

需要特定格式的模块。配置文件定义文档映射关系。PO 文件必须已存在或用 po4a-gettextize 创建。复杂文档可能需要手动调整。

# HISTORY

**po4a** 由 **Martin Quinson** 创建，旨在利用成熟的 gettext 工作流简化文档翻译。它支持使用标准的 PO 编辑工具进行协作翻译。

# INSTALL

```dnf: sudo dnf install po4a```

```pacman: sudo pacman -S po4a```

```apk: sudo apk add po4a```

```zypper: sudo zypper install po4a```

```brew: brew install po4a```

```nix: nix profile install nixpkgs#po4a```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[po4a-gettextize](/man/po4a-gettextize)(1), [po4a-translate](/man/po4a-translate)(1), [po4a-updatepo](/man/po4a-updatepo)(1), [gettext](/man/gettext)(1), [msgfmt](/man/msgfmt)(1)
