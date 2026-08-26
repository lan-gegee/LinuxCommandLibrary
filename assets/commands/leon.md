# TAGLINE

运行在自己服务器上的开源个人 AI 助手

# TLDR

**全局安装 Leon CLI**

```npm install --global @leon-ai/cli```

**创建新的 Leon 实例**

```leon create birth```

**基于 develop 分支创建实例**

```leon create birth --develop```

**启动 Leon**

```leon start```

**检查配置是否正确**

```leon check```

**查看实例信息**

```leon info```

# SYNOPSIS

**leon** _command_ [_options_]

# PARAMETERS

**create birth**
> 初始化并搭建一个新的 Leon 实例，包括全部所需依赖。

**start**
> 启动 Leon 服务器并开启交互。

**check**
> 验证设置是否成功完成。

**info**
> 查看某个 Leon 实例的详细信息。

**delete**
> 移除某个 Leon 实例。

**update**
> 将 Leon 更新到最新版本。

**run**
> 在 Leon 实例内执行 npm 脚本。

**help**
> 显示可用命令。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**Leon** 是一个运行在你自己服务器上的开源个人 AI 助手。它采用基于技能（skill）的架构，每项能力都是一个模块化的技能，可以独立安装、配置和扩展。

Leon 支持通过其 Web 界面进行语音交互和文本输入。它运行在 Node.js 上，并用 Python 运行时执行技能，因此可跨 Linux、macOS 和 Windows 平台运行。

这款助手专为自托管设计，让所有数据和计算都保留在你自己的基础设施上。技能涵盖生产力、实用工具和信息检索等类别。开发者可以创建自定义技能来扩展 Leon 的能力。随附的 CLI 可帮助设置和管理 Leon 实例。

# CAVEATS

需要在主机系统上安装 Node.js 和 Python。语音交互依赖麦克风以及受支持的语音识别配置。部分技能可能需要额外的 API 密钥才能集成外部服务。初始设置会下载多个依赖项，在网络较慢时可能耗时较长。

# HISTORY

Leon 由 **Louis Grenard** 创建，于 **2019 年**首次发布。项目主页位于 **getleon.ai**，已在 GitHub 上获得超过 15,000 颗星。它的设计初衷是作为 Alexa 和 Google Assistant 等云端助手的隐私优先替代品，强调自托管和开源可扩展性。目前开发仍在持续，社区活跃地贡献着技能和改进。

# INSTALL

```apt: sudo apt install gatb-core```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1)
