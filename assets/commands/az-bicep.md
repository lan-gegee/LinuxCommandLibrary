# TAGLINE

管理用于 Azure 基础设施即代码的 Bicep 文件

# TLDR

**将 Bicep 文件构建**为 ARM 模板

```az bicep build --file [main.bicep]```

将 ARM 模板**反编译**为 Bicep

```az bicep decompile --file [template.json]```

**格式化 Bicep 文件**

```az bicep format --file [main.bicep]```

对 Bicep 文件进行**检查**以发现错误

```az bicep lint --file [main.bicep]```

从 Bicep **生成参数文件**

```az bicep generate-params --file [main.bicep]```

**安装 Bicep CLI**

```az bicep install```

```az bicep upgrade```

**升级 Bicep** 到最新版本

```az bicep publish --file [main.bicep] --target "br:[registry.azurecr.io/bicep/modules/name:v1]"```

# SYNOPSIS

**az bicep** _subcommand_ [_options_]

# DESCRIPTION

**az bicep** 管理 Azure 上基础设施即代码所需的 Bicep CLI。Bicep 是一种领域特定语言（DSL），使用声明式语法部署 Azure 资源，是 ARM 模板的透明抽象。

该命令组提供构建、验证、格式化和发布 Bicep 文件的工具，并可将现有 ARM 模板转换为 Bicep 格式。需要 Azure CLI 2.20.0 或更高版本；如果不存在，Bicep CLI 会在首次使用时自动安装。

# SUBCOMMANDS

**Build & Compile**
> build, build-params, decompile, decompile-params

**Validation**
> lint, format

**Parameters**
> generate-params

**Module Management**
> publish, restore

**CLI Management**
> install, uninstall, upgrade, version, list-versions

# PARAMETERS

**--file** _value_
> Bicep 文件路径。

**--outdir** _value_
> 构建产物的输出目录。

**--outfile** _value_
> 构建结果的输出文件路径。

**--stdout**
> 输出到 stdout 而非文件。

**--target** _value_
> 发布用的模块注册表目标。

**--version** _value_
> 要安装的指定 Bicep CLI 版本。

# CAVEATS

从 ARM 模板反编译得到的 Bicep 在功能上等价，但可能需要手动调整以提高可读性。发布模块需要具有相应权限的容器注册表。Bicep 参数文件需要 Azure CLI 2.53.0 或更高版本以及 Bicep CLI 0.22.x 或更高版本。

# HISTORY

Bicep 于 **2020** 年 **8 月**作为面向 Azure 部署的新语言公布，并于 **2021** 年 **5 月**达到 1.0 版本。它的设计目标是在保持与 Azure Resource Manager 完全兼容的同时，简化 ARM 模板的编写体验。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-deployment](/man/az-deployment)(1), [az-group](/man/az-group)(1)
