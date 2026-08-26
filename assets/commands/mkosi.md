# TAGLINE

构建定制化的现代 Linux 操作系统镜像

# TLDR

显示当前的**构建配置**以确认将要构建的内容

```mkosi summary```

以指定的发行版**构建镜像**

```mkosi build --distribution [fedora|debian|ubuntu|arch|opensuse]```

构建镜像并在容器中运行**交互式 Shell**

```mkosi shell```

在虚拟机中**启动镜像**

```mkosi vm```

**强制重建**已有镜像

```mkosi -f build```

**清理**构建产物

```mkosi clean```

显示**帮助**

```mkosi help```

# SYNOPSIS

**mkosi** [_options_] {**build**|**shell**|**boot**|**vm**|**ssh**|**clean**|**summary**|**genkey**|**help**}

# PARAMETERS

**build**
> 生成镜像（未指定动词时的默认行为）

**shell**
> 通过 systemd-nspawn 容器进入已构建镜像的交互式 Shell

**boot**
> 在镜像容器中引导 systemd

**vm** (alias: **qemu**)
> 在虚拟机中启动镜像（默认使用 QEMU）。

**ssh**
> 通过 SSH 连接到已启动的虚拟机

**clean**
> 移除构建产物

**summary**
> 显示人类可读的配置概览

**cat-config**
> 输出所有已加载配置文件的内容

**burn _device_**
> 将镜像写入块设备

**genkey**
> 生成 SecureBoot 密钥对

**-f, --force**
> 替换已有的输出；重复使用可清除缓存

**-i, --incremental**
> 启用构建之间的缓存

**-C, --directory _dir_**
> 处理前切换到指定目录

**--distribution _distro_**
> 目标发行版：fedora、debian、ubuntu、arch、opensuse 等

**--release _version_**
> 指定的发行版版本

**--format _type_**
> 输出类型：directory、tar、disk、uki 等

**--debug**
> 启用详细输出

# DESCRIPTION

**mkosi** 构建定制化的现代 Linux 操作系统镜像。它封装各软件包管理器（dnf、apt、pacman、zypper）来生成磁盘镜像、容器镜像和统一内核镜像，并提供丰富的自定义选项。

支持的输出格式包括原始 GPT 磁盘镜像、普通目录、tar 与 CPIO 归档、统一内核镜像（UKI）以及 OCI 兼容镜像。该工具支持多种发行版，并能创建带 systemd-boot 或 GRUB 的可引导镜像。

配置从 mkosi.conf 文件读取，支持声明式的镜像定义，包括配置档（profile）、条件段落和模块化配置。

# CAVEATS

在支持 reflink 的文件系统（XFS、btrfs）上运行 mkosi 可显著提升性能。连接虚拟机时 SELinux 可能阻止 sshd 访问 VSock。增量构建的缓存失效机制比较简单；需要干净重建时请用 -ff。部分功能需要 root 权限。

# HISTORY

**mkosi** 属于 **systemd** 项目，由 Lennart Poettering 等人开发。它的设计目标是利用 systemd-nspawn、systemd-repart 和统一内核镜像等 systemd 组件构建现代的、无遗留负担的 Linux 镜像。该工具强调可复现性和基于镜像的部署方式。

# INSTALL

```dnf: sudo dnf install mkosi```

```pacman: sudo pacman -S mkosi```

```apk: sudo apk add mkosi```

```zypper: sudo zypper install mkosi```

```nix: nix profile install nixpkgs#mkosi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-nspawn](/man/systemd-nspawn)(1), [systemd-repart](/man/systemd-repart)(8), [qemu](/man/qemu)(1)
