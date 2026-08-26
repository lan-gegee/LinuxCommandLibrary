# TAGLINE

列出、创建或删除数据库分支

# TLDR

**列出本地分支**

```dolt branch```

**列出全部分支**，包括远程跟踪分支

```dolt branch -a```

**从当前 HEAD 创建分支**

```dolt branch [name]```

**从指定起点创建分支**

```dolt branch [name] [start_point]```

**删除分支**

```dolt branch -d [name]```

**强制删除**未合并的分支

```dolt branch -D [name]```

**重命名当前分支**

```dolt branch -m [new_name]```

**复制分支**

```dolt branch -c [old_name] [new_name]```

**列出远程跟踪分支**

```dolt branch -r```

**显示当前分支**名称

```dolt branch --show-current```

**列出分支**并附带详细的提交信息

```dolt branch -v```

# SYNOPSIS

**dolt branch** [**--list**] [**-v**] [**-a**] [**-r**]
**dolt branch** [**-f**] _branchname_ [_start-point_]
**dolt branch** **-m** [**-f**] [_oldbranch_] _newbranch_
**dolt branch** **-c** [**-f**] [_oldbranch_] _newbranch_
**dolt branch** **-d** [**-f**] [**-r**] _branchname_...

# PARAMETERS

**-d**, **--delete**
> 删除分支。除非同时给出 **-f**，否则该分支必须已被完全合并。

**-D**
> **--delete --force** 的快捷写法。

**-m**, **--move**
> 重命名分支。

**-c**, **--copy**
> 将分支复制为一个新名称。

**-f**, **--force**
> 即使分支已存在也将其重置到指定起点；即使目标名称已存在也强制重命名/复制；或允许删除未合并的分支。

**-r**, **--remote**
> 列出远程跟踪分支或对其执行操作。

**-a**, **--all**
> 同时列出本地分支和远程跟踪分支。

**-v**, **--verbose**
> 显示每个分支的提交哈希和主题行。使用 **-vv** 还会显示上游分支名称。

**-t**, **--track**
> 为远程分支设置上游跟踪。

**--show-current**
> 打印当前活动分支的名称。

**--list**
> 显式进入列表模式。

_start-point_
> 新分支的起始提交引用。默认为当前 HEAD。

# DESCRIPTION

**dolt branch** 用于列出、创建或删除 Dolt 数据库仓库中的分支。分支的工作方式与 Git 分支类似，只是作用于版本化的数据库，让表结构和数据可以并行开发。

不带参数时，该命令列出所有本地分支，并用星号标记当前分支。创建分支会把当前的数据库状态保存下来，作为后续分叉开发的起点。注意：创建分支并不会切换过去；切换分支请使用 **dolt checkout**。

分支可用于测试表结构变更、试验数据变换，或者维护数据集的多个版本。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt-checkout](/man/dolt-checkout)(1), [dolt-merge](/man/dolt-merge)(1), [dolt-commit](/man/dolt-commit)(1), [dolt-status](/man/dolt-status)(1), [dolt](/man/dolt)(1)
