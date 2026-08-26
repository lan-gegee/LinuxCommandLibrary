# TAGLINE

更新 Mageia 软件包仓库列表

# TLDR

更新**所有**已启用的介质

```urpmi.update -a```

按名称更新**特定**介质

```urpmi.update [medium1] [medium2]```

仅更新**更新类**介质（安全/缺陷修复仓库）

```urpmi.update --update```

带**下载限速**地更新所有介质

```urpmi.update -a --limit-rate [100k]```

以**安静**模式更新

```urpmi.update -a -q```

强制更新 GPG **密钥**

```urpmi.update -a --force-key```

# SYNOPSIS

**urpmi.update** [_OPTIONS_] [_MEDIUM_...]

# PARAMETERS

**-a**
> 更新所有已启用的非静态介质。

**--update**
> 仅使用更新类介质。

**--no-md5sum**
> 禁用 MD5SUM 文件检查。

**--force-key**
> 强制更新 GPG 密钥。

**-q**, **--quiet**
> 安静模式。

**-v**, **--verbose**
> 详细输出模式。

**--limit-rate** _rate_
> 限制下载速度，单位为字节/秒（可带 k、m 后缀）。

**--wget**
> 使用 wget 下载。

**--curl**
> 使用 curl 下载。

**--proxy** _url_
> 使用指定的 HTTP 代理。

**--proxy-user** _user:pass_
> 代理身份验证凭据。

# DESCRIPTION

**urpmi.update** 更新 Mageia Linux 中已配置仓库的软件包列表。在安装或升级软件包之前应先运行此命令，确保拿到的是最新的软件包列表。

在 Mageia 文档中，"medium"（介质）与"repository"（仓库）是同义词。

# CAVEATS

Mageia 专用。访问远程介质需要网络连接。应定期运行以获取安全更新。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmi.addmedia](/man/urpmi.addmedia)(8), [urpmi.removemedia](/man/urpmi.removemedia)(8), [urpme](/man/urpme)(8), [urpmq](/man/urpmq)(8)
