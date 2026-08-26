# TAGLINE

快速且节省磁盘空间的 Node.js 软件包管理器

# TLDR

**安装依赖**

```pnpm install```

**添加软件包**

```pnpm add [package]```

**添加开发依赖**

```pnpm add -D [package]```

**运行脚本**

```pnpm run [script]```

**更新软件包**

```pnpm update```

**移除软件包**

```pnpm remove [package]```

# SYNOPSIS

**pnpm** [_command_] [_options_]

# PARAMETERS

**install**
> 安装所有依赖。

**add** _PACKAGE_
> 添加软件包。

**-D**, **--save-dev**
> 保存为开发依赖。

**remove** _PACKAGE_
> 移除软件包。

**update**
> 更新软件包。

**run** _SCRIPT_
> 运行脚本。

**exec** _CMD_
> 执行命令。

**-r**, **--recursive**
> 在所有工作区中运行。

# DESCRIPTION

**pnpm** 是一个快速且节省磁盘空间的 Node.js 软件包管理器，它采用基于内容的寻址存储系统。pnpm 不会把软件包复制到每个项目的 node_modules 中，而是从一个全局存储创建硬链接，当多个项目共享相同依赖时可大幅减少磁盘占用。

它提供严格的 node_modules 结构，阻止访问未声明的依赖，从而提高项目的可靠性。该命令行界面与 npm 高度兼容，支持语法相近的 **install**、**add**、**remove**、**update** 和 **run** 命令。通过 **-r**（递归）提供的工作区支持可以管理 monorepo 项目。

# CONFIGURATION

**.npmrc**
> 项目级或用户级配置文件，用于设置 registry 地址、身份验证令牌以及 `store-dir` 和 `strict-peer-dependencies` 等 pnpm 特有配置。

**~/.local/share/pnpm/store/**（Linux）、**~/Library/pnpm/store/**（macOS）
> 所有项目共享的基于内容寻址的软件包存储。

**pnpm-workspace.yaml**
> 为 monorepo 场景定义工作区软件包。

# CAVEATS

需要 Node.js。使用硬链接以提高效率。

# HISTORY

pnpm 作为 npm 的**快速替代方案**而创建，磁盘占用更少。

# INSTALL

```dnf: sudo dnf install pnpm```

```pacman: sudo pacman -S pnpm```

```apk: sudo apk add pnpm```

```zypper: sudo zypper install pnpm```

```brew: brew install pnpm```

```nix: nix profile install nixpkgs#pnpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [node](/man/node)(1)
