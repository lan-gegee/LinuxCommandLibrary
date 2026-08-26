# TAGLINE

支持插件、代码检查与转换的 Go 版 TypeScript 编译器

# TLDR

**构建**项目（**tsc** 的直接替代）

```ttsc```

仅**类型检查**而不输出文件

```ttsc --noEmit```

**监视**文件并在保存时重新构建

```ttsc --watch```

**应用 lint 自动修复**并进行格式化

```ttsc fix```

仅**格式化**（不改变程序行为）

```ttsc format```

# SYNOPSIS

**ttsc** [_options_] [_project_options_]

**ttsc** **fix** | **format**

# DESCRIPTION

**ttsc** 是一个基于 **typescript-go** 构建的 TypeScript 工具链。它是 **tsc** 的直接替代品：读取相同的 **tsconfig.json**，接受相同的编译器选项，输出相同的 JavaScript，然后在类型检查阶段运行由编译器驱动的插件。

插件可以添加转换、额外的检查或基于类型的代码生成（例如 **typia** 校验器）。安装 **@ttsc/lint** 后，lint 和格式化规则会在同一次编译中执行，违规项会以编译器诊断的形式出现。子命令 **fix** 和 **format** 会就地应用自动修复和格式化。

将其作为开发依赖安装（**npm install -D ttsc typescript**），然后通过 **npx ttsc** 或包脚本调用。可与 **ttsx** 搭配使用，在完整项目类型检查之后执行 TypeScript。

# PARAMETERS

支持大多数 **tsc** 选项，包括：

**--noEmit**
> 仅类型检查；不写入输出文件

**--watch**, **-w**
> 监视输入文件并在变化时重新构建

**--project**, **-p** _path_
> 编译配置文件所指定的项目

**--pretty**
> 用颜色和上下文美化错误和消息显示（默认行为与 **tsc** 相同）

**fix**
> 应用 lint 自动修复和格式化修改

**format**
> 仅应用格式化修改；绝不改变程序行为

# CAVEATS

需要与 **ttsc** 一同安装 **typescript**。插件和 lint 行为取决于已安装的 **@ttsc/**\* 软件包和项目配置（例如 **lint.config.ts**）。并非所有第三方 **tsc** 封装选项都能一一对应；打包器和 Metro 集成请优先参考官方的 **ttsc** 配置指南。

# HISTORY

由 Jeongho Nam（**samchon**）创建，作为 **ttypescript** 和 **ts-patch** 等转换工具链的现代继任者，面向 **typescript-go** 编译器，并集成了 lint、格式化和 MCP 代码图谱工具。

# SEE ALSO

[ttsx](/man/ttsx)(1), [tsc](/man/tsc)(1), [tsx](/man/tsx)(1), [ts-node](/man/ts-node)(1)

# RESOURCES

```[Source code](https://github.com/samchon/ttsc)```

```[Homepage](https://ttsc.dev)```

```[Documentation](https://ttsc.dev/docs)```

<!-- verified: 2026-07-17 -->
