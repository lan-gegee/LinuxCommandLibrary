# TAGLINE

为代理和脚本提供程序化的 After Effects 控制

# TLDR

**启动**控制器（WebSocket、REST、UI、MCP 端点）

```aftr controller
npx aftr-studio controller```

启动 **stdio MCP** 适配器（控制器必须已在运行）

```aftr mcp
npx aftr-studio mcp```

运行无头**模拟器**（无需 After Effects）

```aftr sim```

# SYNOPSIS

**aftr** _command_ [_options_]

# DESCRIPTION

**aftr**（npm/PyPI 上的软件包名为 **aftr-studio**）是一座桥梁，让代码和 AI 代理得以驱动 Adobe After Effects。一个 Node 控制器承载 WebSocket 与 REST API；After Effects 内的 CEP 面板负责执行 ExtendScript 命令并推送渲染进度。代理和 UI 都连接到控制器，而不是直接给 AE 写脚本。

典型设置流程：从克隆的仓库一次性安装 CEP 面板（**npm run deploy:panel**），在 After Effects 中打开 **Window → Extensions → aftr**，运行 **aftr controller**，然后把 Claude Code 或其他 MCP 客户端接到 **http://127.0.0.1:8787/mcp**（或通过 **aftr mcp** 使用 stdio MCP）。命令覆盖合成（comp）、图层、关键帧、效果、文本动画器、VFX 预设以及非阻塞的 **aerender** 作业。无头模拟器可在没有 AE 的情况下演练同一套协议。

# PARAMETERS

**controller**
> 启动桥接服务器（默认 **127.0.0.1:8787**）

**mcp**
> stdio MCP 服务器，把工具调用转发给正在运行的控制器

**sim**
> 用于测试和演示的无头 AE 面板模拟器

# CONFIGURATION

根目录下的 **config.json** 设置主机、端口、路径和超时时间。环境变量覆盖项包括 **AE_BRIDGE_HOST**、**AE_BRIDGE_PORT**、**AE_BRIDGE_TOKEN**（暴露到回环地址之外时用于认证）、**AE_BRIDGE_AERENDER**、**AE_BRIDGE_FFMPEG** 和 **AE_BRIDGE_ALLOW_DEV**。需要 After Effects 2024–2026、Node 18+，并且流水线功能要求 **PATH** 中有 **ffmpeg**。

# CAVEATS

完整的创作控制需要已获许可安装的 After Effects，以及已部署且经过签名的 CEP 面板。在没有 **AE_BRIDGE_TOKEN** 的情况下把控制器暴露到 localhost 之外并不安全。真实的 AE 仅支持 macOS 和 Windows；Docker 镜像只提供不含面板的控制器。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/Arman-Luthra/aftr)```

```[Homepage](https://www.npmjs.com/package/aftr-studio)```

<!-- verified: 2026-07-14 -->
