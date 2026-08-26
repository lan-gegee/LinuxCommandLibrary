# TAGLINE

自动安装并运行软件包可执行文件

# TLDR

**运行软件包可执行文件**

```bunx [prisma] migrate```

**运行特定版本的软件包**

```bunx [email protected] [app.js]```

**在二进制名与包名不同的情况下运行**

```bunx -p @angular/cli ng new [my-app]```

**强制使用 Bun 运行时运行**

```bunx --bun vite dev```

**对文件运行 prettier**

```bunx prettier [file.js]```

**运行 create-react-app**

```bunx create-react-app [my-app]```

# SYNOPSIS

**bunx** [_options_] _package_ [_arguments_]

# DESCRIPTION

**bunx** 自动安装并运行来自 npm 软件包的可执行文件。它相当于 Bun 版的 npx，得益于 Bun 快速的启动速度，对本地已安装的软件包大约快 100 倍。

在本地 node_modules 中找不到的软件包会被自动安装到全局共享缓存中。

# PARAMETERS

**-p**, **--package** _name_
> 当二进制名与包名不同时，指定要安装的软件包。

**--bun**
> 即使可执行文件带有 Node shebang，也强制使用 Bun 运行。

**--no-install**
> 当软件包尚未缓存时直接失败，而不是去获取。

**--silent**
> 抑制与安装相关的输出。

**--verbose**
> 在安装期间打印更多细节。

# BEHAVIOR

默认情况下，bunx 会遵循脚本中的 **#!/usr/bin/env node** shebang。使用 **--bun** 可覆盖此行为并以 Bun 运行时运行。

# WINDOWS

在 Windows 上，bunx 使用特殊的 **.bunx** 文件格式来实现跨文件系统的符号链接，可同时兼容 Bun 和 Node.js。

# CAVEATS

软件包在首次使用后会被全局缓存。当你确实需要 Bun 运行时特性时，请使用 **--bun** 标志。某些软件包可能依赖 Node.js 特有的 API。

# SEE ALSO

[bun](/man/bun)(1), [bun-run](/man/bun-run)(1), [npx](/man/npx)(1)
