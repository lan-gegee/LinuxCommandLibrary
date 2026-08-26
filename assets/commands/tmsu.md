# TAGLINE

基于标签的文件组织系统

# TLDR

**为文件打标签**

```tmsu tag [file] [tag1] [tag2]```

**列出标签**

```tmsu tags```

**按标签查找**

```tmsu files [tag]```

**按多个标签查找**（布尔查询）

```tmsu files [tag1] and [tag2]```

**移除文件的标签**

```tmsu untag [file] [tag]```

**挂载按标签组织的虚拟文件系统**

```tmsu mount [mountpoint]```

**显示特定文件**的标签

```tmsu tags [file]```

**检查**已标记文件的**状态**

```tmsu status```

# SYNOPSIS

**tmsu** _command_ [_options_] [_args_]

# PARAMETERS

**tag**
> 为文件或目录添加标签。

**tags** [_file_]
> 列出所有标签，或列出特定文件的标签。

**files** _query_
> 查询匹配标签表达式的文件（支持 and、or、not）。

**untag**
> 移除文件的标签。

**mount** _mountpoint_
> 挂载一个按标签组织的 FUSE 虚拟文件系统。

**rename** _old_ _new_
> 重命名标签。

**delete** _tag_
> 删除标签及其所有文件关联。

**merge** _tags_ _target_
> 将多个标签合并为一个标签。

**status**
> 列出文件的标记状态（已标记、已修改、缺失）。

# DESCRIPTION

**tmsu**（Tag My Stuff Unix）是一款文件标记工具，让你通过赋予任意标签来组织文件，而不必完全依赖目录层级。标签和文件关联存储在本地 SQLite 数据库中，实际文件保持不变。

可以使用带布尔运算符（and、or、not）的标签表达式查询文件，轻松找到符合特定条件的文件。**mount** 命令提供一个 FUSE 虚拟文件系统，其中被标记的文件按标签组织成目录，可与标准文件管理工具配合使用。

# CAVEATS

挂载需要 FUSE。每个目录一个数据库。基于 Go 的工具。

# HISTORY

**TMSU**（Tag My Stuff Unix）为使用标签进行文件整理而创建，并可选支持 FUSE 文件系统。

# INSTALL

```nix: nix profile install nixpkgs#tmsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [locate](/man/locate)(1)
