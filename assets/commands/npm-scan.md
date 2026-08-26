# TAGLINE

npm 供应链行为威胁扫描器

# TLDR

**扫描软件包的恶意模式**

```npm-scan [package-name]```

**扫描 lockfile**

```npm-scan scan-lockfile```

**以 JSON 格式导出发现结果**

```npm-scan [package-name] --json > [findings.json]```

**出现 critical 级别发现时让 CI 失败**

```npm-scan scan-lockfile --fail-on critical```

# SYNOPSIS

**npm-scan** [_package_] [_options_]
**npm-scan** **scan-lockfile** [_options_]

# PARAMETERS

**scan-lockfile**
> 分析当前项目 lockfile 中的依赖。

**--json**
> 以 JSON 格式输出发现结果。

**--fail-on** _SEVERITY_
> 当发现的严重程度达到或超过给定级别时，以非零状态退出。

**scan**
> 显式的扫描子命令（配合 **npx @lateos/npm-scan scan** 使用）。

# DESCRIPTION

**npm-scan** 是面向 npm 生态的命令行供应链安全工具。它结合静态与行为分析来检测 **npm audit**、Snyk 和 Socket 常常漏掉的攻击模式：混淆载荷、凭据窃取、eBPF rootkit、内存数据抽取、GitHub 作者伪造、针对 AI 平台密钥的攻击，以及利用窃取令牌进行的蠕虫式传播。

该工具内置 23 个检测器，均经过真实攻击活动（IronWorm、Miasma、依赖混淆）的验证。它完全在本地运行，没有遥测或云依赖，支持以 YAML 编写策略即代码（policy-as-code）白名单，并可导出 CycloneDX、SPDX 和 SARIF 格式。还提供 GitHub Action 用于 CI/CD 集成。

个人和开源评估可免费使用；商业生产用途需要 BLA 许可证。

# CAVEATS

行为检测可能会对带有异常安装脚本的合法软件包产生误报。它是对 **npm audit** 的补充而非替代——两者结合可以同时覆盖 CVE 数据库和行为威胁。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm-audit](/man/npm-audit)(1), [socket](/man/socket)(1), [snyk](/man/snyk)(1)

# RESOURCES

```[Source code](https://github.com/lateos-ai/npm-scan)```

```[Homepage](https://lateos.ai/npm-scan)```

<!-- verified: 2026-07-03 -->
