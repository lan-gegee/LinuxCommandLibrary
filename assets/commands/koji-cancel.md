# TAGLINE

取消 Koji 构建系统上正在运行的一个或多个活动任务

# TLDR

按 **ID 取消**任务

```koji cancel [task_id]```

取消**多个任务**

```koji cancel [task_id1] [task_id2]```

按 NVR 或构建 ID 取消**构建**

```koji cancel [package-1.0-1.fc38]```

取消**整个任务树**（任务及其全部后代）

```koji cancel --full [task_id]```

对非本人拥有的任务**强制**取消（仅管理员）

```koji cancel --force [task_id]```

# SYNOPSIS

**koji cancel** [_options_] _task_id_ [_task_id_...]

# DESCRIPTION

**koji cancel** 取消 Koji 构建系统上正在运行的一个或多个活动任务。只有处于可取消状态（等待中或运行中）的任务才能被此命令成功取消。

# PARAMETERS

**task_id**
> 数字任务 ID，或构建 NVR / 构建 ID（可指定多个）。

**--justone**
> 只取消任务本身，不取消其后代子任务。

**--full**
> 取消任务及其全部后代（完整任务树）。

**--force**
> 允许管理员取消其他用户拥有的任务。

**-h, --help**
> 显示帮助信息。

# CAVEATS

只能停止用户自己拥有的任务或用户有权取消的任务。已完成的任务无法取消。

# SEE ALSO

[koji](/man/koji)(1), [koji-build](/man/koji-build)(1)
