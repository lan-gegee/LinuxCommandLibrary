# TAGLINE

列出过时的 pnpm 软件包

# TLDR

**检查过时的软件包**

```pnpm outdated```

**检查特定软件包**

```pnpm outdated [package-name]```

**仅检查生产依赖**

```pnpm outdated --prod```

**检查开发依赖**

```pnpm outdated --dev```

**检查全局安装的软件包**

```pnpm outdated -g```

**长格式输出**

```pnpm outdated --long```

# SYNOPSIS

**pnpm outdated** [_--prod_] [_--dev_] [_-g_] [_packages_]

# PARAMETERS

**--prod**
> 仅生产依赖。

**--dev**
> 仅开发依赖。

**-g**, **--global**
> 全局软件包。

**--long**
> 显示扩展信息。

**-r**, **--recursive**
> 检查工作区中的所有软件包。

**--filter** _PATTERN_
> 过滤工作区中的软件包。

**--no-table**
> 以列表形式输出过时的依赖。

**--compatible**
> 仅显示满足 package.json 中 semver 范围的版本。

# DESCRIPTION

**pnpm outdated** 通过将已安装版本与 registry 上的版本进行比较，检查是否有更新版本可用的软件包。它会显示一个表格，列出每个过时软件包的当前版本、期望版本（符合 semver 范围）和最新版本。

输出使用颜色区分主版本升级（红色）和次版本升级（黄色）。使用 **--prod** 或 **--dev** 按依赖类型过滤，使用 **-g** 检查全局软件包，在 monorepo 中使用 **-r** 检查所有工作区软件包。**--long** 标志会显示包括软件包主页在内的额外详情。

# CAVEATS

需要 pnpm。需要网络访问。可能显示不想要的主版本更新。

# HISTORY

**pnpm outdated** 是 **pnpm** 的一部分，pnpm 是一个快速且节省磁盘空间的软件包管理器，作为 npm 的替代方案而创建。

# INSTALL

```dnf: sudo dnf install pnpm```

```pacman: sudo pacman -S pnpm```

```apk: sudo apk add pnpm```

```zypper: sudo zypper install pnpm```

```brew: brew install pnpm```

```nix: nix profile install nixpkgs#pnpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnpm](/man/pnpm)(1), [npm-outdated](/man/npm-outdated)(1), [yarn](/man/yarn)(1)
