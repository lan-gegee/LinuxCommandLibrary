# TAGLINE

面向 Debian 软件包的 GPG 签名工具

# TLDR

**对 .changes 文件签名**

```debsign [package.changes]```

**使用指定密钥签名**

```debsign -k [KEYID] [package.changes]```

**仅对 .dsc 文件签名**

```debsign [package.dsc]```

**使用指定的维护者身份**签名

```debsign -m "[Name <email@example.com>]" [package.changes]```

**换用不同密钥重新签名**

```debsign -e "[newemail@example.com]" [package.changes]```

**对远程主机上的文件签名**

```debsign -r [user@remotehost] [package.changes]```

# SYNOPSIS

**debsign** [_options_] _changes-or-dsc-file_

# PARAMETERS

_FILE_
> 要签名的 .changes 或 .dsc 文件。

**-k** _KEYID_
> 用于签名的 GPG 密钥 ID。

**-m** _MAINTAINER_
> 指定用于签名的维护者。

**-e** _MAINTAINER_
> 与 -m 相同，但优先级更高。

**-r** [_username@_]_remotehost_
> 在指定的远程主机上签名文件，传输使用 scp。

**-p** _PROGNAME_
> 使用指定的 GPG 程序代替默认的 gpg。

**-S**
> 查找仅源码构建的 .changes 文件而非二进制构建的 .changes 文件。

**-a** _ARCH_
> 为 .changes 文件搜索指定 Debian 架构。

**--re-sign**
> 文件已被签名时重新创建签名。

**--no-re-sign**
> 文件已被签名时沿用现有签名。

**--debs-dir** _DIR_
> 在指定目录而非父目录中寻找要签名的文件。

**--no-conf**
> 不读取任何配置文件。必须是第一个选项。

**-h**, **--help**
> 显示帮助信息并退出。

**--version**
> 显示版本和版权信息。

# CONFIGURATION

**~/.devscripts**
> 配置文件，用于设置默认 GPG 密钥 ID 和签名行为。

# DESCRIPTION

**debsign** 模仿 dpkg-buildpackage(1) 的签名环节。它接收一个 .dsc、.buildinfo 或 .changes 文件，并使用 GPG 对其以及其中引用的所有子 .dsc、.buildinfo 或 .changes 文件进行签名。将软件包上传到 Debian 仓库时必须签名，因为它可以验证软件包维护者的身份。

该工具根据被签名文件中维护者字段找到相应的 GPG 密钥，也可以使用显式指定的密钥。它为文件添加 GPG 签名，供软件包上传和安装过程中验证。

debsign 通常在使用 dpkg-buildpackage 或 debuild 构建 Debian 软件包之后、上传到仓库之前作为最后一步使用。

# CAVEATS

需要有效的 GPG 密钥。签名密钥必须被仓库信任。签名后再修改文件内容会使签名失效。私钥必须可用于签名。

# HISTORY

debsign 属于 **devscripts** 软件包，是为 Debian 软件包维护开发的工具。自软件包上传要求 GPG 签名以来，它一直是 Debian 上传流程中的核心工具。

# SEE ALSO

[gpg](/man/gpg)(1), [debuild](/man/debuild)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1)
