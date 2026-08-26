# TAGLINE

用于安装和管理 Unity 编辑器、模块和项目的独立 CLI

# TLDR

**安装**最新的长期支持（LTS）编辑器

```unity install lts```

**安装特定版本编辑器**并附带 Android、iOS 和 WebGL 模块

```unity install [6000.2.10f1] -m android ios webgl```

**列出本机已安装的编辑器**

```unity editors -i```

**打开项目**（从项目设置中解析所需的编辑器版本）

```unity open [path/to/project]```

**登录** Unity 账户（浏览器流程）

```unity auth login```

对 CLI 二进制文件进行**自我更新**

```unity upgrade```

**显示子命令的帮助**

```unity install --help```

# SYNOPSIS

**unity** [_global-options_] _command_ [_args_]

# DESCRIPTION

**unity** 是 Unity Technologies 推出的独立命令行界面，可在终端中安装和管理 Unity 编辑器及模块，无需 Unity Hub 桌面应用。它是一个独立的二进制程序，面向 CI 代理、自动化脚本和以终端为先的工作流。该工具目前处于实验阶段；标志和子命令可能在各版本之间发生变化。

通过 **unity**，你可以按版本或别名（**lts**、**latest**、主版本流如 **6**）下载编辑器、添加平台模块（**android**、**ios**、**webgl** 等）、列出已安装和可用的发行版、用匹配的编辑器打开项目、管理许可证和身份验证，以及通过 **unity upgrade** 自我更新。输出可以是人可读格式、**json**、**tsv** 或 **ndjson**，便于管道处理。

驱动*运行中*的编辑器（例如 **unity command** 或 **unity command eval**）需要项目中安装实验性的 **com.unity.pipeline** 软件包；登录后可用 **unity pipeline install** 安装。对于纯粹的编辑器安装和打开项目的工作流，这一层是可选的。

在 Linux 上，官方安装脚本将二进制文件放在 **~/.local/bin/unity**。软件包和 Homebrew 安装使用的包名为 **unity-cli**，但仍然提供 **unity** 命令，因为在某些发行版上 **unity** 这个名字已被其他软件包占用。

# PARAMETERS

全局选项和完整的子命令集取决于版本。请对已安装的二进制文件运行 **unity --help** 和 **unity** _command_ **--help**。常用命令：

**install** [_version_] [**-m** _module_...]

> 安装编辑器。版本可以是完整字符串（例如 **6000.3.7f1**），也可以是 **lts** 或 **latest** 等别名。别名 **i**。

**install-modules** **-e** _version_ **-m** _module_...

> 为已通过 Hub 或此 CLI 安装的编辑器添加模块。别名 **im**。

**uninstall** _version_

> 移除已安装的编辑器。别名 **u**。

**editors** [**-i** | **-r**]

> 列出已安装（**-i**）或可用（**-r**）的编辑器；子命令包括 **add** 和 **default**。别名 **e**。

**open** _path_

> 用项目声明的编辑器版本打开项目。第一个参数若是路径，则等同于 **open**。

**auth** **login** | **status** | **logout**

> 管理 Unity 账户会话。别名 **a**。

**upgrade**

> 将 CLI 二进制文件替换为最新版本（如果安装由包管理器管理，则打印相应的升级命令）。

**doctor**

> 打印环境和配置诊断信息。

**--format** _human|json|tsv|ndjson_

> 为自动化选择结构化输出。**--json** 是 JSON 的全局简写。

# INSTALLATION

**安装脚本**（macOS/Linux；截至 2026 年为 beta 频道）：

```
curl -fsSL https://public-cdn.cloud.unity3d.com/hub/prod/cli/install.sh | UNITY_CLI_CHANNEL=beta bash
```

**Homebrew cask**（二进制名仍为 **unity**）：

```
brew install --cask unity-cli
```

**Linux 软件包**（Unity 仓库；包名 **unity-cli**）：

```
sudo apt install unity-cli
```

```
sudo dnf install unity-cli
```

请先按照官方文档说明注册 Unity 的 apt/rpm 仓库。可用 **unity upgrade** 自我更新；如果安装由包管理器管理，则使用相应的包管理器。

# CAVEATS

Unity 将该 CLI 标记为实验性。仍在以 **-- --headless** 调用 Hub 的脚本需要迁移：版本标志、错误流（**stderr**）、管道默认输出格式（**tsv**）和退出码都与旧的 Hub CLI 不同。

模块只能添加到通过 Hub 或此 CLI 安装的编辑器。手动解压安装的编辑器必须重新安装或注册后才能使用模块。

驱动运行中的编辑器需要 **com.unity.pipeline** 以及已登录的会话；该软件包同样处于实验阶段。

# HISTORY

Unity 长期以来通过 **-- --headless** 提供 Hub 桌面自动化。**2026 年**，Unity 推出了这个独立的 **unity** 二进制程序，作为面向终端和 CI 工作流的更快、无依赖的替代方案，具备结构化输出、服务账户身份验证，以及通过 Pipeline 软件包实现的可选实时编辑器控制。

# SEE ALSO

[godot](/man/godot)(1)

# RESOURCES

```[Documentation](https://docs.unity.com/en-us/unity-cli)```

```[Homepage](https://unity.com/blog/meet-the-unity-cli)```

<!-- verified: 2026-08-11 -->
