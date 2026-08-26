# TAGLINE

扫描依赖中的已知安全漏洞

# TLDR

**审计依赖**中的已知安全漏洞

```bun audit```

**只报告高危和严重级别**的漏洞

```bun audit --audit-level=[high]```

**只审计生产依赖**，跳过 devDependencies

```bun audit --prod```

按 CVE 编号**忽略一个或多个漏洞**（可重复该标志）

```bun audit --ignore [CVE-2023-12345] --ignore [CVE-2023-67890]```

**输出 registry 的原始 JSON**（供 CI 解析）

```bun audit --json```

# SYNOPSIS

**bun** **audit** [_options_]

# PARAMETERS

**--audit-level**=_level_
> 只报告达到此严重程度或更高的漏洞。取值：**low**、**moderate**、**high**、**critical**。

**--prod**
> 只审计生产依赖，忽略 **devDependencies**。

**--ignore** _CVE_
> 忽略指定的 CVE。可重复使用以忽略多条通告。

**--json**
> 打印来自 npm registry 的原始 JSON 响应，而非格式化报告。

# DESCRIPTION

**bun audit** 将已安装软件包及其版本的列表（从 **bun.lock** 解析得到）发送到 npm registry，并打印返回的漏洞报告。registry 会与 GitHub Advisory Database 交叉比对，因此覆盖范围与 **npm audit** 报告的内容一致。

该命令按严重程度（**low**、**moderate**、**high**、**critical**）对发现的问题分类，涵盖直接依赖、**devDependencies**、**bundledDependencies** 和 **optionalDependencies**。

# EXIT STATUS

**0**
> 未发现漏洞。

**1**
> 发现了一个或多个漏洞。

# CAVEATS

只能发现已公开记录的安全通告。无法检测尚未被报告的零日漏洞利用、恶意软件、配置错误或供应链攻击。审计通过并不保证安全。需要存在 **bun.lock**，因此请先运行 **bun install**。与 **npm audit fix** 不同，**bun audit** 目前没有自动修复模式 - 你必须手动升级版本。

# HISTORY

**bun audit** 于 **Bun v1.2.15**（2025 年中）引入，为使用 Bun 包管理器的项目提供与 **npm audit** 兼容的安全扫描。

# SEE ALSO

[bun](/man/bun)(1), [bun-install](/man/bun-install)(1), [npm-audit](/man/npm-audit)(1), [snyk](/man/snyk)(1)
