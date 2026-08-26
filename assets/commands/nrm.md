# TAGLINE

npm registry 管理器

# TLDR

**列出 registry**

```nrm ls```

**使用某个 registry**

```nrm use [taobao]```

**添加自定义 registry**

```nrm add [name] [url]```

**删除 registry**

```nrm del [name]```

**测试 registry 速度**

```nrm test```

**显示当前 registry**

```nrm current```

# SYNOPSIS

**nrm** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> nrm 子命令。

**ls**
> 列出 registry。

**use** _NAME_
> 切换 registry。

**add** _NAME_ _URL_
> 添加 registry。

**del** _NAME_
> 移除 registry。

**test**
> 测试各 registry 速度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nrm** 是 npm registry 管理器，可在多个 npm registry 之间快速切换。

该工具管理 registry 的 URL，并预置了常用的 registry。

# CAVEATS

Node.js 工具。使用 npm install -g 安装。会修改 .npmrc。

# HISTORY

nrm 的创建目的是在不同 npm registry 之间**轻松切换**。

# INSTALL

```brew: brew install nrm```

```nix: nix profile install nixpkgs#nrm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-config](/man/npm-config)(1), [yarn](/man/yarn)(1)
