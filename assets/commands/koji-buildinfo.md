# TAGLINE

显示 Koji 构建系统中构建任务的信息

# TLDR

输出构建任务的**基本信息**

```koji buildinfo [BuildID_or_NVR]```

输出带有**变更日志**的信息

```koji buildinfo [BuildID_or_NVR] --changelog```

显示**帮助**

```koji buildinfo -h```

# SYNOPSIS

**koji buildinfo** [_options_] _build_...

# PARAMETERS

_BuildID_or_NVR_
> 构建 ID 数字或 Name-Version-Release 字符串

**--changelog**
> 在输出中包含变更日志信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**koji buildinfo** 显示 Koji 构建系统中构建任务的信息。它会展示构建状态、所有者、标签、来源和时间戳等详情。

构建任务可以通过数字 ID 或 NVR（Name-Version-Release）格式指定，例如 "python-3.9.1-1.fc34"。

# CAVEATS

需要能访问 Koji hub 的网络。某些构建可能因访问控制而限制可见性。

# HISTORY

koji buildinfo 是 Koji 构建系统的一部分，Fedora、CentOS 及其他基于 RPM 的发行版用它进行软件包构建和管理。

# INSTALL

```dnf: sudo dnf install koji```

```brew: brew install koji```

```nix: nix profile install nixpkgs#koji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[koji](/man/koji)(1), [koji-download-build](/man/koji-download-build)(1), [koji-tag-build](/man/koji-tag-build)(1)
