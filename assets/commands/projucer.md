# TAGLINE

JUCE 音频框架项目管理器

# TLDR

**打开项目**

```Projucer [project.jucer]```

**创建新项目**

```Projucer --create-project [project-name]```

**重新保存项目文件**

```Projucer --resave [project.jucer]```

**设置 JUCE 路径**

```Projucer --set-global-search-path [os] [key] [path]```

**生成 Makefile**

```Projucer --resave [project.jucer]```

**显示状态**

```Projucer --status [project.jucer]```

# SYNOPSIS

**Projucer** [_--resave_] [_--create-project_] [_options_] [_file_]

# PARAMETERS

**--resave** _FILE_
> 重新生成 IDE 文件。

**--create-project** _NAME_
> 创建新项目。

**--status** _FILE_
> 显示项目状态。

**--set-global-search-path** _OS KEY PATH_
> 设置模块路径。

**--help**
> 显示帮助。

# DESCRIPTION

**Projucer** 是 JUCE 框架的项目管理工具，用于创建和维护跨平台的音频应用和插件。它读取 **.jucer** 项目文件（其中定义了源文件、模块和构建目标），然后为 Xcode、Visual Studio、Linux Makefile 及其他构建系统生成原生 IDE 工程。

该工具负责 JUCE 模块管理，允许开发者添加、移除和配置提供音频处理、GUI 组件、网络等功能的框架模块。当项目文件变化时，**--resave** 会重新生成所有 IDE 文件以保持同步。

Projucer 既可作为图形化 IDE 用于交互式开发，也可作为命令行工具用于 CI/CD 自动化。CLI 模式支持创建新项目、重新生成构建文件以及查询项目状态，无需启动 GUI。

# CAVEATS

需要 JUCE 框架。专注于音频开发。下载体积较大。

# HISTORY

**Projucer** 是 **JUCE**（Jules' Utility Class Extensions）的一部分，这是 ROLI（现 PACE）旗下的音频应用框架。

# SEE ALSO

[cmake](/man/cmake)(1), [make](/man/make)(1)
