# TAGLINE

 带模板和本地基础设施图的分层式 AWS CLI

# TLDR

**列出** EC2 实例

```awless list instances```

通过 **SSH** 连接实例（智能 SSH）

```awless ssh [instance-id-or-name]```

**运行**一个创建型模板

```awless run [template.awless]```

**同步**账户的本地关系图

```awless sync```

# SYNOPSIS

**awless** *command* [*args*]

# DESCRIPTION

**awless** 是一款替代的 AWS CLI，专注于精简的分层命令集、基础设施模板化、用于离线浏览的本地关系图同步，以及"智能 SSH"连接实例。它会记录修改云端资源的操作，便于审查/回滚工作流。可通过 GitHub releases 或软件包管理器安装。

# PARAMETERS

**list** *resources*

> 列出某一类型的 AWS 资源。

**create** / **delete** / **update**

> 修改类操作（务必谨慎确认）。

**run** *template*

> 执行一个 awless 模板。

**ssh** *target*

> 使用自动发现的连接详情进行连接。

**sync**

> 刷新本地基础设施关系图。

认证使用标准的 AWS 凭证/区域配置。

# CAVEATS

项目活跃度可能落后于官方 **aws** CLI 的功能——请对照当前的 AWS API 加以验证。创建资源的模板会产生费用。建议使用最小权限的 IAM 凭证。

# INSTALL

```aur: yay -S awless```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [saws](/man/saws)(1)

# RESOURCES

```[Source code](https://github.com/wallix/awless)```

<!-- verified: 2026-07-19 -->
