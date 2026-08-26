# TAGLINE

扫描安全漏洞

# TLDR

**审计依赖**

```npm audit```

**修复漏洞**

```npm audit fix```

**强制修复（含破坏性变更）**

```npm audit fix --force```

**以 JSON 格式输出**

```npm audit --json```

**仅审计生产依赖**

```npm audit --omit=dev```

**设置最低严重级别**

```npm audit --audit-level=[high]```

**试运行修复**（预览变更而不实际应用）

```npm audit fix --dry-run```

# SYNOPSIS

**npm** **audit** [_options_]

# PARAMETERS

**fix**
> 自动安装兼容的更新来修复漏洞。

**--force**
> 强制更新到最新版本，即使包含破坏性变更。

**--json**
> 以 JSON 格式输出结果。

**--omit** _TYPE_
> 从审计中省略某类依赖（dev、optional 或 peer）。取代已弃用的 --production 标志。

**--audit-level** _LEVEL_
> 触发非零退出码所需的最低严重级别：low、moderate、high、critical。

**--dry-run**
> 预览 audit fix 将做出的更改而不实际应用。

**--package-lock-only**
> 仅修改 package-lock.json，跳过 node_modules 的更新。

**--parseable**
> 以可解析的输出格式显示漏洞。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**npm audit** 通过将项目依赖与 npm 安全公告数据库比对，扫描其中已知的安全漏洞。它会报告严重级别（low、moderate、high、critical）、存在漏洞的软件包以及依赖路径。

**npm audit fix** 子命令会自动安装兼容的更新来解决漏洞。使用 **--force** 允许大版本更新，但可能引入破坏性变更。发现漏洞时该命令会以非零码退出，因此适合在 CI/CD 流水线中使用。

# CAVEATS

需要网络访问以查询 npm 安全公告数据库。--force 标志可能安装带有破坏性变更的更新；请务必先用 --dry-run 检查。--production 标志在 npm 8 及以上版本已弃用；请改用 --omit=dev。

# HISTORY

npm audit 于 **npm 6**（2018 年）推出，用于提供自动化的安全漏洞扫描。它取代了 npm 收购的第三方工具 `nsp`（Node Security Platform）。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-fund](/man/npm-fund)(1), [snyk](/man/snyk)(1)
