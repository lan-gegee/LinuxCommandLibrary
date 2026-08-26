# TAGLINE

Debian 软件包构建工具

# TLDR

**构建软件包**

```dpkg-buildpackage```

**不签名构建**

```dpkg-buildpackage -us -uc```

**只构建二进制**

```dpkg-buildpackage -b```

**只构建源码**

```dpkg-buildpackage -S```

**并行构建**

```dpkg-buildpackage -j[4]```

**不清理直接构建**

```dpkg-buildpackage -nc```

**指定签名密钥**

```dpkg-buildpackage -k[keyid]```

# SYNOPSIS

**dpkg-buildpackage** [_options_]

# DESCRIPTION

**dpkg-buildpackage** 从源码构建 Debian 软件包。它统筹完整的构建流程，包括解压源码、运行构建系统以及创建 .deb 文件。

该工具处理依赖关系，运行 debian/rules 目标，调用 dpkg-source 生成源码包、dpkg-genchanges 生成上传文件。它是构建 Debian 软件包的标准方式。

# PARAMETERS

**-b**
> 仅构建二进制。

**-S**
> 仅构建源码。

**-F**
> 完整构建（源码加二进制）。

**-us**
> 不签名源码包。

**-uc**
> 不签名 changes 文件。

**-j** _n_
> 并行任务数。

**-nc**
> 构建前不清理。

**-tc**
> 构建后清理。

**-k** _keyid_
> 用于签名的 GPG 密钥。

**-r** _cmd_
> 用 cmd 获取 root 权限。

**-d**
> 不检查依赖。

**--build=** _type_
> 指定构建类型。

# CAVEATS

需要已安装构建依赖。签名需要 GPG 密钥。必须在软件包源码目录中运行。要实现可重现构建，建议使用干净的环境。

# HISTORY

**dpkg-buildpackage** 是 **dpkg** 工具套件的一部分，dpkg 自 **1994 年**起就是 Debian 软件包管理的核心。它随 Debian 打包实践的演进而发展，多年来陆续加入了对源码格式、签名和交叉编译的支持。

# INSTALL

```dnf: sudo dnf install dpkg-dev```

```apk: sudo apk add dpkg-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg](/man/dpkg)(1), [dpkg-deb](/man/dpkg-deb)(1), [debuild](/man/debuild)(1), [pbuilder](/man/pbuilder)(1)
