# TAGLINE

node Package Manager

# TLDR

**安装依赖**

```npm install```

**安装软件包**

```npm install [package]```

**全局安装**

```npm install -g [package]```

**安装开发依赖**

```npm install -D [package]```

**运行脚本**

```npm run [script-name]```

**启动应用**

```npm start```

**运行测试**

```npm test```

**更新软件包**

```npm update```

**初始化项目**

```npm init```

**根据 lockfile 干净安装**

```npm ci```

**列出已安装的软件包**

```npm ls```

**检查过时的软件包**

```npm outdated```

**运行安全审计**

```npm audit```

**卸载软件包**

```npm uninstall [package]```

**发布软件包**

```npm publish```

# SYNOPSIS

**npm** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> npm 子命令。

**install**
> 安装软件包。

**uninstall**
> 移除软件包。

**run** _SCRIPT_
> 运行软件包脚本。

**update**
> 更新软件包。

**init**
> 创建 package.json。

**ci**
> 从 package-lock.json 干净安装（用于 CI/CD）。

**audit**
> 运行安全漏洞审计。

**ls**
> 列出已安装的软件包。

**outdated**
> 检查过时的软件包。

**publish**
> 将软件包发布到 registry。

**-g**
> 全局安装。

**-D**, **--save-dev**
> 保存为开发依赖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm** 即 Node Package Manager，是 Node.js 的默认包管理器。它通过 package.json 和 package-lock.json 文件管理 JavaScript 软件包及依赖。

npm 连接着世界上最大的软件 registry，拥有超过两百万个软件包。

# CAVEATS

需要 Node.js。依赖 package-lock.json 保证确定性。依赖网络。

# HISTORY

npm 由 **Isaac Schlueter** 于 2010 年创建，是 Node.js 的默认包管理器。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npx](/man/npx)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1)
