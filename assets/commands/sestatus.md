# TAGLINE

报告 SELinux 状态与配置

# TLDR

**打印**当前 SELinux 状态

```sestatus```

**打印**所有策略布尔值的状态

```sestatus -b```

**打印**文件和进程上下文

```sestatus -v```

# SYNOPSIS

**sestatus** [_-v_] [_-b_]

# PARAMETERS

**-b**
> 显示所有策略布尔值的当前状态

**-v**
> 显示 /etc/sestatus.conf 中指定的文件和进程的安全上下文

# DESCRIPTION

**sestatus** 报告 SELinux 系统的当前状态。它显示 SELinux 是否启用、当前模式（enforcing、permissive 或 disabled）、已加载的策略类型以及各种安全设置。

典型输出包括 SELinux 状态、已加载的策略、当前模式、策略版本，以及是否存在被拒绝的策略访问。

# OUTPUT FIELDS

**SELinux status**: enabled/disabled
**SELinuxfs mount**: path to SELinux filesystem
**SELinux root directory**: SELinux configuration location
**Loaded policy name**: targeted, mls, etc.
**Current mode**: enforcing, permissive, disabled
**Mode from config file**: configured default mode
**Policy MLS status**: MLS/MCS status
**Policy deny_unknown status**: how unknown access is handled
**Memory protection checking**: protection mode

# CAVEATS

仅在安装了 SELinux 的系统上可用。需要对 SELinux 文件系统和配置文件的读取权限。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getenforce](/man/getenforce)(8), [setenforce](/man/setenforce)(8), [semanage](/man/semanage)(8)
