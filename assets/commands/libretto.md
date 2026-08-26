# TAGLINE

用于构建和维护浏览器自动化的 AI 工具包

# TLDR

在当前目录**搭建一个新的 Libretto 项目**

```npm create libretto@latest```

将 Libretto **安装**到现有的 Node 项目中

```npm install libretto && npx libretto setup```

在受控的浏览器会话中**打开 URL**

```npx libretto open [https://example.com]```

**截取快照**（HTML + 截图）并交给 LLM 分析

```npx libretto snapshot --objective "[find the login form]"```

对当前页面**执行 Playwright TypeScript**

```npx libretto exec "[await page.click('button.submit')]"```

**运行已保存的工作流文件**

```npx libretto run [src/workflows/scrape-page.ts]```

**定向到具名会话**（多个窗口可以共存）

```npx libretto snapshot --session [checkout] --objective "[verify total]"```

# SYNOPSIS

**libretto** _command_ [_options_]

# COMMANDS

**setup**
> 下载捆绑的 Chromium 构建版本，并配置快照分析模型。

**open** _URL_
> 启动浏览器并导航到 _URL_。

**snapshot** **--objective** _TEXT_
> 捕获 HTML 和 PNG 截图，然后围绕给定目标总结该页面。

**exec** _CODE_
> 对当前页面运行一段 Playwright TypeScript 代码。

**run** _FILE_
> 执行一个由 TypeScript 编写、可编排多个步骤的工作流文件。

**help**
> 打印完整的命令列表。

# PARAMETERS

**--session** _NAME_
> 定向到某个具名浏览器会话，避免并行工作流互相干扰。

**--objective** _TEXT_
> 在快照过程中传给模型的自然语言目标。

**--headless**
> 不显示窗口地运行 Chromium。

**--model** _NAME_
> 覆盖用于分析快照的 LLM。

# DESCRIPTION

**Libretto** 是构建于 **Playwright** 之上的 CLI 和编码智能体技能，帮助工程师为没有正式 API 的系统编写和维护浏览器自动化。开发者不必手写选择器，只要把 Libretto 指向一个活动页面，让 LLM 输出"节省 token"的摘要、网络请求记录和 DOM 片段，即可直接粘贴进智能体提示词。

典型工作流是：先用 **libretto open** 打开页面，再用 **libretto snapshot** 捕获上下文，接着用 **libretto exec** 迭代调试，最后把步骤固化进一个 TypeScript 文件，日后可用 **libretto run** 重放。所有状态都保存在项目级的 _.libretto/_ 目录中（会话、浏览器档案、捕获的流量）。

# CONFIGURATION

Libretto 会从项目的 **.env** 文件中读取所配置 LLM 服务商（OpenAI、Anthropic 等）的 API 密钥。_.libretto/_ 目录保存：

```
.libretto/
  sessions/         # Playwright user-data directories
  snapshots/        # captured HTML + PNG + summaries
  profiles/         # reusable configuration presets
```

# CAVEATS

Libretto 依赖 Chromium，并会在 **libretto setup** 阶段下载它；公司代理可能会拦截下载。由于该工具会将页面内容交给 LLM 处理，对已登录页面做快照时务必注意不要泄露机密信息。库版本和 Playwright API 可能频繁变动——请在 _package.json_ 中固定版本号。

# HISTORY

Libretto 由 **Saffron Health** 发布，是一个开源工具包，致力于让基于浏览器的集成对智能体更加友好。它把 Playwright 与具有模型感知能力的 CLI 以及面向编码助手发布的 **Model Context Protocol (MCP)** 技能结合在一起。

# SEE ALSO

[playwright](/man/playwright)(1), [npx](/man/npx)(1), [curl](/man/curl)(1), [puppeteer](/man/puppeteer)(1)
