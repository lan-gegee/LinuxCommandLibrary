# TAGLINE

保存和恢复 Vagrant 虚拟机状态

# TLDR

**保存快照**

```vagrant snapshot save [name]```

**恢复快照**

```vagrant snapshot restore [name]```

**列出快照**

```vagrant snapshot list```

**删除快照**

```vagrant snapshot delete [name]```

**快速保存**

```vagrant snapshot push```

# SYNOPSIS

**vagrant** **snapshot** _command_ [_options_]

# PARAMETERS

**save** _name_
> 创建命名快照。

**restore** _name_
> 恢复到快照。

**list**
> 列出快照。

**delete** _name_
> 移除快照。

**push**
> 快速保存（未命名）。

**pop**
> 恢复并删除最近一次 push 的快照。

# DESCRIPTION

**vagrant snapshot** 管理虚拟机快照。保存并恢复虚拟机状态，用于测试和开发。支持命名快照以及快速的 push/pop 操作。

# SEE ALSO

[vagrant](/man/vagrant)(1)
