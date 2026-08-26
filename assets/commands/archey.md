# TAGLINE

以 ASCII 艺术标志展示系统信息

# TLDR

打印**系统摘要**（操作系统、内核、硬件）

```archey```

# SYNOPSIS

**archey** [_options_]

# DESCRIPTION

**archey** 是一个简单的工具，可在终端中美观地展示系统信息。它在系统详情旁边显示 Linux 发行版的 ASCII 艺术标志，内容包括操作系统、内核、运行时间、软件包数量、Shell、分辨率、桌面环境和硬件信息等。

# PARAMETERS

**-c, --color**
> 强制使用彩色输出

**-n, --no-color**
> 禁用彩色输出

# CONFIGURATION

**~/.config/archey4/config.yaml**
> archey4 的用户级配置，控制要显示的条目、颜色和标志。

**/etc/archey4/config.yaml**
> archey4 的系统级配置。

# CAVEATS

不同发行版存在不同的版本（archey、archey3、archey4）。显示内容因发行版和可用的系统信息而异。

# HISTORY

最初由 Melik Manukyan 为 **Arch Linux** 开发。存在多个分支，包括 archey3（Python 3）和 archey4。

# SEE ALSO

[neofetch](/man/neofetch)(1), [screenfetch](/man/screenfetch)(1), [fastfetch](/man/fastfetch)(1)

# RESOURCES

```[Source code](https://github.com/HorlogeSkynet/archey4)```

<!-- verified: 2026-06-11 -->
