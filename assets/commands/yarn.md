# TAGLINE

快速可靠的 JavaScript 依赖管理器

# TLDR

从 package.json **安装所有依赖**

```yarn install```

**添加软件包**到依赖中

```yarn add [package]```

**将软件包**添加为开发依赖

```yarn add --dev [package]```

**移除一个软件包**

```yarn remove [package]```

**升级软件包**到最新版本

```yarn upgrade```

**运行** package.json 中定义的**脚本**

```yarn run [script]```

**初始化新项目**

```yarn init```

交互式**升级**软件包

```yarn upgrade-interactive```

# SYNOPSIS

**yarn** [_command_] [_flags_]

# PARAMETERS

**install**
> 从 package.json 安装所有依赖。

**add** _package_
> 将软件包添加为项目依赖。

**remove** _package_
> 从项目中移除软件包。

**upgrade** [_package_]
> 根据版本范围将软件包升级到最新的允许版本。

**run** _script_
> 执行 package.json 中定义的脚本。

**init**
> 初始化新项目，创建 package.json。

**publish**
> 将软件包发布到 registry。

**create** _starter-kit_
> 使用入门套件创建新项目。

**config**
> 管理 Yarn 配置项。

**cache clean**
> 清理全局缓存。

**--dev**, **-D**
> 将软件包添加为开发依赖。

**--global**, **-g**
> 全局安装软件包。

**--verbose**
> 为命令打印详细输出。

**--cwd** _directory_
> 指定工作目录。

**--mutex** _type_
> 确保只有一个 Yarn 实例在运行（file 或 network）。

**--help**
> 显示命令的帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**Yarn** 是一款快速、可靠且安全的 JavaScript 依赖管理器。它会缓存下载过的每个软件包，支持离线安装之前获取过的包。与 npm 相比，Yarn 通过并行操作获得更快的性能。

不带命令运行 **yarn** 相当于执行 **yarn install**。运行 **yarn script** 会执行 package.json 中用户定义的脚本。锁文件 **yarn.lock** 确保各台机器上的安装结果一致。

Yarn 2+（Berry）引入了 Plug'n'Play 以支持零安装工作流，并改进了对 workspace 的支持。配置可以全局设置，也可以通过 **.yarnrc.yml** 按项目设置。

# CAVEATS

存在两个主要版本：Yarn Classic（1.x）和 Yarn Modern（2+/Berry），二者的特性和配置不同。Yarn Modern 默认使用 Plug'n'Play，可能需要调整项目配置。全局安装位置与 npm 不同。

# HISTORY

Yarn 由 **Facebook**（现 Meta）与 Exponent、Google 和 Tilde 合作开发，于 **2016 年 10 月**发布，作为 npm 的替代品。它解决了当时 npm 在性能和安全方面的问题。Yarn 2（Berry）是一次完全重写，于 **2020 年 1 月**发布，带来了 Plug'n'Play 和改进的 workspaces 等特性。如今 Yarn 是一个社区驱动的项目。

# INSTALL

```pacman: sudo pacman -S yarn```

```apk: sudo apk add yarn```

```zypper: sudo zypper install yarn```

```brew: brew install yarn```

```nix: nix profile install nixpkgs#yarn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [pnpm](/man/pnpm)(1), [node](/man/node)(1), [npx](/man/npx)(1)
