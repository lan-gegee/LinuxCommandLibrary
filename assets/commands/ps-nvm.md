# TAGLINE

PowerShell 的 Node.js 版本管理器

# TLDR

**列出 Node 版本**（PowerShell）

```ps-nvm list```

**安装 Node 版本**

```ps-nvm install [18.0.0]```

**使用特定版本**

```ps-nvm use [18.0.0]```

**设置默认版本**

```ps-nvm default [18.0.0]```

# SYNOPSIS

**ps-nvm** _command_ [_version_]

# PARAMETERS

**list**
> 列出已安装的版本。

**install** _VERSION_
> 安装 Node 版本。

**use** _VERSION_
> 切换到指定版本。

**default** _VERSION_
> 设置默认版本。

**uninstall** _VERSION_
> 移除版本。

# DESCRIPTION

**ps-nvm** 是一个专为 Windows 上 PowerShell 原生设计的 Node.js 版本管理器。它允许在同一系统上安装、切换和管理多个 Node.js 版本，类似于 Unix 上的 nvm，但专为 PowerShell 环境构建。

该工具下载并管理 Node.js 二进制文件，通过调整系统 PATH 指向所选版本。可以设置默认版本，使其在新的 PowerShell 会话中保持生效。

# CAVEATS

仅支持 PowerShell；是 nvm 在 Windows 上的专用替代品。以 PowerShell 模块形式安装。部分操作需要管理员权限。

# HISTORY

ps-nvm 为 **PowerShell** 环境的 Node.js 版本管理而创建。

# SEE ALSO

[nvm](/man/nvm)(1), [node](/man/node)(1), [volta](/man/volta)(1)
