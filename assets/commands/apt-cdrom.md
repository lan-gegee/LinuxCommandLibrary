# TAGLINE

将 CD-ROM 或 DVD-ROM 添加为 APT 软件包源

# TLDR

将 CD-ROM **添加**到软件源

```sudo apt-cdrom add```

添加时**不挂载**

```sudo apt-cdrom add -m```

**识别** CD-ROM 内容

```sudo apt-cdrom ident```

使用**特定挂载点**添加

```sudo apt-cdrom add -d [/media/cdrom]```

# SYNOPSIS

**apt-cdrom** [_-d mount_] [_-m_] [_-r_] _command_

# DESCRIPTION

**apt-cdrom** 将 CD-ROM 或 DVD-ROM 添加到 APT 的可用软件源列表。它会扫描光盘、识别其中的软件包，并将相应的条目添加到 /etc/apt/sources.list。

这对于离线安装或在无法访问互联网时使用发行版介质很有用。

# PARAMETERS

**add**
> 将光盘添加到软件源列表

**ident**
> 报告光盘标识而不进行添加

**-d** _path_
> CD-ROM 挂载点

**-m**, **--no-mount**
> 不挂载/卸载光盘

**-r**, **--rename**
> 提示输入光盘标签

**-f**, **--fast**
> 快速复制（假定已知光盘结构）

**-a**, **--thorough**
> 彻底扫描软件包

# CONFIGURATION

**/etc/apt/sources.list**
> CD-ROM 条目作为软件包源被添加到的文件。

**/etc/apt/apt.conf**
> APT 配置文件，可在其中设置 CD-ROM 挂载点和行为选项。

# CAVEATS

CD-ROM 软件源的优先级低于网络仓库。物理介质会随时间老化。大多数现代安装都改用网络源。

# HISTORY

在 Linux 发行版主要通过物理介质分发的年代，**apt-cdrom** 是必不可少的工具。它至今仍然可用，但自从宽带互联网普及后就很少被使用了。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8)
