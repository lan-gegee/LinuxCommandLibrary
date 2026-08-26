# TAGLINE

为项目生成软件物料清单

# TLDR

**以默认格式生成 SBOM**

```npm sbom```

**以 SPDX 格式生成**

```npm sbom --sbom-format spdx```

**以 CycloneDX 格式生成**

```npm sbom --sbom-format cyclonedx```

**输出到文件**

```npm sbom --sbom-format cyclonedx > [sbom.json]```

**省略开发依赖**

```npm sbom --omit dev```

**只使用 package-lock.json**（忽略 node_modules）

```npm sbom --package-lock-only```

# SYNOPSIS

**npm** **sbom** [_options_]

# PARAMETERS

**--sbom-format** _FORMAT_
> 输出格式：spdx 或 cyclonedx（必填）。

**--sbom-type** _TYPE_
> 软件包类型：library（默认）、application 或 framework。

**--omit** _TYPE_
> 省略某类依赖（dev、optional、peer）。

**--package-lock-only**
> 只使用 package-lock.json，忽略 node_modules。

**--workspace** _name_
> 在指定工作区的上下文中运行。

**--workspaces**
> 对所有已配置的工作区运行。

# DESCRIPTION

**npm sbom** 生成软件物料清单（SBOM），列出当前项目的全部依赖。它支持 **SPDX** 和 **CycloneDX** 格式，两者都是记录软件供应链组件的行业标准。输出包括软件包名称、版本、许可证和依赖关系。

# CAVEATS

需要 npm 9.5.0 或更高版本。必须存在 package-lock.json 或 node_modules。要得到可用的输出，--sbom-format 选项是必需的。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-audit](/man/npm-audit)(1), [npm-ls](/man/npm-ls)(1)
