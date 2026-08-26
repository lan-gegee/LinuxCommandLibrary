# TAGLINE

管理 TeX Live 软件包仓库

# TLDR

**列出仓库**

```tlmgr repository list```

**添加仓库**

```tlmgr repository add [url] [tag]```

**移除仓库**

```tlmgr repository remove [url]```

**设置整个仓库列表**（替换所有现有条目）

```tlmgr repository set [url#tag] [url#tag ...]```

**检查仓库的验证状态**

```tlmgr repository status```

# SYNOPSIS

**tlmgr repository** _action_ [_options_]

# PARAMETERS

**list** [_path|url|tag_]
> 列出已配置的仓库及其标签。如果给定了路径、URL 或标签，则从该来源初始化 TL 数据库并列出其中的软件包。

**list** **--with-platforms**
> 额外列出每个软件包可用的平台。

**add** _path_ [_tag_]
> 添加仓库，可选择附加一个标签以便引用。

**remove** _path|tag_
> 通过完整路径/URL 或标签移除仓库。

**set** _path_[**#**_tag_] [_path_[**#**_tag_] ...]
> 用指定条目替换整个仓库列表。必须有一个仓库标记为 **main**。

**status**
> 报告已加载仓库的验证状态（标签、URL 和验证状态）。

# DESCRIPTION

**tlmgr repository** 管理 TeX Live 软件包仓库列表。它允许配置 CTAN 镜像和额外的软件包来源。必须始终有一个仓库标记为 **main**；否则操作会失败。TeX Live Manager 的组成部分。

# CAVEATS

**set** 操作会替换之前配置的所有仓库。必须有一个仓库标记为 **main**，否则操作将失败。仓库验证依赖可用的 GnuPG（gpg）二进制文件。

# SEE ALSO

[tlmgr-update](/man/tlmgr-update)(1), [tlmgr](/man/tlmgr)(1), [tlmgr-conf](/man/tlmgr-conf)(1), [tlmgr-install](/man/tlmgr-install)(1)
