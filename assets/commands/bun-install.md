# TAGLINE

安装项目依赖

# TLDR

**安装全部依赖**

```bun install```

**添加依赖**

```bun add [package]```

**添加开发依赖**

```bun add -d [package]```

**以精确版本添加**

```bun add --exact [package]```

**移除依赖**

```bun remove [package]```

**安装时不运行生命周期脚本**

```bun install --ignore-scripts```

**仅为生产环境安装**

```bun install --production```

# SYNOPSIS

**bun install** [_options_]

**bun add** [_options_] _package_ ...

**bun remove** _package_ ...

# DESCRIPTION

**bun install** 是 Bun 内置的包管理器，是 npm、yarn 和 pnpm 的快速替代品。它将 package.json 中的依赖安装到与 Node.js 兼容的 node_modules 文件夹中。

该包管理器使用全局缓存避免重复下载软件包，并采用系统上最快的文件写入系统调用。

# PARAMETERS

**-d, --dev**
> 作为开发依赖添加

**--exact**
> 将包版本固定为精确版本

**--production**
> 只安装生产依赖

**--ignore-scripts**
> 跳过运行生命周期脚本

**--frozen-lockfile**
> 若锁文件需要更新则报错

**--force**
> 强制重新下载所有包

**--global**
> 全局安装软件包

# LOCKFILE

自 v1.2 起，Bun 默认使用 **bun.lock**（文本格式）作为锁文件。首次安装前请删除其他锁文件（package-lock.json、yarn.lock、pnpm-lock.yaml），以免产生冲突。

# TRUSTED DEPENDENCIES

出于安全考虑，Bun 默认不运行依赖的生命周期脚本。可通过 package.json 中的 **trustedDependencies** 为可信包设置白名单。

# CAVEATS

与现有的 package.json 文件兼容。支持 workspaces、git/http/tarball 依赖以及自定义 registry。某些 npm 特有功能的行为可能有所不同。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-add](/man/bun-add)(1), [bun-remove](/man/bun-remove)(1), [npm](/man/npm)(1), [yarn](/man/yarn)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
