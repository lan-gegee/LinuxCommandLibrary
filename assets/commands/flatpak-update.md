# TAGLINE

更新已安装的 Flatpak 应用程序和运行时

# TLDR

**更新所有**已安装的应用和运行时

```flatpak update```

更新所有内容并**自动确认**提示

```flatpak update -y```

更新**特定应用**

```flatpak update [com.example.app]```

**降级**到特定提交

```flatpak update --commit [COMMIT_HASH] [com.example.app]```

仅更新**用户安装**

```flatpak update --user```

仅更新**系统安装**

```flatpak update --system```

只**下载**更新而不部署

```flatpak update --no-deploy```

# SYNOPSIS

**flatpak update** [_options_] [_ref..._]

**flatpak update** [_options_] **--appstream** [_remote_]

# PARAMETERS

**-u, --user**
> 更新按用户划分的安装

**--system**
> 更新系统级安装

**--commit** _commit_
> 更新到特定提交（可以降级）

**--no-pull**
> 不下载，直接部署本地已有的版本

**--no-deploy**
> 只下载更新而不部署

**--app**
> 仅更新应用程序

**--runtime**
> 仅更新运行时

**-y, --assumeyes**
> 自动对所有提示回答 yes

**--noninteractive**
> 输出最少信息，便于脚本化/自动化

**--appstream** [_remote_]
> 更新远程仓库的 appstream 元数据

**-v, --verbose**
> 输出调试信息

# DESCRIPTION

**Flatpak update** 从已配置的远程仓库将应用程序和运行时更新到最新版本。不带参数时，它会更新包括所有远程仓库 appstream 元数据在内的一切内容。

引用遵循 **(app|runtime)/ID/ARCH/BRANCH** 格式，其中大多数元素是可选的。该工具会自动解析不完整的引用。

该命令会在保留明确安装或固定的运行时的前提下，提议卸载不再使用的生命周期已结束的运行时。使用 **--commit** 可通过提交哈希更新或降级到特定版本。

# CAVEATS

更新可能需要大量下载带宽和磁盘空间。使用 **--commit** 固定特定版本会阻止自动安全更新。**--no-deploy** 选项适用于在慢速网络下预先下载更新。被屏蔽的应用（通过 **flatpak mask**）在更新时会被跳过。

# HISTORY

本命令是 Red Hat 的 Alexander Larsson 所开发 **Flatpak** 项目的一部分。Flatpak 约于 **2015 年**从 xdg-app 项目演化而来，为 Linux 提供与发行版无关的沙箱化应用分发系统。

# INSTALL

```apt: sudo apt install flatpak```

```dnf: sudo dnf install flatpak```

```pacman: sudo pacman -S flatpak```

```apk: sudo apk add flatpak```

```zypper: sudo zypper install flatpak```

```nix: nix profile install nixpkgs#flatpak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-install](/man/flatpak-install)(1), [flatpak-mask](/man/flatpak-mask)(1), [flatpak-remote-info](/man/flatpak-remote-info)(1)

# RESOURCES

```[Homepage](https://flatpak.org/)```

```[Source code](https://github.com/flatpak/flatpak)```

<!-- verified: 2026-07-15 -->
