# TAGLINE

TeX Live 交互式配置工具

# TLDR

启动交互式 TeX Live 配置菜单

```texconfig```

显示当前 TeX Live 配置

```texconfig conf```

# SYNOPSIS

**texconfig** [_option_] [_command_]

# DESCRIPTION

**texconfig** 提供一个基于 curses 的交互式界面（以及非交互式的命令行界面）来配置 TeX Live 安装。它让你无需手动编辑 `texmf.cnf` 或格式文件，即可更改纸张尺寸、默认模式、断字模式以及许多其他 TeX 引擎和格式设置。

常见任务包括：

- 在 A4 和 letter 纸张之间切换
- 启用或禁用特定语言的断字模式
- 配置更改后重建格式文件
- 查看和编辑 TeX Live 主配置文件

# PARAMETERS

**conf**  
> 打印当前配置（非交互式）

**paper**  
> 设置默认纸张尺寸（a4 或 letter）

**formats**  
> 重建格式文件

**hyphen**  
> 管理断字模式

不带参数运行 `texconfig` 会启动全屏交互式配置器。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tlmgr](/man/tlmgr)(1), [tex](/man/tex)(1)
