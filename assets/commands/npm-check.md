# TAGLINE

检查过时和未使用的软件包

# TLDR

**检查更新**

```npm-check```

**交互式更新**

```npm-check -u```

**检查全局安装的软件包**

```npm-check -g```

**跳过未使用检查**

```npm-check --skip-unused```

**全部更新**

```npm-check -y```

**仅检查生产依赖**

```npm-check --production```

# SYNOPSIS

**npm-check** [_options_]

# PARAMETERS

**-u**
> 交互式更新模式。

**-g**
> 检查全局软件包。

**--skip-unused**
> 跳过未使用软件包检查。

**-y**
> 无需提示直接更新全部。

**--production**
> 仅生产依赖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm-check** 检查过时和未使用的软件包，并提供交互式更新。

该工具会显示可用的更新，并识别未被使用的依赖。

# CAVEATS

第三方工具。使用 npm install -g 安装。提供交互式 TUI。

# HISTORY

npm-check 的创建目的是提供**交互式的软件包更新**和未使用依赖检测。

# INSTALL

```nix: nix profile install nixpkgs#npm-check```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-outdated](/man/npm-outdated)(1), [ncu](/man/ncu)(1)
