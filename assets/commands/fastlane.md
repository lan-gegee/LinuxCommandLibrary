# TAGLINE

iOS 和 Android 应用自动化工具

# TLDR

**初始化 Fastlane**

```fastlane init```

**运行一个 lane**

```fastlane [lane_name]```

**构建并测试 iOS 应用**

```fastlane ios test```

**部署到 App Store**

```fastlane release```

**部署到 TestFlight**

```fastlane beta```

**列出可用 action**

```fastlane actions```

**列出可用 lane**

```fastlane lanes```

# SYNOPSIS

**fastlane** [_options_] [_lane_]

# SUBCOMMANDS

**init**
> 初始化 Fastlane。

**lanes**
> 列出所有 lane。

**actions**
> 列出所有 action。

**env**
> 打印环境信息。

**new_action**
> 创建新 action。

**docs**
> 生成文档。

# PARAMETERS

**--verbose**
> 启用详细输出。

**--env** _environment_
> 加载特定环境的配置。

# CONFIGURATION

**./fastlane/Fastfile**
> 主配置文件，定义用于构建、测试和部署自动化的 lane（工作流）。

**./fastlane/Appfile**
> 应用特定配置，包括 bundle identifier 和 Apple ID。

# DESCRIPTION

**fastlane** 自动化处理 iOS 和 Android 开发任务，包括构建、测试、代码签名，以及将应用发布到 App Store 和 Google Play。

该工具提供基于 Ruby 的 DSL 来定义工作流（称为 "lane"），将多个 action 串联起来。它可处理证书管理、截图生成、beta 分发和应用商店提交等复杂任务。

fastlane 与 xcodebuild、Gradle、gym、match、deliver 等工具集成，为移动开发和发布流程提供端到端的自动化。

# INSTALL

```brew: brew install fastlane```

```nix: nix profile install nixpkgs#fastlane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xcodebuild](/man/xcodebuild)(1), [gradle](/man/gradle)(1)

# RESOURCES

```[Source code](https://github.com/fastlane/fastlane)```

```[Homepage](https://fastlane.tools/)```

<!-- verified: 2026-07-15 -->
