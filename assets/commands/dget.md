# TAGLINE

Debian 软件包与源码下载工具

# TLDR

下载一个**二进制软件包**

```dget [package]```

从 .dsc **下载并解压源码**

```dget [http://deb.debian.org/debian/pool/main/p/package/package_1.0.dsc]```

**仅下载**不解压

```dget -d [http://deb.debian.org/debian/pool/main/p/package/package_1.0.dsc]```

# SYNOPSIS

**dget** [_options_] _url_|_package_

# DESCRIPTION

**dget** 用于下载 Debian 软件包。它可以从软件仓库下载二进制包，也可以从 .dsc URL 下载源码包。给定 .dsc URL 时，它会获取所有源码组件，并可选地解压它们。

属于 devscripts 软件包的一部分，常用于软件包开发。

# PARAMETERS

**-d, --download-only**
> 仅下载，不解压

**-u, --unsigned**
> 不校验签名

**-x**
> 解压源码包

**-b**
> 仅在必要时才获取 .orig.tar

# CAVEATS

需要网络访问。除非使用 -u，否则源码包下载要求有效的 GPG 签名。devscripts 的一部分。

# SEE ALSO

[apt-get](/man/apt-get)(8), [debuild](/man/debuild)(1)
