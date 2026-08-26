# TAGLINE

为本地开发创建包的符号链接

# TLDR

**将当前包注册**为全局链接的包

```bun link```

**将全局注册的包链接**到当前项目

```bun link [package-name]```

# SYNOPSIS

**bun** **link** [_package-name_]

# DESCRIPTION

**bun link** 为本地包开发创建符号链接。工作流分为两步：

1. 在包目录中运行 **bun link**（不带参数），将其注册为全局可用的链接包。
2. 在使用该包的项目中运行 **bun link [package-name]**，创建从 node_modules 指向已注册包的符号链接。

这适用于开发和测试本地包而无需发布到 registry。对源包的修改会立即反映在所有链接它的项目中。

# CAVEATS

如果被链接的包需要构建步骤，则必须在链接前完成构建。对被链接包的修改会立即反映在使用它的项目中。这种链接是 Bun 包管理器特有的，与 npm 或 yarn 的 link 注册不互通。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-unlink](/man/bun-unlink)(1), [bun-install](/man/bun-install)(1), [npm-link](/man/npm-link)(1)
