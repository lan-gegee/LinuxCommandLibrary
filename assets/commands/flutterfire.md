# TAGLINE

在 Flutter 项目中设置 Firebase 的 CLI 工具

# TLDR

**配置 Firebase**

```flutterfire configure```

**重新配置特定平台**

```flutterfire configure --platforms=[android,ios]```

**使用特定项目进行配置**

```flutterfire configure --project=[firebase-project-id]```

**更新配置**

```flutterfire configure --yes```

# SYNOPSIS

**flutterfire** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作类型：configure、install。

**configure**
> 为 Flutter 项目设置 Firebase。

**--project** _ID_
> Firebase 项目 ID。

**--platforms** _LIST_
> 要配置的平台。

**--yes**
> 接受默认值而不提示。

**--out** _FILE_
> 输出配置文件的路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flutterfire** 是用于在 Flutter 项目中设置 Firebase 的 CLI 工具。它将配置流程自动化，生成各平台专用的文件和 Dart 代码。

该工具连接到你的 Firebase 项目并下载所选平台的配置。它会生成 firebase_options.dart，用于在 Flutter 应用中初始化 Firebase。

flutterfire 免去了手动复制配置文件的麻烦，并保证各平台之间的配置一致。

# CAVEATS

需要 Firebase CLI 并完成身份验证。Firebase 项目必须已经存在。每个目标平台都需要相应的平台 SDK。

# HISTORY

flutterfire 由 **FlutterFire** 团队创建，目的是简化 Flutter 应用中的 Firebase 集成。它用自动化设置取代了手动配置，覆盖所有受支持的平台。

# SEE ALSO

[flutter](/man/flutter)(1), [firebase](/man/firebase)(1)

# RESOURCES

```[Documentation](https://firebase.flutter.dev/)```

```[Source code](https://github.com/invertase/flutterfire_cli)```

<!-- verified: 2026-07-15 -->
