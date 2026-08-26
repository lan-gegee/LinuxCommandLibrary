# TAGLINE

管理 CRUX Linux 的 ports 集合

# TLDR

**更新** ports 树

```ports -u```

**列出**当前树中的 ports

```ports -l```

显示已安装软件与 ports 之间的**差异**

```ports -d```

# SYNOPSIS

**ports** [**-u**|**-l**|**-d**]

# PARAMETERS

**-u**
> 从配置的源更新 ports 树

**-l**
> 列出当前树中的所有 ports

**-d**
> 显示已安装软件包与 ports 之间的差异

# DESCRIPTION

**ports** 管理 CRUX Linux 上的 ports 集合。ports 树包含软件包的构建配方（Pkgfile）。该工具将本地 ports 树与远程仓库同步。

差异选项有助于识别需要更新的软件包，以及从 ports 系统之外安装的软件包。

# CAVEATS

CRUX 专属工具。更新需要联网。驱动配置文件位于 `/etc/ports/`。它不会直接构建或安装软件包；请使用 **prt-get** 或 **pkgmk** 完成这些操作。

# HISTORY

**ports** 是 CRUX Linux 软件包管理系统的组成部分。CRUX 使用受 BSD 启发的基于 ports 的系统，软件包配方会被下载并在本地构建。

# SEE ALSO

[pkgmk](/man/pkgmk)(8), [pkgadd](/man/pkgadd)(8), [prt-get](/man/prt-get)(8)
