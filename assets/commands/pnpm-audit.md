# TAGLINE

检查 pnpm 依赖中的安全漏洞

# TLDR

**运行安全审计**

```pnpm audit```

**修复漏洞**

```pnpm audit --fix```

**JSON 输出**

```pnpm audit --json```

**仅审计生产依赖**

```pnpm audit --prod```

# SYNOPSIS

**pnpm audit** [_options_]

# PARAMETERS

**--fix**
> 在 **package.json** 中添加 overrides，将存在漏洞的传递依赖固定到安全版本。

**--json**
> 以 JSON 格式输出审计报告。

**-P**, **--prod**
> 仅审计生产依赖（跳过 _devDependencies_）。

**-D**, **--dev**
> 仅审计开发依赖。

**--no-optional**
> 审计时跳过可选依赖。

**--audit-level** _LEVEL_
> 报告的最低严重级别：_low_、_moderate_、_high_ 或 _critical_（默认：_low_）。

**--ignore** _CVE_
> 按标识符忽略特定的安全公告。

**--ignore-unfixable**
> 跳过没有可用补丁的安全公告。

**--ignore-registry-errors**
> 当 registry 返回非 200 状态码时以退出码 0 结束，仅在发现真实漏洞时才失败。

# DESCRIPTION

**pnpm audit** 使用 npm 安全公告数据库扫描项目依赖中已知的安全漏洞。它会报告受影响的软件包、严重级别以及可用的已修复版本。

**--fix** 选项会尝试自动将有漏洞的软件包更新到安全版本。使用 **--prod** 或 **--dev** 可分别将扫描范围限制为生产依赖或开发依赖。**--audit-level** 选项设置报告的最低严重级别阈值（low、moderate、high、critical）。

# CAVEATS

需要网络访问。使用 npm 安全公告数据库。

# HISTORY

pnpm audit 是为了扫描依赖中的**安全漏洞**而添加的。

# INSTALL

```dnf: sudo dnf install pnpm```

```pacman: sudo pacman -S pnpm```

```apk: sudo apk add pnpm```

```zypper: sudo zypper install pnpm```

```brew: brew install pnpm```

```nix: nix profile install nixpkgs#pnpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnpm](/man/pnpm)(1), [npm-audit](/man/npm-audit)(1)
