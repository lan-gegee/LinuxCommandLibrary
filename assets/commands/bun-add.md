# TAGLINE

向 Bun 项目添加软件包

# TLDR

**添加依赖**

```bun add [lodash]```

**添加开发依赖**

```bun add -D [jest]```

**添加多个包**

```bun add [react] [react-dom]```

**以精确版本添加**

```bun add --exact [typescript@5.0.0]```

**全局安装**

```bun add -g [typescript]```

**从 git 仓库添加**

```bun add git+https://github.com/[user]/[repo]```

**作为 peer 依赖添加**

```bun add -P [react]```

**试运行，不实际修改**

```bun add --dry-run [package]```

# SYNOPSIS

**bun add** [_options_] _package_ ...

# DESCRIPTION

**bun add** 将软件包添加到 package.json 并安装到 node_modules。它会更新或创建 bun.lockb，以保证安装可复现。该命令比 npm 或 yarn 的同类命令快得多。

# PARAMETERS

**-D, --dev**
> 添加到 devDependencies

**-P, --peer**
> 添加到 peerDependencies

**-O, --optional**
> 添加到 optionalDependencies

**-E, --exact**
> 使用精确版本，不加 ^ 或 ~ 前缀

**-g, --global**
> 全局安装到 Bun 的全局存储

**--production**
> 跳过 devDependencies

**--registry** _url_
> 使用自定义 npm registry

**--lockfile-only**
> 只更新锁文件而不安装

**--dry-run**
> 模拟执行但不做实际修改

**--force**
> 忽略警告强制安装

**--trust**
> 允许所添加的包运行生命周期脚本

# PACKAGE SOURCES

支持 npm registry 包、semver 版本范围、git URL（git+https://...）、本地路径（file:../path）以及工作区包（workspace:*）。

# CAVEATS

会创建二进制的 bun.lockb 锁文件（新版本中为文本格式的 bun.lock）。除非指定 --exact，包版本默认采用插入符（^）范围。全局安装的包存放在 Bun 的全局存储中，而非系统级目录。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-install](/man/bun-install)(1), [bun-remove](/man/bun-remove)(1), [npm-install](/man/npm-install)(1), [yarn](/man/yarn)(1)
