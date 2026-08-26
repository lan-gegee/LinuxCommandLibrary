# TAGLINE

从命令行搜索并下载 iOS App Store 的 IPA 软件包

# TLDR

**登录** App Store

```ipatool auth login```

**显示**当前账户信息

```ipatool auth info```

**搜索**应用

```ipatool search "[term]"```

按 bundle 标识符**下载**应用

```ipatool download -b [com.example.app]```

**购买**应用（若下载前需要）

```ipatool purchase -b [com.example.app]```

用于脚本的 **JSON 输出**

```ipatool search "[term]" --format json```

# SYNOPSIS

**ipatool** *command* [*options*]

# DESCRIPTION

**ipatool** 是 iOS（及 tvOS）App Store 的命令行客户端。通过 Apple ID 凭据完成身份验证后，你可以搜索商店、在需要时购买应用，并下载用于设备或工具链工作流的 **.ipa** 软件包。它常用于自动化、归档和逆向工程研究——并非手机上官方 App Store 安装的替代品。

全局选项控制输出格式和交互性。子命令涵盖 **auth**、**search**、**download**、**purchase** 及相关操作；运行 **ipatool** *command* **--help** 可查看完整的选项。

# PARAMETERS

**auth login** | **auth info** | **auth revoke**

> 管理 App Store 会话凭据。

**search** *term*

> 搜索 iOS/tvOS 应用。**-l**, **--limit** 限制结果数量；**--platform** 选择 **iphone**、**ipad** 或 **appletv**。

**download**

> 下载 IPA（通常配合 **-b** / **--bundle-identifier**）。版本与输出选项见 **--help**。

**purchase**

> 购买应用，使其可被当前账户下载。

**--format** *text*|*json*

> 输出格式（默认：text）。

**--non-interactive**

> 不进行提示；若需要输入则直接失败。

**--verbose**

> 详细日志输出。

**-h**, **--help**

> 显示命令或子命令的帮助。

# CAVEATS

需要有效的 Apple ID 并遵守 Apple 条款。某些应用有地区限制、收费或拒绝批量下载。以此方式获取的 IPA 在没有额外签名工具的情况下无法直接侧载到未越狱的 iOS 设备。不得用于盗版。

# INSTALL

```brew: brew install ipatool```

```nix: nix profile install nixpkgs#ipatool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinstaller](/man/ideviceinstaller)(1), [ios-deploy](/man/ios-deploy)(1)

# RESOURCES

```[Source code](https://github.com/majd/ipatool)```

<!-- verified: 2026-07-19 -->
