# TAGLINE

安全地移除过时的内核软件包

# TLDR

**移除旧内核，保留默认的最近 2 个**

```sudo purge-old-kernels```

**保留指定数量的旧内核**

```sudo purge-old-kernels --keep [3]```

**模拟移除而不做更改**

```sudo purge-old-kernels -s```

**无需确认提示即移除旧内核**

```sudo purge-old-kernels -y```

# SYNOPSIS

**purge-old-kernels** [_--keep N_] [_apt-get options..._]

# PARAMETERS

**--keep** _N_
> 要保留的旧内核数量。默认为 **2**。

_apt-get options_
> 任何额外的参数都会直接传递给 **apt-get**(8)。常见示例：**-y**（自动确认）、**-s**（模拟/干运行）、**-q**（安静模式）。

# DESCRIPTION

**purge-old-kernels** 从 Ubuntu 和 Debian 系统上移除旧的 Linux 内核和头文件包以回收磁盘空间，尤其是 **/boot** 分区的空间。随着时间推移，内核升级会积累不再需要的旧版本，该工具可自动化安全地移除它们。它绝不会移除当前正在运行的内核。

默认情况下，该工具保留最近的 **2** 个内核，可通过 **--keep** 选项配置。任何额外参数都会直接传递给 **apt-get**(8)，因此可以使用 **-s** 进行干运行模拟、使用 **-y** 跳过确认。该命令是 Ubuntu/Debian 系统上 **byobu** 软件包的一部分，需要 root 权限。

**注意：** 该工具现已弃用。其功能预计将被整合进 **apt**(8)。

# CAVEATS

仅适用于 Ubuntu/Debian。需要 root 权限。绝不会移除当前正在运行的内核。现已弃用，功能将整合进 apt(8)。

# HISTORY

purge-old-kernels 是为 **Ubuntu** 内核软件包清理而创建的。

# INSTALL

```dnf: sudo dnf install byobu```

```apk: sudo apk add byobu```

```zypper: sudo zypper install byobu```

```brew: brew install byobu```

```nix: nix profile install nixpkgs#byobu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [uname](/man/uname)(1)
