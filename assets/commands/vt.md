# TAGLINE

VirusTotal 命令行界面

# TLDR

**扫描文件**

```vt scan file [file]```

**获取文件报告**

```vt file [hash]```

**扫描 URL**

```vt scan url [https://example.com]```

**获取 URL 报告**

```vt url [url]```

**搜索**

```vt search "[query]"```

**下载文件**

```vt download [hash]```

# SYNOPSIS

**vt** _command_ [_subcommand_] [_options_] [_args_]

# PARAMETERS

**scan**
> 提交扫描。

**file**
> 文件操作。

**url**
> URL 操作。

**search**
> 搜索 VT。

**download**
> 下载文件。

**--apikey** _KEY_
> API 密钥。

# DESCRIPTION

**vt** 是 VirusTotal 的官方命令行界面。VirusTotal 是一项在线服务，使用数十种防病毒引擎和安全工具分析文件和 URL 中的恶意软件。它在终端中提供对 VirusTotal 扫描与情报能力的直接访问。

该工具可以提交文件和 URL 进行扫描，按文件哈希或 URL 获取分析报告，在 VirusTotal 数据库中搜索已知威胁，并下载样本用于研究。结果包括来自多个防病毒引擎的检测判定、行为分析数据和社区信誉评分。

所有操作都需要 VirusTotal API 密钥，速率限制取决于账户级别。该 CLI 同时支持免费和付费 API 功能，对安全分析师、应急响应人员和自动化威胁检测工作流都很有用。

# CAVEATS

需要 API 密钥。有速率限制。更多功能需付费。

# HISTORY

**vt** 是 **VirusTotal**（Google 旗下的在线恶意软件扫描服务）的官方 CLI。

# INSTALL

```apt: sudo apt install vt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [clamav](/man/clamav)(1)
