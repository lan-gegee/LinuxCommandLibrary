# TAGLINE

面向 AI 智能体打造的浏览器自动化 CLI

# TLDR

从受保护的页面**提取**内容（隐蔽模式）

```browser-act stealth-extract [https://example.com]```

在**会话**中打开页面

```browser-act --session [my-task] browser open [id] [https://example.com]```

读取带**索引**的页面状态

```browser-act --session [my-task] state```

按元素索引**点击**

```browser-act --session [my-task] click [3]```

按索引向输入框**输入文字**

```browser-act --session [my-task] input [2] "[text]"```

加载智能体**技能**快照

```browser-act get-skills core --skill-version [2.0.2]```

# SYNOPSIS

**browser-act** [_--session_ _name_] _command_ [_args_...]

# PARAMETERS

**--session** _name_
> 命名会话，用于多任务隔离和并发执行。

**stealth-extract** _url_
> 以隐蔽模式一次性抓取受保护页面的内容。

**browser open** _id_ _url_
> 在浏览器实例中打开 URL。

**state**
> 返回带索引的可交互元素列表（对 LLM 而言更省 token）。

**click** _index_
> 点击 `state` 中给定索引处的元素。

**input** _index_ _text_
> 向给定索引处的元素输入文字。

**solve-captcha**
> 在可用时自动解决 CAPTCHA 验证码。

**remote-assist**
> 生成一个实时 URL 供人工接管，然后恢复智能体运行。

**get-skills**
> 返回环境状态、浏览器列表以及可供智能体使用的命令。

# DESCRIPTION

**browser-act** 是一款专为 AI 编程智能体设计的浏览器自动化命令行工具。它强调抗反爬能力（指纹、代理、CAPTCHA 辅助）、多会话并发且互不串 cookie，并输出紧凑的带索引文本，让模型只需点击 `3` 而不必解析 HTML。

其模式包括复用本地 Chrome 登录态、隐蔽隐私会话（全新指纹），以及适用于多账户工作流的固定身份隐蔽模式。敏感操作可在技能层要求确认把关。

# CAVEATS

完整安装面向智能体设计（技能包来自 BrowserAct skills 仓库）。部分隐蔽/代理功能需要免费登录或付费方案。自动化第三方网站可能违反其服务条款——请负责任地使用。

# HISTORY

开源的 **BrowserAct Skills** 项目，为 Windows、macOS 和 Linux 上的智能体工具链提供浏览器层。

# SEE ALSO

[playwright](/man/playwright)(1), [chromium](/man/chromium)(1)

# RESOURCES

```[Source code](https://github.com/browser-act/skills)```

```[Homepage](https://www.browseract.com)```

```[Documentation](https://github.com/browser-act/skills/blob/main/docs/README.md)```

<!-- verified: 2026-07-28 -->
