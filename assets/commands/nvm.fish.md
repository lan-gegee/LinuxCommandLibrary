# TAGLINE

Fish shell 的 Node 版本管理器

# TLDR

**安装**指定的 Node.js **版本**

```nvm install [version]```

**安装最新的** **LTS** 版本

```nvm install lts```

**根据** **.nvmrc** 或 **.node-version** 文件安装版本

```nvm install```

**使用**已安装的特定版本

```nvm use [version]```

**列出已安装的**版本

```nvm list```

**列出所有可用的**远程版本

```nvm list-remote```

**为新 Shell 设置默认**版本

```set --universal nvm_default_version [version]```

**卸载**某个版本

```nvm uninstall [version]```

# SYNOPSIS

**nvm** [_command_] [_version_]

# PARAMETERS

**install** _VERSION_
> 安装 Node.js 版本。接受具体版本号（v18.4.0）、部分版本号（v18）或别名（latest、lts）。

**use** _VERSION_
> 在当前环境中激活已安装的 Node.js 版本。

**list**
> 列出已安装的 Node.js 版本，包括系统级 Node（如果存在）。

**list-remote**
> 显示镜像上所有可用的 Node.js 版本。

**current**
> 显示当前激活的 Node.js 版本。

**uninstall** _VERSION_
> 移除已安装的 Node.js 版本。

# CONFIGURATION

**$nvm_default_version**
> 新 Shell 会话的默认 Node.js 版本。通过 `set --universal nvm_default_version VERSION` 设置。

**$nvm_default_packages**
> 随每个新 Node.js 版本自动安装的软件包。通过 `set --universal nvm_default_packages yarn np` 设置。

**$nvm_data**
> Node.js 二进制文件的存储位置。默认为 `$XDG_DATA_HOME/nvm`（~/.local/share/nvm）。

**$nvm_mirror**
> Node.js 二进制文件的下载镜像。默认为 https://nodejs.org/dist。

# DESCRIPTION

**nvm.fish** 是由 **jorgebucaran** 开发的纯 Fish shell 实现的 Node 版本管理器。它提供了一种轻量级方式，可直接在 Fish shell 中安装、切换和管理多个 Node.js 版本。

与基于 bash 的原始 nvm 不同，nvm.fish 完全用 Fish 编写，没有任何外部依赖。它支持 **.nvmrc** 和 **.node-version** 文件以实现按项目自动切换版本，并符合 XDG Base Directory 规范。

通常通过 **Fisher** 安装（`fisher install jorgebucaran/nvm.fish`），或手动复制函数和补全脚本。

# CAVEATS

仅适用于 Fish shell，与 bash 版 nvm 及其配置不兼容。**nvm install** 命令只在当前环境中激活所安装的版本；如需跨会话保持，请使用 **$nvm_default_version**。需要 Fish 3.x 或更高版本。

# HISTORY

**nvm.fish** 由 **jorgebucaran** 于 **2016 年**创建，是 Node 版本管理器的原生 Fish shell 实现，灵感来自 creationix 和 ljharb 的原始 **nvm.sh**。

# SEE ALSO

[nvm](/man/nvm)(1), [fish](/man/fish)(1), [fnm](/man/fnm)(1), [node](/man/node)(1), [fisher](/man/fisher)(1)
