# TAGLINE

Avo 分析埋点计划平台的命令行工具

# TLDR

在当前文件夹**初始化** Avo 工作区

```avo init```

从你的 Avo 工作区**拉取**分析包装代码

```avo pull```

**拉取**指定的 source

```avo pull [source_name]```

**检查**实现状态

```avo status```

**切换**到另一个 Avo 分支

```avo checkout [branch]```

将 Avo 的 main 分支**合并**到当前分支

```avo merge main```

**登录** Avo 平台

```avo login```

# SYNOPSIS

**avo** _command_ [_options_]

# PARAMETERS

**init**
> 在当前文件夹初始化一个 Avo 工作区。

**pull** [_source_]
> 从你的 Avo 工作区拉取分析包装代码。

**checkout** _branch_
> 切换到另一个 Avo 分支。

**source** _command_
> 管理当前项目的 source。

**status** [_source_]
> 显示 Avo 实现的状态。

**merge main**
> 将 Avo 的 main 分支拉取到你的当前分支。

**conflict**
> 解决 Avo 文件中的 git 冲突。

**edit**
> 在浏览器中打开 Avo 工作区。

**login**
> 登录 Avo 平台。

**logout**
> 退出 Avo 平台。

**whoami**
> 显示当前登录的用户名。

**-v**, **--verbose**
> 输出更详细的信息。

**-f**, **--force**
> 当传入分支处于打开状态时仍继续合并。

**--version**
> 显示版本号。

**--help**
> 显示帮助。

# DESCRIPTION

**avo** 是 Avo 分析埋点计划平台的命令行界面。它让你把类型安全的分析包装代码（codegen）从 Avo 工作区直接拉取到项目中，确保分析实现与埋点计划保持一致。

主要工作流是运行 `avo pull`，根据你在 avo.app 上定义的埋点计划获取最新生成的分析代码。首次运行时，它会提示你选择要为其生成代码的 Avo source 以及保存位置。此配置存储在 **avo.json** 文件中。

# CAVEATS

需要 Node.js >= 14.16。拉取前必须先通过 `avo login` 完成认证。配置存储在项目根目录的 avo.json 中。

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1)
