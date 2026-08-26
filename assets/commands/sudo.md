# TAGLINE

以提升的权限执行命令

# TLDR

**以 root 身份运行命令**

```sudo [command]```

**以其他用户身份运行命令**

```sudo -u [username] [command]```

**启动 root Shell**

```sudo -i```

**以其他用户身份启动 Shell**

```sudo -u [username] -s```

**保留环境变量运行命令**

```sudo -E [command]```

**以 root 身份编辑文件**（使用 sudoedit）

```sudo -e [/etc/hosts]```

**列出当前用户**允许执行的命令

```sudo -l```

**使缓存的凭据失效**

```sudo -k```

**在后台运行命令**

```sudo -b [command]```

# SYNOPSIS

**sudo** [_options_] [_command_]

**sudo** -u _user_ [_command_]

**sudo** -i | -s

# PARAMETERS

**-u** _USER_, **--user** _USER_
> 以指定用户身份运行命令（默认：root）

**-g** _GROUP_, **--group** _GROUP_
> 以指定的主组身份运行命令

**-i**, **--login**
> 以目标用户身份运行登录 Shell

**-s**, **--shell**
> 运行 Shell（取自 $SHELL 或用户默认值）

**-e**, **--edit**
> 编辑文件（sudoedit 模式）

**-E**, **--preserve-env**
> 保留用户的环境变量

**-H**, **--set-home**
> 将 HOME 设置为目标用户的主目录

**-b**, **--background**
> 在后台运行命令

**-l**, **--list**
> 列出用户允许执行的命令

**-v**, **--validate**
> 刷新凭据缓存而不运行命令

**-k**, **--reset-timestamp**
> 使缓存的凭据失效

**-K**, **--remove-timestamp**
> 彻底移除缓存的凭据

**-n**, **--non-interactive**
> 非交互模式；需要密码时直接失败

**-A**, **--askpass**
> 使用 askpass 辅助程序获取密码

**-S**, **--stdin**
> 从标准输入读取密码

**-p** _PROMPT_, **--prompt** _PROMPT_
> 自定义密码提示符

**-T** _TIMEOUT_
> 命令超时时间（秒）

**-V**, **--version**
> 显示版本信息

# DESCRIPTION

**sudo**（superuser do）以提升的权限执行命令，通常是以 root 身份。它基于 **/etc/sudoers** 中定义的规则提供对特权操作的可控访问，支持细粒度的权限管理。

认证成功后，sudo 会将凭据缓存一段宽限期（通常为 5 分钟），后续命令无需重新输入密码。使用 **-k** 可使该缓存失效。

**sudoers** 文件控制哪些用户可以在哪些主机上运行哪些命令。用户可以被授予完整的 root 权限，也可以被限制为只能执行特定命令。应使用 **visudo** 命令安全地编辑 sudoers 文件。

# CONFIGURATION

**/etc/sudoers**
> 定义哪些用户可以运行哪些命令的主策略文件。只能用 visudo 编辑。

**/etc/sudoers.d/**
> 用于存放模块化 sudo 策略文件的插入式目录。

**SUDO_EDITOR**
> 指定 sudoedit 所用编辑器的环境变量。

# CAVEATS

以 root 身份运行命令很危险——失误可能损坏系统。**-E** 选项可能暴露敏感的环境变量。出于安全考虑，某些环境变量默认会被过滤。sudoers 语法错误可能导致无法进行管理操作；请始终使用 **visudo** 进行编辑。避免在可能被不可信用户运行的脚本中使用 sudo。

# HISTORY

sudo 最初由 **Bob Coggeshall** 和 **Cliff Spencer** 于 **1980 年**前后在纽约州立大学布法罗分校编写。**Todd Miller** 于 **1994 年**接手维护工作并持续领导开发至今。这个名字通常被理解为 "superuser do"，但它最初代表 "substitute user do"，因为它能以任意用户身份运行命令。sudo 已成为类 Unix 系统上提权的标准方式，在大多数发行版中取代了直接以 root 登录的做法。

# INSTALL

```apt: sudo apt install sudo```

```dnf: sudo dnf install sudo```

```pacman: sudo pacman -S sudo```

```apk: sudo apk add doas-sudo-shim```

```zypper: sudo zypper install sudo```

```nix: nix profile install nixpkgs#sudo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[su](/man/su)(1), [visudo](/man/visudo)(8), [doas](/man/doas)(1)
