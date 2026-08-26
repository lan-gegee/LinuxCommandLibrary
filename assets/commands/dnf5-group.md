# TAGLINE

在 DNF5 中管理软件包组

# TLDR

**列出所有可用和已安装的组**

```dnf5 group list```

**仅列出已安装的组**

```dnf5 group list --installed```

**显示组的详细信息**

```dnf5 group info [group_name]```

**安装组（必选和默认软件包）**

```dnf5 group install [group_name]```

**安装组并包括可选软件包**

```dnf5 group install --with-optional [group_name]```

**移除组及其专属软件包**

```dnf5 group remove [group_name]```

**升级一个组**

```dnf5 group upgrade [group_name]```

# SYNOPSIS

**dnf5 group** {**list**|**info**} [_options_] [_group-spec_...]

**dnf5 group** {**install**|**remove**|**upgrade**} [_options_] _group-spec_...

# PARAMETERS

**list**
> 列出所有匹配的组，可以是已安装或可用的。

**info**
> 打印组的详细信息。接受与 list 相同的选项。

**install**
> 将该组标记为已安装，并安装其必选和默认软件包。

**remove**
> 将该组标记为已移除，并删除不属于其他已安装组的软件包。

**upgrade**
> 升级组的定义及属于该组的软件包。

**--available**
> 仅显示可用（未安装）的组。

**--installed**
> 仅显示已安装的组。

**--hidden**
> 同时显示隐藏的组。

**--contains-pkgs** _PACKAGE_NAME_
> 仅显示包含指定名称软件包的组。支持通配符。

**--with-optional**
> 包含组中的可选软件包（仅限 install）。

**--no-packages**
> 只操作组本身而不改动任何软件包（install/remove）。

# DESCRIPTION

**dnf5 group** 管理 DNF5 中的虚拟软件包集合。组将相关的软件打包在一起，例如"Development Tools"或"Server"。

注意：Fedora 37 至 40 上，`dnf` 运行的是 DNF v4，而 `dnf5` 运行 DNF v5。从 Fedora 41 开始，`dnf` 成为 `dnf5` 的别名。

# INSTALL

```dnf: sudo dnf install dnf5```

```pacman: sudo pacman -S dnf5```

```zypper: sudo zypper install dnf5```

```nix: nix profile install nixpkgs#dnf5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf-group](/man/dnf-group)(8), [dnf5](/man/dnf5)(8)
