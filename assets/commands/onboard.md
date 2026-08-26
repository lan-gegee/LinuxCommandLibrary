# TAGLINE

基于 AST 的命令行工具，用于可视化代码库并强制执行架构边界

# TLDR

**初始化**项目配置和架构规则

```onboard init```

**在交互式画布中可视化**部分代码库

```onboard map --target "internal/parser" --radius 2```

**依据规则检测**架构漂移

```onboard drift --rules architecture.yml```

**提取**某个框架的后端路由

```onboard routes --protocol rest --framework express```

**通过提供的脚本安装**

```curl -fsSL https://raw.githubusercontent.com/animesh-94/Onboard-CLI/main/install.sh | bash```

# SYNOPSIS

**onboard** <command> [options]

# DESCRIPTION

Onboard-CLI 是一款基于 Go 的工具，使用 Tree-sitter 解析代码库（Go、JS/TS、Python、Java 等），构建结构图，并在本地 React Flow 可视化器中呈现。它还支持对照声明式架构规则的漂移检测，以及多种适用于大型系统和新人上手（onboarding）的分析命令。

它会启动一个本地 Web UI 供探索，并可集成到 CI 中以强制执行架构边界。

# COMMANDS

**init**
> 生成 .onboard 配置和 architecture.yml。

**map**
> 映射代码并启动可视化器服务器。

**drift**
> 检查架构规则违规。

**routes**
> 提取受支持框架的 API 路由。

**impact**, **owners**, **export**, **pulse**
> 其他分析命令。

# PARAMETERS

大多数命令可按需接受 `--target`、`--radius`、`--port` 以及框架/协议选择参数。

# CAVEATS

- 可视化器需要浏览器，并会打开一个本地端口。
- 规则评估基于导入路径的正则表达式；请谨慎调整 architecture.yml。
- 主要面向开发者工作流和 CI 门禁场景。

# INSTALL

```apt: sudo apt install onboard```

```pacman: sudo pacman -S onboard```

```apk: sudo apk add onboard```

```zypper: sudo zypper install onboard```

```nix: nix profile install nixpkgs#onboard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ast-grep](/man/ast-grep)(1), [rg](/man/rg)(1)

# RESOURCES

```[Source code](https://github.com/animesh-94/Onboard-CLI)```

```[Homepage](https://onboard-cli.vercel.app)```

```[Documentation](https://github.com/animesh-94/Onboard-CLI#readme)```

<!-- verified: 2026-07-11 -->
