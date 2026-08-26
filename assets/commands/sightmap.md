# TAGLINE

面向智能体 Web 应用上下文的 YAML 语料库与 CLI

# TLDR

全局**安装** CLI

```npm install -g @sightmap/sightmap```

把智能体技能**安装**到本地 harness

```sightmap skills install```

为项目语料库**启动** Chrome 会话

```sightmap browser start```

对 URL **快照**并统计未标注节点覆盖率

```sightmap snapshot --coverage --url '[https://example.com/path]'```

**校验**和**检查****.sightmap/** 语料库

```sightmap validate```

```sightmap lint --warn-only```

**报告**每个视图的覆盖健康度

```sightmap report```

# SYNOPSIS

**sightmap** _command_ [_options_]

# DESCRIPTION

**sightmap** 是 Sightmap 开放格式的官方 CLI。该格式是一个 **.sightmap/** YAML 目录，用于命名 Web 应用的视图、组件和 API 请求，还可包含自由格式的 **memory** 备注，记录源码中不会体现的运行时怪癖。

CLI 通过 Chrome DevTools Protocol 驱动真实浏览器，生成带标注的无障碍快照（将组件名叠加到树上）和结构化的交互事件。智能体以"编辑-验证"循环编写和维护语料库：先快照，修复孤立的可交互节点，再快照，直到覆盖完整。

可通过 npm 安装（**@sightmap/sightmap**），或在 monorepo 中用 Go 源码构建。编程智能体的技能可通过 **sightmap skills install** 安装。

# COMMANDS

**browser start** / **status**

> 启动 Chrome 和本地语料库服务器（默认端口 7891，支持 YAML 热重载），或显示会话状态。

**snapshot** [**--coverage**] [**--url** _url_]

> 捕获带标注的 ARIA 快照；配合 **--coverage** 时，打印 T1/T2/T3 标注统计和未标注簇。

**sel-probe** _selector_

> 对照实时页面验证候选 CSS 选择器。

**validate**

> 检查语料库的结构性 YAML 正确性（出错时以非零值退出）。

**lint** [**--warn-only**]

> 对语料库进行参考性的风格检查。

**capture** [**--all**]

> 刷新视图 URL 已保存的捕获。

**report**

> 每个视图的 T1/T2/T3 健康度表。

**skills install**

> 将内嵌的编写/浏览器技能解包到 **~/.agents/skills/**（或等效目录）。

**version**

> 打印 CLI 版本。

# CAVEATS

浏览器命令需要图形界面的 Chrome/Chromium 会话。覆盖率质量取决于稳定的选择器和持续维护的语料库。Sightmap 用于丰富智能体上下文，不能取代应用测试或无障碍审计。

# SEE ALSO

[chromium](/man/chromium)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/sightmap/sightmap)```

```[Homepage](https://sightmap.org)```

```[Documentation](https://docs.sightmap.org)```

<!-- verified: 2026-07-30 -->
