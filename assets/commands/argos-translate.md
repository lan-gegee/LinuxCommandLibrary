# TAGLINE

离线神经机器翻译

# TLDR

在不同语言间**翻译**文本

```argos-translate --from-lang [en] --to-lang [es] "[Hello, world]"```

通过**管道输入**进行翻译

```echo "[Text]" | argos-translate --from-lang [en] --to-lang [de]```

**从文件翻译**

```argos-translate --from-lang [en] --to-lang [fr] < [input.txt]```

**安装**语言包（通过 argospm）

```argospm install translate-[en]_[es]```

**列出已安装的**语言包

```argospm list```

**更新**软件包索引并**搜索**可用软件包

```argospm update && argospm search --from-lang [en]```

# SYNOPSIS

**argos-translate** **--from-lang** _code_ **--to-lang** _code_ [_text_]

**argospm** _subcommand_ [_options_]

# DESCRIPTION

**argos-translate** 是基于 OpenNMT 神经机器翻译模型的开源离线翻译工具。它完全在本地运行，无需将数据发送到云服务，提供保护隐私的翻译。

语言以可下载的软件包形式提供，命名为 **translate-_from_\__to_**（如 `translate-en_es`）。软件包由配套的 **argospm** 命令管理，支持 update、search、install、list 和 remove 子命令。

# PARAMETERS

**-f** _code_, **--from-lang** _code_
> ISO 639-1 源语言代码（如 `en`、`es`、`fr`）。

**-t** _code_, **--to-lang** _code_
> ISO 639-1 目标语言代码。

**-h**, **--help**
> 显示帮助并退出。

# CAVEATS

必须先通过 **argospm** 安装语言包才能进行翻译。翻译质量因语言对而异，可能不及商业服务。首次运行时因加载模型而较慢；同一进程中的后续调用会更快。处理大文档时内存和 CPU 占用较高。

# HISTORY

**Argos Translate** 由 Argos Open Tech 开发，是云端翻译服务的开源、注重隐私的替代品，使用 CTranslate2 和 OpenNMT 模型。它也是可自托管的 LibreTranslate Web API 的底层引擎。

# INSTALL

```aur: yay -S argos-translate```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[trans](/man/trans)(1)
