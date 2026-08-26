# TAGLINE

跨浏览器自动化与测试框架

# TLDR

**安装浏览器**

```npx playwright install```

**运行测试**

```npx playwright test```

**运行指定测试**

```npx playwright test [test.spec.ts]```

**以 UI 模式运行**

```npx playwright test --ui```

**生成代码**

```npx playwright codegen [url]```

# SYNOPSIS

**playwright** _command_ [_options_]

# PARAMETERS

**install** [_browser_]
> 安装浏览器（chromium、firefox、webkit）及其依赖。

**install-deps**
> 安装浏览器所需的操作系统级依赖（Linux）。

**test** [_files_]
> 运行 Playwright 测试。

**codegen** [_url_]
> 录制用户操作并生成测试代码。

**show-report** [_dir_]
> 在浏览器中打开 HTML 报告。

**open** [_url_]
> 在 Playwright inspector 中打开页面。

**--ui**
> 启动交互式 UI 模式，用于运行和调试测试。

**--debug**
> 以调试模式配合 Playwright Inspector 运行测试。

**--headed**
> 以有界面模式运行浏览器（显示窗口）。

**--project** _NAME_
> 只运行配置中给定的项目（浏览器）。

**--workers** _N_
> 并行测试工作进程的数量。

**--reporter** _NAME_
> 使用的报告器（list、dot、line、html、json、junit）。

**--grep** _PATTERN_
> 只运行匹配正则表达式的测试。

**--retries** _N_
> 失败测试的重试次数。

# DESCRIPTION

**Playwright** 是一个浏览器自动化和测试框架。它支持 Chromium、Firefox 和 WebKit，通过统一的 API 实现跨浏览器测试。

# EXAMPLES

```bash
# Setup new project
npm init playwright@latest

# Run all tests
npx playwright test

# Run with specific browser
npx playwright test --project=firefox

# Debug failing test
npx playwright test --debug

# Generate code by recording
npx playwright codegen example.com

# Show HTML report
npx playwright show-report
```

# TEST EXAMPLE

```typescript
import { test, expect } from '@playwright/test';

test('basic test', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});
```

# CONFIGURATION

**playwright.config.ts** 或 **playwright.config.js**
> 项目配置文件，定义浏览器、测试目录、超时时间和报告器设置。

**PLAYWRIGHT_BROWSERS_PATH**
> 用于覆盖浏览器二进制文件下载位置的环境变量。

# CAVEATS

需要 Node.js。浏览器二进制文件体积较大。CI 环境可能需要特殊配置。

# HISTORY

Playwright 由 **Microsoft** 开发，出自 Puppeteer 背后的团队之手，于 2020 年发布。

# INSTALL

```nix: nix profile install nixpkgs#playwright```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[puppeteer](/man/puppeteer)(1), [node](/man/node)(1), [npx](/man/npx)(1)
