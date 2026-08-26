# TAGLINE

用于离线翻译模型的 Argos Translate 软件包管理器

# TLDR

**更新**远程软件包索引

```argospm update```

**搜索**翻译软件包

```argospm search --from-lang [en] --to-lang [es]```

**安装**翻译软件包

```argospm install [translate-en_es]```

**列出**已安装的翻译软件包

```argospm list```

**删除**已安装的翻译软件包

```argospm remove [translate-en_es]```

# SYNOPSIS

**argospm** [**-h**] {**update**,**search**,**install**,**list**,**remove**} [_args_]

# PARAMETERS

**update**
> 从 Argos Translate 软件包仓库下载远程软件包索引。

**search**
> 在远程索引中搜索可用的翻译软件包。使用 **--from-lang** 和 **--to-lang** 按语言对过滤。

**install**
> 按名称安装翻译软件包（如 translate-en_es）。

**list**
> 列出当前已安装的所有翻译软件包。

**remove**
> 按名称删除已安装的翻译软件包。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**argospm** 是 **Argos Translate** 的软件包管理 CLI。Argos Translate 是一个开源离线翻译库，argospm 负责管理翻译语言包（神经机器翻译模型）的下载与安装，从而实现语言对之间的离线文本翻译。

每个软件包提供特定源语言与目标语言之间的翻译。软件包从 Argos Translate 软件包索引下载并存储在本地，供 **argos-translate** Python 库和 **LibreTranslate** Web 界面使用。

# CAVEATS

翻译软件包包含神经网络模型，体积可能较大。搜索或安装新软件包前必须先用 **argospm update** 更新软件包索引。质量因语言对而异——英语-西班牙语等资源丰富的语言对比不常见的语言对翻译质量更好。

# HISTORY

**argospm** 是 **Argos Translate** 项目的一部分，该项目是用 **Python** 基于 **OpenNMT** 构建的开源神经机器翻译库。项目由 **Argos Open Technologies** 创建，旨在提供免费、离线的翻译能力，作为基于云的服务的替代方案。它同样是可自托管翻译 API **LibreTranslate** 的底层引擎。

# SEE ALSO

[argos-translate](/man/argos-translate)(1), [trans](/man/trans)(1), [pip](/man/pip)(1)
