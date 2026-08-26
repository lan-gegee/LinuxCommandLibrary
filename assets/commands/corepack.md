# TAGLINE

Node.js 软件包管理器的管理器

# TLDR

**启用 Corepack**

```corepack enable```

**禁用 Corepack**

```corepack disable```

**准备特定版本的软件包管理器**

```corepack prepare [yarn@4.0.0] --activate```

**将软件包管理器写入 package.json**

```corepack use [pnpm@9.x]```

**从已下载的归档安装**

```corepack hydrate [./corepack.tgz]```

**打包软件包管理器供离线使用**

```corepack pack [yarn@4.0.0]```

# SYNOPSIS

**corepack** _command_ [_arguments_]

# DESCRIPTION

**corepack** 是 Node.js 的软件包管理器管理器。它依据 package.json 中的 "packageManager" 字段，按项目透明地管理 Yarn、npm 和 pnpm 的版本。这样能确保每个项目都使用自己指定的软件包管理器版本，无需全局安装或手动切换版本。

Corepack 随 Node.js 从 14.19.0 到 24.x 版本一同提供，它充当一个 shim，拦截软件包管理器命令，并自动下载、使用项目配置中指定的正确版本。这消除了开发团队因软件包管理器版本不匹配导致的"在我机器上能跑"问题。

该工具在本地维护软件包管理器版本的缓存，并可使用打包归档以离线模式运行。零运行时依赖使其轻量可靠，适合 CI/CD 环境。

# COMMANDS

**enable**
> 在 PATH 中安装软件包管理器的 shim

**disable**
> 移除 shim，恢复直接访问

**prepare**
> 下载并缓存软件包管理器版本

**use**
> 在 package.json 中写入 packageManager 字段

**hydrate**
> 从归档安装软件包管理器

**pack**
> 创建用于离线安装的归档

# PARAMETERS

**--activate**
> 准备完成后设为默认版本

# PACKAGE.JSON INTEGRATION

```json
{
  "packageManager": "pnpm@9.0.0"
}
```

Corepack 会读取该字段并确保使用正确的版本。

# ENVIRONMENT

**COREPACK_HOME**
> 软件包管理器的缓存目录

**COREPACK_ENABLE_DOWNLOAD_PROMPT**
> 下载前进行提示

**COREPACK_ENV_FILE**
> 自定义 env 文件路径（设为 0 可禁用）

# OFFLINE USAGE

```
corepack pack yarn@4.0.0           # Create archive
corepack hydrate ./yarn.tgz        # Install from archive
```

# CAVEATS

使用前必须先启用。遵循最近的 package.json 中的 packageManager 字段。零运行时依赖。

# INSTALL

```pacman: sudo pacman -S corepack```

```brew: brew install corepack```

```nix: nix profile install nixpkgs#corepack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/nodejs/corepack)```

<!-- verified: 2026-06-23 -->
