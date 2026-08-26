# TAGLINE

统一的 Arch Linux 软件包管理器 CLI

# TLDR

从所有来源（仓库、AUR、Flatpak、AppImage）**升级所有软件包**

```shelly upgrade-all```

**安装**来自软件仓库的软件包

```shelly install [package]```

**移除**已安装的软件包及其不再需要的依赖

```shelly remove --cascade [package]```

在标准仓库中**搜索**可用软件包

```shelly query --available [search_term]```

**搜索** AUR

```shelly aur search [search_term]```

**清理孤立软件包**（作为依赖安装但已不再需要的包）

```shelly purify --orphans```

**安装时无需确认提示**

```shelly install --no-confirm [package]```

# SYNOPSIS

**shelly** [_options_] \<command\> [_args_]

# DESCRIPTION

**shelly** 是 Shelly（Shelly-ALPM）的命令行界面，后者是一款面向 Arch Linux 的现代统一软件包管理器。它通过一个 CLI 完成对标准 ALPM 仓库、AUR、Flatpak 和 AppImage 软件包的安装、更新、搜索和删除。

直接子命令覆盖常见的生命周期操作：**install**、**remove**、**upgrade**、**upgrade-all**、**query**、**update**、**downgrade**、**purify**、**sync**、**news** 以及缓存/密钥环工具。分组子命令处理专门的来源：**shelly aur**、**shelly flatpak** 和 **shelly appimage**。配置通过 **shelly config** 管理。

全局选项如 **--no-confirm**（别名 **-n**）、**--json**（**-j**）、**--verbose**（**-v**）和 **--ui-mode**（**-U**）适用于所有子命令。形如 **-\<Type\>\<Action\>…** 的可选短代码将类型字母（例如 **S** 标准仓库、**A** AUR、**F** Flatpak）映射为动词，便于紧凑调用。

Shelly 还附带独立的 GUI；此处记录的 CLI 二进制文件是可脚本化的入口。在 CachyOS 上，它可以作为发行版仓库中的 **shelly** 软件包安装。

# PARAMETERS

**install** [_packages…_]
> 从仓库、本地文件或 URL 安装软件包。

**remove** [_packages…_]
> 移除软件包。**--cascade**（**-c**）同时移除不需要的反向依赖；**--ripple**（**-i**）移除依赖于目标的软件包。

**upgrade**
> 对标准软件包执行完整的系统升级。

**upgrade-all**
> 升级来自所有来源的软件包（repo、AUR、Flatpak、AppImage）。可用 **--no-aur**、**--no-flatpak**、**--no-appimage** 或 **--no-repo** 跳过某个来源。

**query** [_package_]
> 查询仓库和软件包（默认包含已安装和可用的）。支持 **--available**（**-a**）、**--installed**（**-i**）、**--detail**/**--info**（**-d**）。

**aur search** \<query…\>
> 搜索 Arch 用户仓库（AUR）。

**aur install** [_packages…_]
> 构建并安装 AUR 软件包。

**flatpak** … / **appimage** …
> 分别管理 Flatpak 应用和 AppImage。

**purify**
> 移除损坏的软件包；**--orphans**（**-o**）还会移除孤立的依赖。

**config get|set|list|reset|parallel**
> 读取或修改 Shelly 配置值。

**--no-confirm**, **-n**
> 禁用确认提示。

**--json**, **-j**
> 输出 JSON 以便脚本处理。

**--version**
> 显示版本信息。

# CAVEATS

仅限 Arch Linux（及使用 ALPM 的衍生发行版）；不是通用的多发行版包管理器。AUR 构建会执行 PKGBUILD 脚本，需要可用的构建工具链。特权操作通常需要 root 或配置好的提权助手。该 GUI 和 CLI 与其他不相关的 "Shelly" 项目（智能家居设备、SSH 客户端）共用名称；本页面记录的是 Seafoam Labs 的 Arch 软件包管理器 CLI。

# INSTALL

```aur: yay -S shelly```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(8), [paru](/man/paru)(8), [flatpak](/man/flatpak)(1)

# RESOURCES

```[Source code](https://github.com/Seafoam-Labs/Shelly-ALPM)```

```[Documentation](https://www.seafoam-labs.org/shelly-alpm/docs/cli-reference/)```

<!-- verified: 2026-07-22 -->
