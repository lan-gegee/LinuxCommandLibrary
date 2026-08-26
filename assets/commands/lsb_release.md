# TAGLINE

显示 Linux Standard Base 及发行版专属信息

# TLDR

打印**全部信息**

```lsb_release --all```

打印**描述信息**

```lsb_release --description```

以短格式打印 **OS ID**

```lsb_release -is```

打印**版本号和代号**

```lsb_release -rcs```

# SYNOPSIS

**lsb_release** [_options_]

# DESCRIPTION

**lsb_release** 显示已安装 Linux 发行版的 Linux Standard Base（LSB）及发行版专属信息，包括发行商 ID、描述、版本号和代号。

# PARAMETERS

**-a, --all**
> 打印所有可用信息

**-d, --description**
> 打印发行版描述

**-i, --id**
> 打印发行商 ID

**-r, --release**
> 打印版本号

**-c, --codename**
> 打印代号

**-s, --short**
> 短输出格式（省略字段名）

**-v, --version**
> 打印 LSB 版本

# CAVEATS

并非所有发行版都提供该命令。有些发行版改用 /etc/os-release 文件提供此类信息。

# INSTALL

```dnf: sudo dnf install lsb_release```

```apk: sudo apk add lsb-release-minimal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostnamectl](/man/hostnamectl)(1), [uname](/man/uname)(1)
