# TAGLINE

通用命令行启动器

# TLDR

**启动根视图**

```sunbeam```

按别名或路径**运行扩展**

```sunbeam run [extension] [command]```

从 URL 或本地路径**安装扩展**

```sunbeam extension install [origin]```

**列出已安装的扩展**

```sunbeam extension list```

根据 Sunbeam schema **校验脚本**

```sunbeam validate [manifest.json]```

在系统处理程序中**打开文件或 URL**

```sunbeam open [target]```

# SYNOPSIS

**sunbeam** [_command_] [_flags_]

# PARAMETERS

**run** _extension_ [_command_]
> 执行已安装扩展暴露的某个命令。

**extension install** _origin_
> 从 Git URL 或本地目录安装扩展。

**extension list**
> 显示已安装的扩展。

**extension remove** _alias_
> 卸载扩展。

**validate** _file_
> 检查清单或页面是否符合 Sunbeam JSON schema。

**open** _target_
> 用默认处理程序打开 URL 或文件。

**--help**
> 显示 sunbeam 或任意子命令的用法。

# DESCRIPTION

**sunbeam** 让你用任何语言编写的简单脚本来定义由一系列视图组成的 UI。它介于 Raycast 这类应用启动器和 fzf 这类模糊查找器之间，可以从你的脚本输出的 JSON 渲染出交互式列表、详情和表单。

扩展可以用 Shell、Python、TypeScript 或任何能向标准输出打印 JSON 的语言编写。Sunbeam 内置了 GitHub、Nix、Google 搜索、Hacker News 和 Pipe Boards 的集成，并能干净地嵌入 tmux 或 zellij 弹窗中。

# HISTORY

**sunbeam** 由 **pomdtr** 创建，使用 **Go** 编写，以 MIT 许可证发布。

# SEE ALSO

[fzf](/man/fzf)(1), [rofi](/man/rofi)(1), [television](/man/television)(1)
