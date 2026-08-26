# TAGLINE

为最后一次提交添加共同作者署名

# TLDR

**为最后一次提交添加共同作者**

```git coauthor "[Name]" "[email@example.com]"```

**添加第二位共同作者**（对同一提交再次运行）

```git coauthor "[Name2]" "[email2@example.com]"```

# SYNOPSIS

**git coauthor** _name_ _email_

# PARAMETERS

_NAME_
> 共同作者的姓名。必填。

_EMAIL_
> 共同作者的邮箱。必填。

# DESCRIPTION

**git coauthor** 是一个 **git-extras** 命令，它会修改最后一次提交信息，添加 **Co-authored-by:** 尾注——这是 GitHub 和 GitLab 用来在同一个提交上署名多位贡献者的格式。

每次调用只接受一个姓名和一个邮箱。若要署名多人，请为每位共同作者各运行一次：由于它是在已有的 **Co-authored-by:** 尾注之后追加而非替换，对同一提交反复运行即可累积多位共同作者。

这支持结对编程、群体编程等协作工作流，让署名反映所有贡献者，而不仅仅是执行 **git commit** 的那个人。

# CAVEATS

属于 **git-extras** 软件包。它会修改最后一次提交并重写其哈希，因此不要对已推送到共享分支的提交使用。姓名和邮箱均为必填；该命令没有任何标志，也不校验参数。共同作者的邮箱必须与贡献者的平台账号一致，GitHub/GitLab 才能将署名关联到其个人主页。

# HISTORY

git coauthor 是社区维护的 Git 实用脚本合集 **git-extras** 的一部分，为支持 GitHub 的共同作者尾注约定、给协作成果署名而加入。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-commit](/man/git-commit)(1), [git-authors](/man/git-authors)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-coauthor)```

<!-- verified: 2026-07-17 -->
