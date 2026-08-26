# TAGLINE

简单的命令行任务管理

# TLDR

**添加任务**

```todo add "[task description]"```

**列出任务**

```todo list```

**完成任务**

```todo done [id]```

**移除任务**

```todo rm [id]```

**显示任务**

```todo show [id]```

**清除已完成项**

```todo clear```

# SYNOPSIS

**todo** _command_ [_options_] [_args_]

# PARAMETERS

**add**
> 添加任务。

**list**
> 显示任务。

**done**
> 标记为完成。

**rm**
> 移除任务。

**show**
> 显示详情。

**clear**
> 移除已完成项。

# DESCRIPTION

**todo** 是一款简单的命令行任务管理器，用于创建、列出、完成和移除任务。它提供极简的界面，便于快速录入任务和跟踪进度，没有全功能项目管理工具的复杂性。

存在多个以 "todo" 命名的实现，各自的功能和存储后端略有不同。核心工作流程是一致的：添加带描述的任务，完成时标记为 done，并从列表中清除已完成的条目。

# CAVEATS

存在多个名为 todo 的工具。请检查安装的是哪一个。功能各有差异。

# HISTORY

命令行任务管理领域存在多种 **todo** 实现，各自的功能略有不同。

# INSTALL

```apt: sudo apt install devtodo```

```pacman: sudo pacman -S todoman```

```apk: sudo apk add todoman```

```brew: brew install todoman```

```nix: nix profile install nixpkgs#devtodo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[task](/man/task)(1), [todo.sh](/man/todo.sh)(1), [todoman](/man/todoman)(1)
