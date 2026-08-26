# TAGLINE

创建带有元数据的新 GitHub issue

# TLDR

**以交互方式创建 issue**

```gh issue create```

**带标题和正文创建**

```gh issue create -t "[title]" -b "[body]"```

**从文件读取正文**（用 - 表示标准输入）

```gh issue create -t "[title]" -F [body.md]```

**打开编辑器**撰写 issue

```gh issue create -e```

**添加标签和负责人**

```gh issue create -t "[title]" -l [bug] -l [urgent] -a [@me]```

**按名称使用 issue 模板**

```gh issue create -T "[Bug report]"```

**面向指定仓库**

```gh issue create -R [owner/repo] -t "[title]"```

**打开浏览器表单**

```gh issue create -w```

# SYNOPSIS

**gh** **issue** **create** [_options_]

# PARAMETERS

**-t**, **--title** _string_
> Issue 标题。省略时会提示输入。

**-b**, **--body** _string_
> Issue 正文。省略时会提示输入。

**-F**, **--body-file** _file_
> 从文件读取正文。用 `-` 表示从标准输入读取。

**-e**, **--editor**
> 跳过提示，打开 `$EDITOR` 来撰写标题和正文。

**-l**, **--label** _name_
> 按名称添加标签。可重复使用。

**-a**, **--assignee** _login_
> 按 login 指派用户。`@me` 表示指派给自己。可重复使用。

**-m**, **--milestone** _name_
> 按名称设置里程碑。

**-p**, **--project** _title_
> 按标题将 issue 添加到项目。可重复使用。

**-T**, **--template** _name_
> 按名称使用 issue 模板。

**--recover** _file_
> 从上次失败的运行中恢复已输入的内容。

**-w**, **--web**
> 打开浏览器来创建 issue。

**-R**, **--repo** _[HOST/]OWNER/REPO_
> 指定目标仓库。

# DESCRIPTION

**gh issue create** 在 GitHub 上创建新 issue，支持丰富的元数据。不带标志时，会通过交互式提示依次填写标题、正文、标签、负责人和项目归属。使用标志时，所有字段都可以非交互方式提供，便于在脚本和 CI 中使用。

仓库上配置的 issue 模板可通过 **-T/--template** 按名称选择；模板正文将作为起始文本。**-F/--body-file** 便于把其他工具的输出（例如生成的缺陷报告）直接管道传给新 issue。别名 `gh issue new` 与之等价。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-issue](/man/gh-issue)(1)
