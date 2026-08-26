# TAGLINE

启用 SteamOS 开发者模式

# TLDR

**启用**开发者模式

```sudo steamos-devmode enable```

**无需确认**地启用

```sudo steamos-devmode enable --no-prompt```

检查开发者模式**状态**

```sudo steamos-devmode status```

# SYNOPSIS

**steamos-devmode** _command_ [_OPTIONS_]

# COMMANDS

**enable**
> 启用开发者模式

**status**
> 检查开发者模式是否已启用

# PARAMETERS

**--no-prompt**
> 启用时跳过确认提示

# DESCRIPTION

**steamos-devmode** 在 SteamOS（Steam Deck）上启用开发者模式，这会禁用只读文件系统保护并初始化 pacman 包管理器。这样就可以安装额外软件、修改系统文件以及自定义操作系统。

开发者模式面向想把 Steam Deck 当作完整 Linux 桌面使用、安装开发工具或在默认配置之外定制系统的高级用户。

# CAVEATS

会禁用防止修改系统的只读保护。系统更新可能覆盖开发者模式下的更改。不面向普通用户。使用不当可能影响系统稳定性。需要 root 权限。

# HISTORY

**steamos-devmode** 属于 **SteamOS 3.0**，由 **Valve** 为 **2022 年 2 月**发布的 **Steam Deck** 开发。SteamOS 3.0 基于 Arch Linux，默认使用不可变文件系统。提供开发者模式是为了让高级用户能够修改系统，同时保留锁定主机体验的选项。

# SEE ALSO

[steamos-readonly](/man/steamos-readonly)(1), [pacman](/man/pacman)(8), [steamos-add-to-steam](/man/steamos-add-to-steam)(1)
