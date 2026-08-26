# TAGLINE

管理你应用的 Node.js 环境

# TLDR

**列出所有可安装的 Node.js 版本**

```nodenv install --list```

**安装特定 Node.js 版本**

```nodenv install [18.17.0]```

**设置全局默认的 Node.js 版本**

```nodenv global [18.17.0]```

**设置某个应用本地的 Node.js 版本**

```nodenv local [16.20.0]```

**显示当前生效的 Node.js 版本**

```nodenv version```

**列出所有已安装的 Node.js 版本**

```nodenv versions```

**卸载特定的 Node.js 版本**

```nodenv uninstall [16.20.0]```

**安装 npm 包后重建 shim 可执行文件**

```nodenv rehash```

# SYNOPSIS

**nodenv** _command_ [_options_] [_arguments_]

# PARAMETERS

**install** _VERSION_
> 安装 Node 版本。

**uninstall** _VERSION_
> 卸载 Node 版本。

**versions**
> 列出已安装的版本。

**version**
> 显示当前版本。

**global** [_VERSION_]
> 设置/显示全局版本。

**local** [_VERSION_]
> 设置/显示本地版本。

**shell** [_VERSION_]
> 设置当前 Shell 的版本。

**rehash**
> 重建 shim 可执行文件。

**which** _COMMAND_
> 显示命令对应的路径。

**whence** _COMMAND_
> 列出包含该命令的所有版本。

**root**
> 显示 nodenv 根目录。

**init**
> Shell 初始化。

**install --list**
> 列出可用版本。

**install --list-all**
> 列出包括旧版在内的所有版本。

# DESCRIPTION

**nodenv** 按项目管理多个 Node.js 版本。在将自己注入 PATH 之后，任何对 `node`、`npm`、`npx` 或其他 Node.js 可执行文件的调用都会先激活 nodenv，它使用 shim 拦截命令并将其路由到正确的版本。

版本选择采用层次结构：NODENV_VERSION 环境变量优先，其次是当前目录及父目录中的 `.node-version` 文件，最后是全局版本设置。这样无需手动切换即可实现项目专属的版本。

`nodenv install` 命令由 **node-build** 插件提供，大多数安装方式（例如 Homebrew）默认包含它。它会下载预编译的二进制文件或从源码编译 Node.js。

shim 是位于 `~/.nodenv/shims/` 的轻量可执行文件，它们在执行前确定正确的 Node 版本。安装带可执行文件的 npm 包之后，运行 `nodenv rehash` 为其创建 shim。

项目根目录中的 `.node-version` 文件指定 Node 版本。当你进入该目录时，nodenv 会自动使用那个版本。

# CAVEATS

需要在 profile 中初始化 Shell（在 .bashrc/.zshrc 中加入 `eval "$(nodenv init -)"`）。新安装的全局包需要 `nodenv rehash`。从源码构建耗时且需要构建依赖。与 nvm 不兼容。Shim 会给命令启动带来少量开销。

# HISTORY

**nodenv** 由 **Will Farrington** 和 **Jason Karns** 于 **2014 年**前后创建，仿照 Ruby 的 rbenv 设计。它将 rbenv 经过验证的版本管理模式带到了 Node.js。插件架构在保持核心简洁的同时支持自定义。

# INSTALL

```brew: brew install nodenv```

```nix: nix profile install nixpkgs#nodenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvm](/man/nvm)(1), [fnm](/man/fnm)(1), [volta](/man/volta)(1), [asdf](/man/asdf)(1), [rbenv](/man/rbenv)(1)
