# TAGLINE

IntelliJ IDEA 的命令行启动器

# TLDR

**打开项目**

```idea [project-directory]```

**打开文件**

```idea [file.java]```

**定位到指定行打开**

```idea --line [42] [file.java]```

**比较文件**

```idea diff [file1] [file2]```

**合并文件**

```idea merge [local] [remote] [base] [output]```

**等待 IDE 关闭**（用作 $EDITOR）

```idea --wait [file]```

**按项目代码风格格式化文件**

```idea format -r -s [code-style.xml] [src/]```

**无头运行代码检查**

```idea inspect [project_dir] [inspection-profile.xml] [out_dir]```

# SYNOPSIS

**idea** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的文件或项目。

**--line** _NUM_
> 打开文件并将光标置于指定行号。

**--column** _NUM_
> 定位到指定列（与 **--line** 组合使用）。

diff _file1_ _file2_
> 打开差异查看器，比较两个文件。

merge _local_ _remote_ _base_ _output_
> 打开三方合并工具。

format [_options_] _files_
> 以非交互方式对一个或多个文件应用项目代码风格格式化。

inspect _project_ _profile_ _output_
> 对项目进行无头代码检查，并将报告写入 _output_。

installPlugins _id_...
> 按 ID 从 JetBrains Marketplace 或自定义仓库安装插件。

**--wait**
> 阻塞直到所打开的文件被关闭（适合用作 **$EDITOR**）。

nosplash
> 启动时跳过闪屏。

dontReopenProjects
> 显示欢迎界面，而不是重新打开上次的项目。

disableNonBundledPlugins
> 仅使用内置插件启动；有助于排查问题。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idea** 是 IntelliJ IDEA 的命令行启动器。它可以从终端打开文件、项目并调用 IDE 功能。

该工具支持 diff、merge 和项目导航。可与 git 及其他需要编辑器的工具集成。

# CAVEATS

需要已安装 IntelliJ IDEA。需要配置路径。资源占用较高。

# HISTORY

idea 是 **JetBrains IntelliJ IDEA** 的 CLI 启动器，后者是一款流行的 Java IDE。

# SEE ALSO

[code](/man/code)(1), [webstorm](/man/webstorm)(1), [vim](/man/vim)(1)
