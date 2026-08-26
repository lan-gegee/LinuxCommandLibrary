# TAGLINE

执行软件包的二进制程序

# TLDR

**运行包的二进制程序**，若不存在则自动安装

```bun exec [package]```

**运行指定版本**的包二进制程序

```bun exec [package]@[version]```

**强制使用 Bun 运行时执行**，而非 Node.js

```bun exec --bun [package]```

**当二进制名与包名不同时指定包**

```bun exec -p [package] [binary] [args...]```

**在包不可用时直接运行而不安装**

```bun exec --no-install [binary]```

# SYNOPSIS

**bun** **exec** [_options_] _package_[@_version_] [_args..._]

# DESCRIPTION

**bun exec** 自动安装并运行来自 npm 的包二进制程序。它是 **bun x** 和 **bunx** 的别名，相当于 Bun 版的 **npx**。

如果包的二进制程序存在于本地的 **node_modules/.bin**，则使用该版本。否则，该包会被下载到全局共享缓存中并从那里执行。

默认情况下，Bun 会尊重可执行文件中的 **#!/usr/bin/env node** shebang，用 Node.js 运行它们。使用 **--bun** 可以覆盖这一行为，改用 Bun 的运行时。

# PARAMETERS

**--bun**
> 强制可执行文件使用 Bun 运行时而非 Node.js 运行，即使它带有 Node shebang。必须放在包名之前。

**-p**, **--package** _name_
> 当二进制名与包名不同时，指定要安装的包。

**--no-install**
> 不自动安装包；若其不可用则报错退出。

**--silent**
> 抑制安装过程的输出。

**--verbose**
> 安装过程中启用详细输出。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-x](/man/bun-x)(1), [bun-run](/man/bun-run)(1), [npx](/man/npx)(1)
