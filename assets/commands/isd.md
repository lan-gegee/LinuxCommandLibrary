# TAGLINE

交互式 systemd 单元管理器 TUI

# TLDR

**启动 isd** 浏览 systemd 单元

```isd```

**浏览用户单元**

```isd --user```

# SYNOPSIS

**isd** [**--user**] [_options_]

# DESCRIPTION

**isd**（interactive systemd）是一款用于管理 **systemd** 单元的 TUI，具备模糊搜索、自动刷新的预览和智能 sudo 处理。它提供能随终端大小自适应的流畅布局、带键盘快捷键的命令面板，以及支持自动补全的 YAML 配置。

该工具为高级用户和新手都提供了功能，包括在系统单元和用户单元之间切换、使用分页器查看单元详情，以及缓存常用条目的输入状态。

# CAVEATS

需要 **Python 3.11** 或更高版本。仅支持带有 systemd 的 Linux 系统。部分操作需要 root 权限，isd 会通过智能 sudo 检测来处理。

# HISTORY

**isd** 由 **kainctl** 创建，采用 **Python** 编写。其设计初衷是作为 systemctl 命令更易用的替代品，用于日常 systemd 管理任务。

# INSTALL

```pacman: sudo pacman -S isd```

```nix: nix profile install nixpkgs#isd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1)
