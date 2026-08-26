# TAGLINE

对 git 暂存文件运行 linter

# TLDR

**对暂存文件运行**

```npx lint-staged```

**使用配置文件运行**

```npx lint-staged --config [.lintstagedrc.json]```

**以调试模式运行**

```npx lint-staged --debug```

**试运行（不做更改）**

```npx lint-staged --dry-run```

**对两个分支之间变更的文件运行**

```npx lint-staged --diff="[branch1]...[branch2]"```

**带详细输出运行**

```npx lint-staged --verbose```

# SYNOPSIS

**lint-staged** [_options_]

# PARAMETERS

**--config**, **-c** _file_
> 配置文件路径或 npm 包名。

**--debug**, **-d**
> 启用调试模式。

**--dry-run**
> 显示将要执行的操作但不实际执行。

**--diff** _ref_
> 覆盖 git diff 默认的 --staged 标志来获取文件列表。

**--diff-filter** _filter_
> 覆盖 git diff 默认的 --diff-filter=ACMR。

**--concurrent**, **-p** _number_
> 控制任务的并发度（默认：true 表示并行）。

**--no-stash**
> 禁用创建备份 stash，将修改保留在索引中。

**--hide-unstaged**
> 在运行任务前隐藏已跟踪文件的未暂存更改。

**--quiet**, **-q**
> 抑制任务之外的所有 CLI 输出。

**--relative**, **-r**
> 向任务传递相对于 process.cwd() 的文件路径。

**--verbose**
> 即使任务成功也显示任务输出。

**--allow-empty**
> 当任务撤销了所有暂存的更改时，允许创建空的 git 提交。

**--cwd** _dir_
> 在指定目录中运行所有任务。

**--max-arg-length** _number_
> 覆盖生成的命令字符串的最大长度。

# DESCRIPTION

**lint-staged** 对 git 暂存文件运行 linter。它通常与 husky 或 lefthook 配合使用，只对变更的文件运行格式化器和 linter，从而在提交前保证代码质量。

由于避免了对整个代码库进行 lint，pre-commit 钩子因此变得更快。

# CONFIGURATION

```json
// package.json
{
  "lint-staged": {
    "*.js": ["eslint --fix", "prettier --write"],
    "*.css": "stylelint --fix"
  }
}
```

# CAVEATS

需要 git 仓库。运行期间会 stash 未暂存的更改。可能与部分暂存冲突。与支持自动修复的 linter 配合效果最佳。

# HISTORY

lint-staged 由 **Andrey Okonetchnikov** 于 **2016 年**创建，通过只针对暂存文件来解决 pre-commit 钩子过慢的问题。

# INSTALL

```nix: nix profile install nixpkgs#lint-staged```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[husky](/man/husky)(1), [eslint](/man/eslint)(1), [prettier](/man/prettier)(1), [lefthook](/man/lefthook)(1)
