# TAGLINE

无需安装即可执行软件包

# TLDR

**运行包的二进制**而无需安装

```bun x [package]```

**运行指定版本**

```bun x [package]@[version]```

向命令**传递参数**

```bun x [package] -- [args...]```

**运行 create-* 脚手架包**

```bun x create-[template] [project-name]```

# SYNOPSIS

**bun** **x** [_options_] _package_ [_args..._]

# DESCRIPTION

**bun x** 在不永久安装的情况下运行包的二进制文件。它与 **npx** 类似，但凭借 Bun 的缓存与原生实现速度显著更快。

如果包已在本地或全局安装，则直接使用该版本；否则临时下载并缓存该包。

独立命令 **bunx**（随 **bun** 一起安装）等价于 **bun x**。

常见用例包括运行脚手架工具（create-react-app、create-next-app）、一次性小工具，以及在决定安装前试用包。

# CAVEATS

包会被缓存，但可能在缓存清理时被移除。对于常用工具，建议用 **bun i -g** 全局安装。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-run](/man/bun-run)(1), [npx](/man/npx)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
