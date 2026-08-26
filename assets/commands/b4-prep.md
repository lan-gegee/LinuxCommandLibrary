# TAGLINE

准备并管理待提交的补丁系列

# TLDR

**为系列新建跟踪分支**

```b4 prep -n [topical-branch-name]```

**将当前分支纳入 b4 管理**

```b4 prep -e [base-branch]```

**基于先前发布的系列创建新分支**

```b4 prep -F [message-id]```

**在编辑器中编辑 cover letter**

```b4 prep --edit-cover```

**根据维护者和 git 历史自动填充 To 和 Cc**

```b4 prep --auto-to-cc```

**对系列运行提交前检查**

```b4 prep --check```

# SYNOPSIS

**b4** **prep** [_options_]

# DESCRIPTION

**b4 prep** 将补丁系列建立为一个专用的、由 b4 跟踪的 git 分支并加以维护。创建或登记分支之后，你可以照常添加提交，并用 **git rebase -i** 重排或修改它们；b4 会把 cover letter 和系列元数据保存在分支内部，让各修订版随代码一同保留版本记录。

它可以根据 MAINTAINERS 文件和提交历史自动构建收件人列表，按照项目约定检查系列，并把整理好的系列交给 **b4 send** 发送。每次发布时 b4 都会记录修订号，保证后续提交的编号正确。

# PARAMETERS

**-n** _NAME_, **--new** _NAME_
> 为系列创建名为 _NAME_ 的新 b4 跟踪分支。

**-f** _POINT_, **--fork-point** _POINT_
> 创建新分支时，使用 _POINT_ 作为分叉点。

**-e** _[BRANCH]_, **--enroll** _[BRANCH]_
> 登记现有分支交由 b4 管理，并以 _BRANCH_ 作为跟踪基准。

**-F** _MSGID_, **--from-thread** _MSGID_
> 用先前发布的系列填充新分支。

**--edit-cover**
> 在编辑器中打开 cover letter。

**--show-revision**
> 显示该系列当前的跟踪修订号。

**--force-revision** _N_
> 强制将系列设为修订号 _N_。

**--auto-to-cc**
> 根据维护者信息和 git 历史收集 To 和 Cc 收件人。

**--check**
> 对该系列运行 b4 及项目自带的检查。

**--cleanup** _[BRANCH]_
> 归档并移除已完成任务的 prep 跟踪分支。

# INSTALL

```dnf: sudo dnf install b4```

```pacman: sudo pacman -S b4```

```apk: sudo apk add b4```

```zypper: sudo zypper install b4```

```brew: brew install b4```

```nix: nix profile install nixpkgs#b4```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b4](/man/b4)(1), [b4-send](/man/b4-send)(1), [git-rebase](/man/git-rebase)(1)

# RESOURCES

```[Documentation](https://b4.docs.kernel.org/)```

<!-- verified: 2026-06-10 -->
