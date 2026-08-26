# TAGLINE

从 mega 下载文件和文件夹

# TLDR

从 mega.nz 链接**下载文件**到当前目录

```megatools-dl [https://mega.nz/...]```

下载文件到**指定目录**

```megatools-dl --path [path/to/directory] [https://mega.nz/...]```

以交互方式**选择**要下载的文件

```megatools-dl --choose-files [https://mega.nz/...]```

以 KiB/s 为单位**限制下载速度**

```megatools-dl --limit-speed [speed] [https://mega.nz/...]```

# SYNOPSIS

**megatools-dl** [_options_] _URL_

# PARAMETERS

**--path _directory_**
> 将文件下载到指定目录

**--choose-files**
> 以交互方式选择要从文件夹下载的文件

**--limit-speed _KiB/s_**
> 限制下载带宽

**--no-progress**
> 禁用进度指示器

**--print-names**
> 将已下载文件的名称输出到标准输出

# DESCRIPTION

**megatools-dl** 用于从 mega.nz 云存储链接下载文件和文件夹。作为 **megatools** 工具集的一部分，它提供对 Mega 文件托管服务的命令行访问，公开链接无需账户即可使用。

该工具同时支持文件链接和文件夹链接，并会为文件夹下载自动创建目录结构。它支持恢复中断的下载，并可限制带宽消耗。

对于受保护的链接或私有文件，可通过配置文件或 megatools 工具集的命令行选项提供身份验证。

# CAVEATS

Mega.nz 的链接格式偶尔会变化；请确保 megatools 为最新版本。大型下载可能受 Mega 传输配额的限制。密码保护的链接需要 URL 中包含解密密钥或以交互方式输入。

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [aria2c](/man/aria2c)(1)
