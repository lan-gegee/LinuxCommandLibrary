# TAGLINE

使用 Web 技术构建桌面应用

# TLDR

**初始化新的 Tauri 项目**

```tauri init```

**启动开发服务器**

```tauri dev```

**构建生产版本应用**

```tauri build```

**构建带调试符号的版本**

```tauri build --debug```

**为特定目标平台构建**

```tauri build --target [x86_64-apple-darwin]```

**构建指定的打包类型**

```tauri build --bundles [deb,appimage]```

**生成图标**

```tauri icon [icon.png]```

**显示版本**

```tauri --version```

# SYNOPSIS

**tauri** [_command_] [_options_]

**cargo tauri** [_command_] [_options_]

# COMMANDS

**init**：在现有目录中初始化新的 Tauri 项目。

**dev**：启动支持热重载的开发服务器。

**build**：构建生产版本应用包。

**icon**：从源图片生成图标。

**info**：显示环境诊断信息。

**add**：向项目添加 Tauri 插件。

**plugin**：插件开发相关命令。

**signer**：用于更新的签名工具。

**completions**：生成 Shell 补全脚本。

# PARAMETERS

**-v**, **--verbose**
> 启用详细日志输出。

**-d**, **--debug**
> 使用调试配置构建。

**-t**, **--target** _target_
> 目标三元组（例如 x86_64-unknown-linux-gnu）。

**-f**, **--features** _features_
> 要启用的 Rust 特性，以逗号分隔。

**-b**, **--bundles** _bundles_
> 打包类型：deb、rpm、appimage、msi、app、dmg、updater。

**-r**, **--runner** _runner_
> 使用的构建工具（默认为 cargo）。

**-c**, **--config** _file_
> tauri.conf.json 的路径或配置 JSON 字符串。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**tauri** 是用于构建 Tauri 应用的命令行界面。Tauri 是一个框架，可以使用 Web 技术（HTML、CSS、JavaScript）和 Rust 后端构建小巧、快速的桌面应用。

该 CLI 管理应用的完整生命周期：项目初始化、支持热重载的开发、生产环境构建以及发行版打包。它与前端构建流程集成，并处理特定平台的打包工作。

应用可以面向 Windows（MSI、NSIS）、macOS（DMG、应用包）和 Linux（DEB、RPM、AppImage）构建。该框架通过使用系统自带的 WebView 而非捆绑浏览器引擎，从而生成体积很小的二进制文件。

可通过 Cargo 安装：`cargo install tauri-cli`，或通过 npm 安装：`npm add -D @tauri-apps/cli`

# CAVEATS

需要 Rust 工具链和各平台的依赖（Linux 上需要 WebKitGTK、macOS 上需要 Xcode、Windows 上需要 WebView2）。交叉编译存在限制。通用 macOS 构建需要同时安装 ARM 和 Intel 两个目标平台。

# HISTORY

**Tauri** 作为 Electron 的轻量替代方案而诞生，使用系统 WebView 而非捆绑 Chromium。1.0 版本于 2022 年发布，2.0 版本增加了对移动平台的支持。该项目由 Commons Conservancy 内的 Tauri Program 维护。

# SEE ALSO

[cargo](/man/cargo)(1), [npm](/man/npm)(1), [electron](/man/electron)(1)
