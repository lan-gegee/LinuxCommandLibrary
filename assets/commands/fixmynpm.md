# TAGLINE

审计并修复不安全的 npm 配置文件

# TLDR

**检查全局 ~/.npmrc** 的安全与配置问题

```fixmynpm doctor```

**扫描目录树**中的所有 .npmrc 文件并报告问题

```fixmynpm audit --root [path/to/projects]```

**对 .npmrc 文件应用建议修复**

```fixmynpm fixer --root [path/to/projects]```

预览更改但**不写入**任何内容（试运行）

```fixmynpm fixer --root [path/to/projects] --dry-run```

**在全部 node_modules 中追查特定软件包**（事件响应）

```fixmynpm scan --package "[lodash@4.17.20]" --incident```

查找匹配 **glob 模式**的 .npmrc 文件

```fixmynpm scan --root [~/code] --npmrc```

# SYNOPSIS

**fixmynpm** _command_ [_options_]

# DESCRIPTION

**fixmynpm** 是一款诊断型 CLI，用来发现和修复不安全或配置不当的 **.npmrc** 文件。它会检查全局 **~/.npmrc**，遍历项目目录找出嵌套的 **.npmrc** 文件，对照内置的安全规则库逐条审计，并且可以自动应用修复。内置检查涵盖 registry 校验、TLS 设置、认证令牌处理、生命周期脚本执行以及依赖混淆风险。

除了配置体检之外，**fixmynpm** 还能充当事件响应工具：**scan** 命令可以递归遍历 **node_modules**，按名称、版本范围或是否存在捆绑的 .npmrc 来定位特定的失陷软件包，因此在处置供应链安全通告时非常实用。

# PARAMETERS

**doctor**
> 检查 ~/.npmrc 并报告安全或配置违规项，附修复建议。

**audit**
> 递归扫描目录树，列出每一个 .npmrc 文件以及各自发现的问题。

**fixer**
> 对扫描发现的 .npmrc 文件应用推荐的修正。

**scan**
> 定位 .npmrc 文件，或在 node_modules 中搜索特定软件包（事件响应模式）。

**--root** _dir_
> scan、audit 和 fixer 的起始目录（默认为用户主目录）。

**--package** _glob_
> 把扫描结果过滤为名称或 glob 模式匹配的软件包。

**--version** _range_
> 与 **--package** 组合时，按 semver 版本范围过滤扫描结果。

**--npmrc**
> 将扫描输出限定于捆绑了 .npmrc 文件的软件包。

**--incident**
> 启用事件响应启发式检查，包括探测 node_modules 中捆绑的 .npmrc。

**--dry-run**
> 展示计划中的修改，但不改动任何文件。

# CAVEATS

只作用于 **.npmrc** 文件；不会修改 **package.json**、锁文件或已安装的二进制。fixer 会就地改写文件——大范围执行前请配合 **--dry-run** 或版本控制。事件响应扫描需要递归遍历所选根目录下的每个 **node_modules** 目录，在大规模工作站上可能很慢。

# HISTORY

**fixmynpm** 由 **madhugb** 创建，在一系列暴露了用户 **.npmrc** 危险默认配置的 npm 供应链事件之后，于 **2026 年在 Hacker News 上公布**。它采用 **Go** 编写，通过 **go install github.com/madhugb/fixmynpm@latest** 分发。

# SEE ALSO

[npm](/man/npm)(1), [npm-audit](/man/npm-audit)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1)
