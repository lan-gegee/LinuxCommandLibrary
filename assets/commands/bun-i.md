# TAGLINE

安装软件包（bun install 的别名）

# TLDR

**安装 package.json 中的全部依赖**

```bun i```

**安装指定的包**

```bun i [package]```

将包**作为开发依赖安装**

```bun i -d [package]```

**安装指定版本**

```bun i [package]@[version]```

**全局安装包**

```bun i -g [package]```

**安装时不更新锁文件**

```bun i --frozen-lockfile```

# SYNOPSIS

**bun** **i** [_options_] [_packages..._]

# PARAMETERS

**-d**, **--dev**
> 作为开发依赖安装。

**-g**, **--global**
> 全局安装软件包。

**--frozen-lockfile**
> 不更新锁文件。

**--no-save**
> 不写入 package.json。

**--production**
> 不安装 devDependencies。

# DESCRIPTION

**bun i** 是 **bun install** 的别名。它根据 package.json 为项目安装依赖，或向项目添加新包。

Bun 的包管理器凭借原生实现和高效的缓存机制，速度显著快于 npm 或 yarn。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-install](/man/bun-install)(1), [bun-remove](/man/bun-remove)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
