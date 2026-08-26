# TAGLINE

Google 的自动化网页审计工具

# TLDR

**审计一个 URL**

```lighthouse [https://example.com]```

**输出到指定文件**

```lighthouse [https://example.com] --output-path [report.html]```

**以 JSON 输出**

```lighthouse [https://example.com] --output json```

**审计特定类别**

```lighthouse [https://example.com] --only-categories=performance,accessibility```

**使用无头 Chrome**

```lighthouse [https://example.com] --chrome-flags="--headless"```

**设置视口**

```lighthouse [https://example.com] --screenEmulation.width=[1920]```

# SYNOPSIS

**lighthouse** _url_ [_options_]

# PARAMETERS

**--output** _format_
> 输出格式（html、json、csv）。

**--output-path** _file_
> 报告保存路径。

**--only-categories** _list_
> 要审计的类别。

**--chrome-flags** _flags_
> Chrome 启动标志。

**--preset** _preset_
> 审计预设（desktop、perf）。

**--view**
> 在浏览器中打开报告。

**--quiet**
> 抑制输出。

**--port** _PORT_
> 用于调试协议的端口。

**--form-factor** _FACTOR_
> 模拟移动端或桌面端（mobile|desktop）。

**--save-assets**
> 保存工件（截图、trace、devtools 日志）。

**--budget-path** _FILE_
> 性能预算 JSON 文件的路径。

**--verbose**
> 启用详细日志记录。

# DESCRIPTION

**lighthouse** 是 Google 的自动化网页审计工具。它测试性能、无障碍性、最佳实践、SEO 以及渐进式 Web 应用特性，并生成包含改进建议的详细报告。默认模拟移动设备。

Lighthouse 需要安装 Chrome 或 Chromium，它会启动浏览器来执行审计。该工具也内置在 Chrome DevTools 中，并可作为 Node.js 模块在 CI 管道中以编程方式使用。

# CAVEATS

需要 Node.js 和兼容的 Chrome/Chromium 安装。受网络状况和系统负载影响，结果在不同运行之间可能有差异；建议多次审计以保证稳定性。除非指定 **--preset=desktop**，否则默认使用移动端模拟。

# HISTORY

**Lighthouse** 由 **Google** 开发，约于 **2016 年**首次发布，是 Chrome DevTools 生态系统的一部分。最初专注于渐进式 Web 应用，现已成长为涵盖性能、无障碍性、SEO 和最佳实践的综合网页质量审计工具。

# INSTALL

```apk: sudo apk add lighthouse```

```brew: brew install lighthouse```

```nix: nix profile install nixpkgs#lighthouse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1), [puppeteer](/man/puppeteer)(1)
