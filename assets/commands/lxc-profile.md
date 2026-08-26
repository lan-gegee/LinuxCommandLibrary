# TAGLINE

管理 LXD 容器和虚拟机的配置 profile

# TLDR

**列出**所有可用的 profile

```lxc profile list```

**查看**指定 profile 的配置

```lxc profile show [profile_name]```

在默认编辑器中**编辑**指定的 profile

```lxc profile edit [profile_name]```

**创建**新的 profile

```lxc profile create [profile_name]```

使用指定的 profile **启动**新容器

```lxc launch [container_image] [container_name] -p [profile1] -p [profile2]```

**更改**运行中容器的 profile

```lxc profile assign [container_name] [profile1,profile2]```

# SYNOPSIS

**lxc profile** _command_ [_options_]

# PARAMETERS

**list**
> 列出所有可用的 profile

**show _profile_**
> 显示一个 profile 的完整配置

**edit _profile_**
> 在默认编辑器中打开一个 profile 进行编辑

**create _profile_**
> 创建一个新的空 profile

**delete _profile_**
> 移除一个 profile

**copy _source_ _dest_**
> 将 profile 复制为新名称

**rename _old_ _new_**
> 重命名 profile

**assign _instance_ _profiles_**
> 设置实例的 profile（逗号分隔列表）

**add _instance_ _profile_**
> 向实例现有的 profile 中添加一个 profile

**remove _instance_ _profile_**
> 从实例中移除一个 profile

**set _profile_ _key_ _value_**
> 设置 profile 的配置键

**get _profile_ _key_**
> 获取 profile 的配置值

**device add _profile_ _device_ _type_ [_options_]**
> 向 profile 添加设备

**device remove _profile_ _device_**
> 从 profile 中移除设备

# DESCRIPTION

**lxc profile** 管理 LXD 容器和虚拟机的配置 profile。profile 定义了可复用的配置选项集合，包括资源限制、设备映射、网络设置和安全策略。

容器可以使用多个 profile，它们按顺序应用（后面的 profile 会覆盖前面的）。**default** profile 会自动应用到新容器上，通常包含基本的网络和存储配置。

Profile 配置采用 YAML 格式，用于指定 CPU/内存限制、磁盘配额、网络接口以及 GPU 直通等选项。

# CAVEATS

对 profile 的更改不会自动应用到运行中的容器；请重启容器或重新分配 profile 以使更改生效。删除正在被容器使用的 profile 会失败。default profile 无法删除。

# INSTALL

```apt: sudo apt install lxd-client```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc](/man/lxc)(1), [lxc-create](/man/lxc-create)(1), [lxc-start](/man/lxc-start)(1), [lxc-ls](/man/lxc-ls)(1)
