# TAGLINE

面向 AI 编码代理的高速无头验证浏览器

# TLDR

先**安装**再运行 setup 以检测代理工作流

```hwatu setup```

以**无头**方式打开站点并运行一次性的 verify 流程

```hwatu check localhost:5173 --eval 'document.title' --shot=/tmp/after.png```

像终端浏览器一样打开 URL（默认无头）

```hwatu localhost:3000```

对两个已打开的窗口进行**像素 diff** 并打印匹配百分比

```hwatu diff --id 2 --other 1 --heatmap /tmp/heat.png```

从 stdin **渲染** HTML 并截图

```echo '<h1>hi</h1>' | hwatu render --stdin --shot=/tmp/gen.png```

把一个活动会话在平铺窗口管理器中交给**人类**

```hwatu focus [window_id]```

为代理客户端启动 **MCP** 服务器

```hwatu mcp```

# SYNOPSIS

**hwatu** [_options_] [_url_]

**hwatu** **check**|_diff_|_motion_|_snapshot_|_focus_|_render_|_setup_|_doctor_|_mcp_ ...

# PARAMETERS

**check** _url_
> 一次性验证：加载页面，可选 eval/截图，返回 JSON 指标

**diff** **--id** _n_ **--other** _m_
> 对两个窗口做像素 diff；可选 **--heatmap** 路径

**motion** **--id** _n_
> 将动画以数值形式报告（时长、缓动、速度）

**snapshot**
> 以结构化 JSON 形式呈现页面状态（token 而非像素）

**render** **--stdin**
> 从 stdin 渲染标记语言，无需本地 HTTP 服务器

**focus** _id_
> 将无头窗口实体化为可见会话以便人工接管

**setup** [**--client** _name_] [**--scope** project|user] [**--dry-run**] [**--undo**]
> 检测编码代理并配置 MCP/socket 连接

**doctor**
> 环境与就绪状态检查

**mcp**
> 作为 MCP 服务器运行（`command: hwatu`、`args: ["mcp"]`）

**demo**
> 运行内置的演示验证流程

**--headless**
> 无头窗口模式（代理使用的默认值；按窗口的属性）

# DESCRIPTION

**hwatu** 是一个专为 AI 代理循环构建的 Linux 验证浏览器：它是一个常驻的 WebKitGTK 守护进程，保持引擎热身使页面检查开销极低（约几十毫秒），返回的是可度量的原语（像素匹配分数、动画指标、控制台/网络错误）而不仅仅是原始截图，并且可以在任务中途把**同一个活动会话**移交给人类而不丢失 cookie 或状态。

它以静态二进制加发行版 webkitgtk 的形式发布，提供简洁的 CLI、一个 MCP 服务器以及换行分隔 JSON 的 Unix socket 协议。典型的代理流程是：打开无头窗口，反复 `check` 或 `diff` 直到匹配百分比上升，只有当出现 CAPTCHA 或需要人为判断时才 `focus`。

仅限 Linux；渲染引擎是 WebKit 而非 Chromium——针对引擎相关的缺陷，请在 CI 中保留一套 Chromium 测试矩阵。

# CAVEATS

要求主机上安装 WebKitGTK 6.x。无头是可在运行中实时切换的按窗口属性，而非仅限启动时设置的模式。采用 AGPL-3.0 许可证。不能完全替代 Playwright 的多浏览器 CI 矩阵。

# HISTORY

这是一个开源 Rust 项目，旨在让代理的浏览器验证变成单次工具调用，而不是多步骤的 Playwright/devtools 会话，并把可中断的人工移交作为一等特性。

# INSTALL

```aur: yay -S hwatu```

<!-- packages: 2026-07-29 -->

# SEE ALSO

[playwright](/man/playwright)(1), [chromium](/man/chromium)(1)

# RESOURCES

```[Source code](https://github.com/hongnoul/hwatu)```

```[Documentation](https://github.com/hongnoul/hwatu/tree/main/docs)```

<!-- verified: 2026-07-29 -->
