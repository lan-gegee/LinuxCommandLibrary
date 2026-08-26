# TAGLINE

保存和恢复 KDE Plasma 桌面自定义配置

# TLDR

将当前配置**保存**为 profile

```konsave -s [profile_name]```

**应用**一个 profile

```konsave -a [profile_name]```

**保存并覆盖**已有 profile

```konsave -s [profile_name] -f```

**列出**所有 profile

```konsave -l```

**移除**一个 profile

```konsave -r [profile_name]```

将 profile **导出**为 .knsv 文件

```konsave -e [profile_name]```

**导入**一个 .knsv profile

```konsave -i [path/to/profile.knsv]```

# SYNOPSIS

**konsave** [_options_] [_profile_name_]

# PARAMETERS

**-s**, **--save** _NAME_
> 将当前配置保存为指定名称的 profile

**-a**, **--apply** _NAME_
> 应用一个已保存的 profile

**-l**, **--list**
> 列出所有已保存的 profile

**-r**, **--remove** _NAME_
> 移除一个 profile

**-e**, **--export-profile** _NAME_
> 将 profile 导出为 .knsv 文件

**-i**, **--import-profile** _FILE_
> 从 .knsv 文件导入 profile

**-f**, **--force**
> 保存时覆盖已有的 profile

# DESCRIPTION

**konsave** 保存和恢复 KDE Plasma 桌面的自定义配置。它会捕获主题设置、图标包、壁纸以及其他视觉自定义项。

Profile 可以导出并与他人分享，方便在不同机器之间复制桌面配置，或与社区分享美化方案。

# CAVEATS

主要为 KDE Plasma 设计。某些配置在不同系统环境之间可能无法完美迁移。导入的 profile 可能需要额外安装主题/图标所需的软件包。

# HISTORY

konsave 的创建是为了简化备份、分享和切换 KDE Plasma 桌面配置的过程，满足了注重自定义的 Linux 社区中的一个普遍需求。

# INSTALL

```nix: nix profile install nixpkgs#konsave```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-colorscheme](/man/plasma-apply-colorscheme)(1), [lookandfeeltool](/man/lookandfeeltool)(1)
