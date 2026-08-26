# TAGLINE

让 AI 编码智能体截取浏览器标签页屏幕截图的 CLI

# TLDR

**启动**供浏览器扩展连接的 WebSocket 守护进程

```peeked start```

**列出**当前跟踪的浏览器标签页 URL

```peeked list```

**截取**给定 URL 对应页面的屏幕截图（扩展必须已连接）

```peeked at http://localhost:3000```

**检查**服务器和扩展的连接状态

```peeked status```

**停止** WebSocket 服务器

```peeked stop```

# SYNOPSIS

**peeked** _command_ [arguments]

# COMMANDS

**start**

> 启动本地 WebSocket 服务器（端口 7336），接收截图请求并流式对接浏览器扩展。启动时会清理之前的图片。

**list**

> 列出已连接的浏览器扩展所报告的全部被跟踪标签页 URL。

**at** _url_

> 向已连接的浏览器标签页请求指定 URL 的屏幕截图。JPEG 会保存到一个临时目录（例如 `$TMPDIR/peek_cli/images/`）。

**status**

> 报告服务器是否在运行以及是否已有浏览器扩展连接。

**stop**

> 停止正在运行的 WebSocket 服务器进程。

# DESCRIPTION

`peeked` 是 peek-cli 的命令行组件。它让 AI 编码智能体（如 Claude Code、Codex 等）能够获取打开的浏览器标签页的实时屏幕截图。

该工具由 `peeked start` 启动的本地 WebSocket 服务器构成。一个配套的 Chrome 扩展连接到该服务器，并按需转发屏幕截图。智能体通过 CLI（或经由智能体技能/插件）发出命令来列出标签页和请求截图。

屏幕截图以 base64 形式传送并由 CLI 写入本地；智能体从不直接访问浏览器，也不注入代码。

安装：

```bash
npm i -g peeked
```

还必须从 Chrome 网上应用店安装配套的浏览器扩展。

# CAVEATS

需要官方的 Peek CLI Chrome 扩展；没有它，服务器就没有可报告或截图的标签页。

服务器只绑定到 localhost。使用前必须在每台机器/会话上显式启动它。

屏幕截图写入每用户的临时目录，除执行 `start` 时外不会自动清理。

在某些版本中，错误消息可能引用过时的命令名（例如 "peeked begin"）。

仅提供只读的截图能力；无法进行导航、输入或页面操作。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1)

# RESOURCES

```[Source code](https://github.com/puffinsoft/peek-cli)```

<!-- verified: 2026-07-11 -->
