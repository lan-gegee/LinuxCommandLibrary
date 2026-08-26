# TAGLINE

OpenPGP 和 PIV 智能卡管理

# TLDR

**列出可用的智能卡**

```gpg-card list```

**显示卡片信息**

```gpg-card info```

**修改 PIN**

```gpg-card passwd```

**设置持卡人姓名**

```gpg-card name```

**从卡片 URL 获取公钥**

```gpg-card fetch```

**在卡上生成密钥**

```gpg-card generate```

**将卡片恢复出厂设置**

```gpg-card factory-reset```

# SYNOPSIS

**gpg-card** [_options_] [_command_ [_args_]]

# SUBCOMMANDS

**list**
> 列出可用的卡片和读卡器。

**info**
> 显示卡片信息。

**name**
> 设置持卡人姓名。

**lang**
> 设置语言偏好。

**url**
> 设置公钥 URL。

**fetch**
> 从卡上记录的 URL 获取密钥。

**passwd**
> 修改 PIN、Admin PIN 或重置码（Reset Code）。

**generate**
> 在卡上生成密钥。

**keytocard**
> 将密钥传输到卡上。

**forcesig**
> 切换签名是否必须输入 PIN。

**factory-reset**
> 将卡片恢复出厂设置。

# DESCRIPTION

**gpg-card** 是 GnuPG 中用于管理 OpenPGP 和 PIV 智能卡的工具。它提供交互式界面，可用于配置卡片、管理 PIN、生成密钥以及将密钥传输到智能卡。

它随 GnuPG 2.3 推出，用来取代较旧的 **gpg --card-edit** 工作流，为智能卡操作提供了更精简的命令行体验。

# INSTALL

```apt: sudo apt install scdaemon```

```apk: sudo apk add gnupg-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1)
