# TAGLINE

查询 Arch 用户仓库（AUR）的轻量工具。

# TLDR

**搜索**匹配正则表达式的 AUR 软件包

```auracle search '[regex]'```

显示一个或多个 AUR 软件包的**信息**

```auracle info [package1] [package2] ...```

显示一个或多个 AUR 软件包的 **PKGBUILD**

```auracle show [package1] [package2] ...```

显示已安装 AUR 软件包的**更新**

```auracle outdated```

连同依赖一起递归**克隆**软件包仓库

```auracle clone --recurse [package]```

# SYNOPSIS

**auracle** _command_ [_options_] [_packages_]

# DESCRIPTION

**auracle** 是一款用于查询 Arch User Repository（AUR）的轻量级命令行工具。它提供快速搜索、软件包信息查询和更新检查功能，但不负责构建或安装软件包。

auracle 用 C++ 编写，专注于 AUR 查询而非完整的包管理。它设计为与其他工具或脚本配合使用，构成完整的 AUR 工作流。

# SUBCOMMANDS

**search** _pattern_
> 在 AUR 中搜索匹配该模式（正则表达式）的软件包

**info** _packages_
> 显示指定软件包的详细信息

**show** _packages_
> 打印软件包的 PKGBUILD 文件

**outdated**
> 列出有可用更新的已安装 AUR 软件包

**clone** _packages_
> 克隆软件包的 git 仓库

**download** _packages_
> 下载有更新的软件包，可选 `--recurse` 同时下载新的依赖

**buildorder** _packages_
> 显示构建给定一组 AUR 软件包所需的构建顺序和来源

**rawsearch** _pattern_
> 输出某次搜索请求从 AUR 返回的原始 JSON 响应

**rawinfo** _packages_
> 输出某次 info 请求从 AUR 返回的原始 JSON 响应

# PARAMETERS

**-q**, **--quiet**
> 仅输出软件包名称（与 `search` 和 `outdated` 一起使用）

**--sort** _field_
> 按字段对搜索结果排序（name、votes、popularity）

**--rsort** _field_
> 按字段对搜索结果逆序排序

**--literal**
> 将搜索词视为字面字符串而非正则表达式

**--recurse**
> 递归跟进并处理依赖（与 `clone` 和 `download` 一起使用）

**--show-file** _file_
> 控制 `show` 子命令显示哪个源文件

**--search-by** _field_
> 按特定字段搜索（name、name-desc、maintainer、depends、makedepends、optdepends、checkdepends）

**--color** _when_
> 控制彩色输出：`auto`、`never` 或 `always`（默认：auto）

# CAVEATS

不构建也不安装软件包；安装时请配合 **makepkg** 或 AUR 助手使用。正则表达式应加引号以防止 Shell 展开。只查询 AUR API；不访问本地软件包数据库。

# SEE ALSO

[yay](/man/yay)(1), [paru](/man/paru)(1), [makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8)
