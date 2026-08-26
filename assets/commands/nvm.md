# TAGLINE

Node 版本管理器

# TLDR

**安装 Node.js 版本**

```nvm install [version]```

**安装最新 LTS**

```nvm install --lts```

**使用特定版本**

```nvm use [version]```

**列出已安装的版本**

```nvm ls```

**列出可用版本**

```nvm ls-remote```

**设置默认版本**

```nvm alias default [version]```

# SYNOPSIS

**nvm** [_command_] [_options_]

# PARAMETERS

**install** _VERSION_
> 安装 Node.js 版本。

**use** _VERSION_
> 切换到指定版本。

**ls**
> 列出已安装的版本。

**ls-remote**
> 列出可用版本。

**alias** _NAME_ _VERSION_
> 创建版本别名。

**uninstall** _VERSION_
> 移除版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nvm** 即 Node 版本管理器。管理多个 Node.js 安装。

该工具支持按项目切换版本。基于 Shell 进行版本管理。

# CAVEATS

它是 shell 函数而非可执行文件。需在配置文件中 source。每个 shell 都需单独激活。

# HISTORY

nvm 的诞生是为了让开发者能够**轻松切换** Node.js 版本。

# INSTALL

```pacman: sudo pacman -S nvm```

```brew: brew install nvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [fnm](/man/fnm)(1), [n](/man/n)(1)
