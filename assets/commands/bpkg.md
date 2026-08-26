# TAGLINE

bash 脚本包管理器。

# TLDR

全局**安装软件包**

```bpkg install [package-name] -g```

**安装指定版本**

```bpkg install [package-name]@[version]```

本地**安装软件包**（安装到 ./deps/）

```bpkg install [package-name]```

从 bpkg.json **安装依赖**

```bpkg getdeps```

**运行软件包脚本**

```bpkg run [script-name]```

**带参数运行脚本**

```bpkg run [script-name] "[arg1]" "[arg2]"```

**列出可用脚本**

```bpkg run --list```

**获取软件包信息**

```bpkg package```

# SYNOPSIS

**bpkg** [_-hV_] _command_ [_arguments_]

# DESCRIPTION

**bpkg** 是一个轻量级的 bash 包管理器，用于从 GitHub 仓库获取和安装 Shell 脚本。它负责下载、设置权限和组织脚本，既可以全局安装，也可以按项目安装。

软件包通过 **bpkg.json** 文件配置，其中定义了元数据、依赖和可执行脚本。该工具的工作方式类似 Node.js 的 npm 或 Python 的 pip。

# SUBCOMMANDS

**install**
> 安装软件包（加 -g 全局安装，不加则本地安装）。

**getdeps**
> 安装 bpkg.json 中定义的依赖。

**run**
> 执行软件包中定义的脚本。

**package**
> 显示软件包元数据。

**update**
> 更新本地可用软件包的索引。

**source**
> 将软件包的 bash 文件 source 到当前 Shell 中。

**init**
> 以交互方式创建 bpkg.json 文件。

**json**
> 解析和查询 JSON（内部使用）。

**show**
> 显示软件包 readme 或索引中的详情。

**list**
> 列出本地索引中可用的软件包。

**term**
> 终端实用工具。

# PARAMETERS

**-g, --global**
> 全局安装软件包到 ${PREFIX:-/usr/local/bin}。

**-d, --dev**
> 同时安装开发依赖。

**-l, --list**
> 列出可用命令（与 run 配合使用）。

**-h, --help**
> 显示帮助消息。

**-V, --version**
> 显示版本信息。

**@version**
> 指定软件包版本（如 package@1.0.0）。

# CAVEATS

软件包必须包含有效的 **bpkg.json** 或 **package.json** 文件。全局安装需要对目标目录有相应的写权限。依赖会递归安装在 deps/ 子目录中。

# HISTORY

bpkg 是专为 bash 脚本设计的简单包管理器，灵感来自 npm 等包管理器。它提供了一种标准化的方式，便于在多个项目之间共享和复用 Shell 脚本工具。

# INSTALL

```dnf: sudo dnf install bpkg```

```nix: nix profile install nixpkgs#bpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [npm](/man/npm)(1), [basher](/man/basher)(1)

# RESOURCES

```[Source code](https://github.com/bpkg/bpkg)```

```[Homepage](https://bpkg.sh)```

<!-- verified: 2026-06-19 -->
