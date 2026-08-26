# TAGLINE

TeX Live 官方安装器，TeX Live 是一套完整的 TeX 发行版

# TLDR

**交互式启动 TeX Live 安装器**

```install-tl```

**以无人值守模式和默认设置安装 TeX Live**

```install-tl --no-interaction```

**从本地 ISO 或目录安装**

```install-tl --repository [/path/to/texlive/iso]```

**安装最小方案**（仅基础软件包）

```install-tl --scheme=small```

**指定自定义安装目录**

```install-tl --texdir=[/opt/texlive/2024]```

**使用指定的 profile 文件安装**

```install-tl --profile=[texlive.profile]```

# SYNOPSIS

**install-tl** [_-gui_] [_-no-gui_] [_-repository URL_] [_-scheme SCHEME_] [_-profile FILE_] [_-texdir DIR_] [_-no-interaction_] [_-help_]

# PARAMETERS

**-gui**
> 以 GUI 模式启动（需要 Perl/Tk）

**-no-gui**
> 强制使用文本模式安装

**-repository** _URL_
> 指定软件包仓库（本地路径或 URL）

**-scheme** _SCHEME_
> 安装方案：full、medium、small、basic、minimal 等

**-profile** _FILE_
> 使用 profile 文件中的设置进行自动化安装

**-texdir** _DIR_
> TeX Live 主安装目录

**-texmflocal** _DIR_
> 站点级本地文件目录

**-texmfhome** _DIR_
> 用户专属文件目录

**-portable**
> 便携式安装（USB 盘，不集成到系统）

**-no-interaction**
> 无人值守运行（自动化安装）

**-no-cls**
> 输出前不清屏

**-help**
> 显示帮助信息

# DESCRIPTION

**install-tl** 是 TeX Live 的官方安装器。TeX Live 是一个包含 LaTeX、字体及相关程序的完整 TeX 发行版。根据可用依赖和命令行选项，安装器可以在 GUI、文本或全自动模式下运行。

安装器从 CTAN 镜像下载软件包，也可以使用本地仓库。安装方案从最小（约 100MB）到完整（约 7GB）不等。安装完成后，可使用 **tlmgr**（TeX Live Manager）来更新和管理软件包。

# CAVEATS

完整安装需要数 GB 磁盘空间。网络安装依赖 CTAN 镜像的可用性。GUI 模式需要 Perl/Tk，默认可能未安装。TeX Live 每年发布新版本，通常需要每年重新安装而非原地升级。

# HISTORY

TeX Live 首次发布于 **1996 年**，是全球各 TeX 用户组合作的成果，旨在提供一致、跨平台的 TeX 发行版。install-tl 脚本随之演进，基于 Perl 的安装器在 **2008 年**前后成为标准。它取代了早期各平台专用的安装器，至今仍由 TeX Live 团队积极维护。

# SEE ALSO

[tlmgr](/man/tlmgr)(1), [pdflatex](/man/pdflatex)(1), [xelatex](/man/xelatex)(1), [lualatex](/man/lualatex)(1), [tex](/man/tex)(1)
