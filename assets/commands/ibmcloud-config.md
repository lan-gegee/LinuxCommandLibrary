# TAGLINE

管理 IBM Cloud CLI 配置

# TLDR

**显示配置**

```ibmcloud config --list```

**设置 HTTP 超时**

```ibmcloud config --http-timeout [60]```

**设置跟踪**

```ibmcloud config --trace [true]```

**设置彩色输出**

```ibmcloud config --color [true]```

**设置区域设置**

```ibmcloud config --locale [en_US]```

# SYNOPSIS

**ibmcloud config** [_options_]

# PARAMETERS

**--list**
> 显示所有设置。

**--http-timeout** _SEC_
> HTTP 超时。

**--trace** _BOOL_
> 启用跟踪。

**--color** _BOOL_
> 彩色输出。

**--locale** _LOCALE_
> 输出区域设置。

**--check-version** _BOOL_
> 版本检查。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ibmcloud config** 管理 IBM Cloud CLI 的配置。它用于设置超时、输出格式和行为等选项。

该命令存储当前用户的设置。设置在多个会话之间持久保存，并影响所有 ibmcloud 命令。

# CAVEATS

设置为用户级别。某些设置需要重启后生效。属于 ibmcloud CLI 的一部分。

# HISTORY

ibmcloud config 是 **IBM Cloud** CLI 配置系统的组成部分。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-login](/man/ibmcloud-login)(1)
