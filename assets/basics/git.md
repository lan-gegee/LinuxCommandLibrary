# Git

## 入门
先告诉 git 你是谁；姓名和邮箱会被记录在你创建的每个提交中。
```[git](/man/git) config --global user.name "Your Name"```
```[git](/man/git) config --global user.email "you@example.com"```

在当前目录新建一个仓库，或者克隆一个现有仓库。
```[git](/man/git) init```
```[git](/man/git) clone [url]```

## 日常流程
改动分两步入库：**add** 把它们放入暂存区，**commit** 把暂存的改动变成一个永久快照。**status** 用于查看当前的全部状态。
```[git](/man/git) status```
```[git](/man/git) add [file]```
```[git](/man/git) add .```
```[git](/man/git) commit -m "describe the change"```

以交互方式逐块（hunk）暂存：适合只提交部分改动的情况。
```[git](/man/git) add -p```

与远程仓库交换提交。**pull** 相当于 **fetch**（下载）加 **merge** 一步完成。
```[git](/man/git) push```
```[git](/man/git) pull```

## 分支
分支是指向提交的低成本指针。**switch** 用于切换分支，**-c** 用于创建分支；较老的 **checkout** 一条命令兼顾两项工作。
```[git](/man/git) branch```
```[git](/man/git) branch -a```
```[git](/man/git) switch [branchName]```
```[git](/man/git) switch -c [newBranch]```
```[git](/man/git) checkout -b [newBranch]```

将另一个分支合并到当前分支。
```[git](/man/git) merge [branchName]```

删除本地和远程的分支。**-d** 拒绝删除未合并的工作；**-D** 强制删除。
```[git](/man/git) branch -d [branchName]```
```[git](/man/git) branch -D [branchName]```
```[git](/man/git) push origin --delete [branchName]```

## 查看历史
```[git](/man/git) log```
```[git](/man/git) log --oneline --graph --all```
```[git](/man/git) show [commitHash]```
```[git](/man/git) blame [fileName]```

单独使用 **diff** 显示未暂存的改动；**--staged** 显示下次提交将包含的内容。
```[git](/man/git) diff```
```[git](/man/git) diff --staged```
```[git](/man/git) diff [branch1]..[branch2]```

## 撤销操作
丢弃文件未提交的改动，或将文件移出暂存区而不丢失改动。
```[git](/man/git) restore [fileName]```
```[git](/man/git) restore --staged [fileName]```

修补最近一次提交（提交信息或遗漏的文件），或通过创建一个反向的新提交来安全地撤销某次提交。
```[git](/man/git) commit --amend```
```[git](/man/git) revert HEAD```

**reset** 将分支指针回移。**--soft** 把你的改动保留在暂存区，**--hard** 则将其丢弃。
```[git](/man/git) reset --soft HEAD~1```
```[git](/man/git) reset --hard HEAD~1```

**revert** 在共享分支上是安全的，因为它只是新增一个提交。**reset --hard** 和 **--amend** 会改写历史：不要对已经推送过的提交使用它们。

让已写入 .gitignore 但此前被提交过的文件停止被跟踪。
```[git](/man/git) rm -r --cached .```
```[git](/man/git) add .```
```[git](/man/git) commit -m "remove ignored files"```

## 贮藏
把未提交的工作暂存到一边，得到干净的工作目录，之后再取回。**-u** 会包含未跟踪的文件。
```[git](/man/git) stash -u```
```[git](/man/git) stash list```
```[git](/man/git) stash pop```
```[git](/man/git) stash apply```

**pop** 应用贮藏并将其从列表中移除；**apply** 应用后仍保留贮藏，适合把同一份工作应用到多个分支的情况。

## 标签
标签用于标记特定的提交，通常是发布版本。附注标签（**-a**）会保存作者、日期和说明信息。
```[git](/man/git) tag [tagName]```
```[git](/man/git) tag -a v1.0 -m "release 1.0"```
```[git](/man/git) tag -d [tagName]```
```[git](/man/git) push --tags```

标签默认不会被推送。需要显式推送：使用 **--tags** 或 **git push origin [tagName]**。

## 远程
远程是仓库另一份副本的命名 URL；**origin** 是主远程的惯用名称。
```[git](/man/git) remote -v```
```[git](/man/git) remote add [remoteName] [remoteURL]```
```[git](/man/git) fetch [remoteName]```
```[git](/man/git) pull [remoteName] [branchName]```

**push -u** 将本地分支与远程分支关联起来，之后 **git push** 和 **git pull** 无需参数即可使用。
```[git](/man/git) push -u [remoteName] [branchName]```

## 改写历史
**rebase** 把你的提交重新播放到另一个分支之上，形成线性历史；**cherry-pick** 将单个提交复制到当前分支。
```[git](/man/git) rebase [branchName]```
```[git](/man/git) rebase -i HEAD~3```
```[git](/man/git) cherry-pick [commitHash]```

交互式 rebase（**-i**）让你重排、压缩和改写提交说明。与 **reset** 一样，绝不要 rebase 其他人可能已经拉取过的提交。

## 获取帮助
```[git](/man/git) help [command]```
```[git](/man/git) help -g```
