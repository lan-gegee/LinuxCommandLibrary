# TAGLINE

JavaScript 工具链版本管理器

# TLDR

**安装 Node 版本**

```volta install node@[18]```

**安装指定版本**

```volta install node@[18.17.0]```

**安装 npm 版本**

```volta install npm@[9]```

**安装 yarn**

```volta install yarn```

**为项目固定 Node 版本**

```volta pin node@[18]```

**列出已安装的工具**

```volta list```

**显示当前版本**

```volta which node```

**只下载不安装**

```volta fetch node@[20]```

# SYNOPSIS

**volta** [_install_] [_pin_] [_list_] [_fetch_] [_options_] [_tool_[@_version_]]

# PARAMETERS

**install** _TOOL_
> 安装工具。

**pin** _TOOL_
> 为项目固定工具版本。

**uninstall** _TOOL_
> 移除工具。

**list** [_all_]
> 列出已安装的工具。

**fetch** _TOOL_
> 只下载，不安装。

**run** _TOOL_
> 运行工具。

**which** _TOOL_
> 显示工具路径。

**setup**
> 配置 Shell。

**--quiet**
> 不输出信息。

**--verbose**
> 详细输出。

**--version**
> 显示版本。

# DESCRIPTION

**volta** 管理 JavaScript 工具的版本。它以快速、可靠的方式处理 Node.js、npm 和 Yarn 的切换。

固定的版本配置存储在 package.json 中。进入项目目录时，Volta 会自动使用固定的版本。

安装速度很快。Volta 下载预编译的二进制文件并加以缓存。版本切换是即时的。

垫片（shim）系统会拦截 node、npm 和 npx 命令，并根据项目配置路由到正确的版本。

全局软件包在不同 Node 版本之间也能正常工作。Volta 将它们与 Node 安装分开管理。

完成 setup 之后无需任何额外配置。版本切换会根据项目需求透明地进行。

# CAVEATS

需要进行 Shell 设置。仅限于 Node.js 生态系统。全局软件包存在一些边缘情况。比 nvm/fnm 更新。

# HISTORY

**Volta** 由 **LinkedIn** 于 **2019 年**前后创建。它使用 Rust 编写，强调管理 JavaScript 工具链时的速度和可靠性。

# INSTALL

```brew: brew install volta```

```nix: nix profile install nixpkgs#volta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [nvm](/man/nvm)(1), [fnm](/man/fnm)(1)
