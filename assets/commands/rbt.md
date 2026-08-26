# TAGLINE

Review Board 代码评审的命令行客户端

# TLDR

**为未提交的更改创建评审请求**

```rbt post```

**为特定提交创建**评审请求

```rbt post [revision]```

**更新已有的评审请求**

```rbt post -u```

**按 ID 更新特定的**评审请求

```rbt post -r [review_request_id]```

**应用评审请求中的补丁**

```rbt patch [review_request_id]```

**显示评审请求的状态**

```rbt status```

**落地已评审的更改**（合并并关闭）

```rbt land [review_request_id]```

# SYNOPSIS

**rbt** _command_ [_options_] [_arguments_]

# PARAMETERS

**post**
> 用本地更改创建或更新评审请求

**patch**
> 将评审请求中的 diff 应用到本地代码树

**land**
> 落地已评审的更改（提交、推送并关闭评审）

**status**
> 显示待处理的评审请求及其状态

**diff**
> 打印将要上传评审的 diff

**close**
> 关闭评审请求（已提交或已丢弃）

**setup-repo**
> 为 RBTools 配置仓库

**--server** _URL_
> 指定 Review Board 服务器的 URL

**-r**, **--review-request-id** _ID_
> 指定要更新的评审请求 ID

**-u**, **--update**
> 更新最近一个匹配的评审请求

**--publish**
> 立即发布评审请求

**-d**, **--debug**
> 启用调试输出

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rbt** 是 Review Board 的命令行客户端。Review Board 是一款基于 Web 的代码评审工具。它可以在终端中自动创建、更新和管理代码评审请求，并与 Git、Mercurial、SVN、Perforce、CVS 等版本控制系统集成。

最常见的流程是先用 **rbt post** 上传待评审的更改，再用 **rbt land** 合并通过评审的更改。该工具会自动生成 diff 并检测仓库配置，尽量减少手动操作。

配置通常保存在仓库根目录的 **.reviewboardrc** 文件中，包含服务器 URL 和仓库设置，便于团队成员共享一致的配置。

# CONFIGURATION

**.reviewboardrc**
> 每个仓库一份的配置文件，指定 Review Board 服务器 URL、仓库名称以及评审请求的默认设置。

**REVIEWBOARD_URL**
> 指定 Review Board 服务器 URL 的环境变量，可替代 .reviewboardrc。

# CAVEATS

需要 Python 3.7+ 和一台已配置好的 Review Board 服务器。必须通过 **--server**、环境变量或 .reviewboardrc 文件指定服务器 URL。

在发布评审之前，必须先用 **rbt setup-repo** 或手动编辑 .reviewboardrc 正确配置仓库。

凭据通常通过系统钥匙串保存，也可以交互式输入。避免将凭据以明文形式存储在配置文件中。

# HISTORY

RBTools 是 Review Board 项目的一部分，由 VMware 的 **Christian Hammond** 和 **David Trowbridge** 创建。Review Board 于 **2007 年**首次发布，是一款旨在简化同行评审流程的开源代码评审工具。大约在 Review Board 2.0 时，rbt 命令取代了早期的 post-review 脚本。

# INSTALL

```apk: sudo apk add rbtools```

```brew: brew install rbtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [hg](/man/hg)(1), [svn](/man/svn)(1), [diff](/man/diff)(1)
