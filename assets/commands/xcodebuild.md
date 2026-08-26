# TAGLINE

从命令行构建 Xcode 项目

# TLDR

**以默认设置构建项目**

```xcodebuild```

**构建指定的 scheme**

```xcodebuild -scheme [SchemeName]```

**针对指定 SDK**和目标设备构建

```xcodebuild -scheme [SchemeName] -sdk iphoneos -destination "generic/platform=iOS"```

**构建一个 workspace**

```xcodebuild -workspace [App.xcworkspace] -scheme [SchemeName]```

**创建归档**

```xcodebuild archive -scheme [SchemeName] -archivePath [path/to/App.xcarchive]```

**导出归档**为 IPA

```xcodebuild -exportArchive -archivePath [App.xcarchive] -exportPath [output] -exportOptionsPlist [options.plist]```

**运行测试**

```xcodebuild test -scheme [SchemeName] -destination "platform=iOS Simulator,name=iPhone 15"```

**列出可用的 scheme**

```xcodebuild -list```

**列出可用的 SDK**

```xcodebuild -showsdks```

# SYNOPSIS

**xcodebuild** [**-project** _name_] [**-workspace** _name_] [**-scheme** _name_] [**-target** _name_] [**-sdk** _sdk_] [**-destination** _dest_] [_action_...]

# PARAMETERS

**-project** _name_
> 构建由 name.xcodeproj 指定的项目。

**-workspace** _name_
> 构建由 name.xcworkspace 指定的 workspace。

**-scheme** _name_
> 构建具有指定名称的 scheme。workspace 必须提供此参数。

**-target** _name_
> 构建具有指定名称的 target。

**-sdk** _sdk_
> 使用指定的 SDK 构建（iphoneos、iphonesimulator、macosx）。

**-destination** _destination_
> 使用 destination 所描述的目标设备。

**-configuration** _config_
> 构建配置：Debug 或 Release。

**-archivePath** _path_
> 归档输出的路径。

**-exportPath** _path_
> 导出输出的路径。

**-exportOptionsPlist** _path_
> 指定导出选项的 plist 文件。

**-list**
> 列出所有 target、scheme 和配置。

**-showsdks**
> 列出所有可用的 SDK。

**-allowProvisioningUpdates**
> 允许自动管理描述文件。

**build**
> 构建 target（默认操作）。

**archive**
> 创建用于分发的归档。

**test**
> 运行单元测试。

**clean**
> 移除构建产物。

# DESCRIPTION

**xcodebuild** 是 Apple 用于构建 Xcode 项目和 workspace 的命令行工具。它执行构建、测试、归档和导出操作，是 CI/CD 流水线以及自动化构建 macOS、iOS、watchOS 和 tvOS 应用的关键工具。

该工具可用于项目（.xcodeproj）或 workspace（.xcworkspace）。workspace 通常与 CocoaPods 或 Swift Package Manager 一起使用，必须指定 scheme。scheme 定义要构建哪些 target 以及使用什么配置。

面向 iOS 分发的构建通常是两个步骤：先 **archive** 创建 .xcarchive，然后用导出选项 plist 执行 **-exportArchive** 生成最终的 .ipa 文件。代码签名和描述文件可通过 **-allowProvisioningUpdates** 自动管理。

# CAVEATS

需要安装 Xcode（仅有 Command Line Tools 不够）。如有需要可使用 `xcode-select -s` 切换开发者目录。归档和导出需要有效的代码签名身份和描述文件。模拟器目标设备需要已安装模拟器。

# HISTORY

**xcodebuild** 自 **Xcode** 早期版本起就一直是其组成部分，随 Apple 开发者工具一同演进。该工具的功能日益强大，陆续增加了对 workspace 的支持、用于模拟器和真机的 destination 描述符以及与 xcpretty 兼容的输出。它仍然是 iOS 和 macOS 持续集成系统的基础。

# INSTALL

```nix: nix profile install nixpkgs#xcodebuild```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xcrun](/man/xcrun)(1), [xcode-select](/man/xcode-select)(1), [codesign](/man/codesign)(1), [swift](/man/swift)(1)
