# TAGLINE

Red Hat 系统的 RPM 软件包管理器

# TLDR

**查询**软件包版本

```rpm -q [package]```

列出**所有**匹配的软件包

```rpm -qa '[pattern*]'```

**强制安装**软件包

```rpm -U [package.rpm] --force```

查找**文件所属的软件包**

```rpm -qf [/path/to/file]```

列出**软件包内的文件**

```rpm -ql [package]```

显示软件包**脚本**

```rpm -qp --scripts [package.rpm]```

**校验**软件包

```rpm -Va '[pattern*]'```

显示**变更日志**

```rpm -q --changelog [package]```

# SYNOPSIS

**rpm** [**-q**|**-i**|**-U**|**-e**|**-V**] [_options_] [_package_]

# MODES

**-q, --query**
> 查询已安装的软件包

**-i, --install**
> 安装软件包

**-U, --upgrade**
> 升级或安装软件包

**-e, --erase**
> 删除软件包

**-V, --verify**
> 校验软件包完整性

# PARAMETERS

**-a, --all**
> 所有软件包

**-f, --file _file_**
> 查询拥有该文件的软件包

**-l, --list**
> 列出软件包中的文件

**-p, --package _file_**
> 查询软件包文件

**--force**
> 强制执行操作

**--nodeps**
> 忽略依赖关系

**--scripts**
> 显示脚本小程序（scriptlets）

# DESCRIPTION

**rpm** 是面向 Red Hat 系 Linux 发行版的 RPM 包管理器。它负责安装、升级、删除和查询 RPM 格式的软件包。

该工具维护着一个已安装软件包的数据库，处理依赖关系，并可以校验软件包完整性。它是底层级的软件包工具；dnf/yum 在其之上提供更高层级的功能。

# CAVEATS

不会自动解决依赖关系（请改用 dnf/yum）。应当校验软件包签名。--force 和 --nodeps 选项可能破坏系统。安装/删除需要 root 权限。

# HISTORY

**RPM** 最初由 Red Hat 的 Marc Ewing 和 Erik Troan 开发。它已成为包括 Fedora、RHEL、CentOS 和 SUSE 在内众多 Linux 发行版的标准软件包格式。

# INSTALL

```apt: sudo apt install rpm```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf](/man/dnf)(8), [yum](/man/yum)(8), [rpm2cpio](/man/rpm2cpio)(8), [rpmbuild](/man/rpmbuild)(8)
