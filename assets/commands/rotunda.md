# TAGLINE

由命令行驱动的智能体优先网页浏览器

# TLDR

**下载**随附的浏览器构建版本

```uvx rotunda agent fetch```

创建一个**命名浏览器配置档案**

```uvx rotunda agent new-profile --name [agent-demo]```

在现有配置档案内打开一个新的**上下文**

```uvx rotunda agent new-context [agent-demo]```

将上下文**导航**至某个 URL

```uvx rotunda agent navigate [3] [https://example.com]```

**描述**当前页面以获取元素引用

```uvx rotunda agent describe [3]```

按引用**点击**某个元素

```uvx rotunda agent click [3] [ref_id]```

保存视口的**截图**

```uvx rotunda agent screenshot [3] --path [page.png]```

# SYNOPSIS

**rotunda agent** _subcommand_ [_context-id_] [_options_]

# DESCRIPTION

**Rotunda** 是一款专为 AI 智能体打造的浏览器。它内置一个隐蔽（stealth）的 Chromium 构建版本，提供用于导航、检查和表单交互的高级原语，并将配置档案、守护进程会话和短资源索引持久化保存在 **~/.rotunda** 下，这样后续的 **uvx rotunda** 调用无需重启即可附加到同一配置档案。

agent CLI 分为几个子命令族：配置档案与会话管理（**fetch**、**new-profile**、**new-context**、**stop**），导航原语（**navigate**、**back**、**forward**、**reload**、**wait**），检查（**describe**、**screenshot**、**extract**），以及交互（**click**、**hover**、**fill**、**type**、**select**、**check**、**press**、**upload**、**dialog**）。每个针对元素的命令都通过数字形式的上下文 id 和由 **describe** 返回的元素引用来定位目标。

Rotunda 也可以作为构建于 **Playwright** 之上的 Python 库导入，但对于基于 Shell 的智能体来说，CLI 是推荐的入口。

# PARAMETERS

**fetch**
> 将随附的浏览器构建版本下载到 ~/.rotunda。

**new-profile** **--name** _name_
> 创建一个持久的浏览器配置档案。

**new-context** _profile_
> 在指定配置档案中打开一个全新的浏览器上下文；打印一个数字形式的上下文 id。

**navigate** _ctx_ _url_
> 在给定上下文中加载 _url_。

**describe** _ctx_
> 打印页面结构以及其他命令所需的引用 id。

**click** _ctx_ _ref_, **hover** _ctx_ _ref_
> 与被引用的元素进行鼠标交互。

**fill** _ctx_ _ref_ _text_
> 替换输入字段的值。

**type** _ctx_ _text_
> 在当前焦点位置输入文本。

**select** _ctx_ _ref_ _value_
> 按值选择下拉选项。

**check** _ctx_ _ref_, **press** _ctx_ _key_
> 切换复选框 / 发送键盘按键。

**extract** _ctx_ [_--format_ _text|html|markdown|links_]
> 从页面提取文本、原始 HTML、Markdown 或链接列表。

**screenshot** _ctx_ [_--full-page_] [_--path_ _file_]
> 捕获视口或整个页面。

**upload** _ctx_ _ref_ _file_
> 将 _file_ 附加到文件输入元素。

**dialog** _ctx_ _action_
> 接受或关闭浏览器对话框（alert/confirm/prompt）。

**wait** _ctx_ _condition_
> 阻塞直到页面条件满足（加载状态、选择器、超时）。

**back**, **forward**, **reload** _ctx_
> 标准导航原语。

**stop**
> 关闭配置档案守护进程。

# CONFIGURATION

**~/.rotunda/**
> 在多次 **uvx rotunda** 调用之间共享的持久化配置档案、守护进程套接字和短资源索引。

**~/.rotunda/profiles/**_name_
> 通过 **new-profile** 创建的每个命名配置档案对应一个子目录。

# CAVEATS

需要已安装 **uv / uvx**；**uvx rotunda** 会按需下载并运行该项目。上下文通过数字 id 寻址，这些 id 仅在守护进程的生命周期内有效——调用 **stop** 会使其失效。规避机器人检测只能尽力而为；某些网站仍会拦截自动化流量。

# HISTORY

**Rotunda** 由 **MonkeySee AI** 于 **2026 年**发布，作为一个对智能体友好的浏览器层，填补了原始 Playwright 脚本与功能齐全的商业浏览器自动化服务之间的空白。其 CLI 界面刻意保持精简且稳定，以便 LLM 驱动的智能体无需专用的 SDK 即可调用。

# SEE ALSO

[playwright](/man/playwright)(1), [chromium](/man/chromium)(1), [puppeteer](/man/puppeteer)(1), [uv](/man/uv)(1)
