# TAGLINE

用 Go 编写的快速而强大的 Git 钩子管理器

# TLDR

**安装 git 钩子**

```lefthook install```

**添加钩子配置**

```lefthook add pre-commit```

**手动运行钩子**

```lefthook run pre-commit```

**卸载钩子**

```lefthook uninstall```

**生成示例配置**

```lefthook dump```

# SYNOPSIS

**lefthook** _command_ [_options_]

# PARAMETERS

**install**
> 安装 lefthook 的 git 钩子。

**uninstall**
> 移除 lefthook 的 git 钩子。

**add** _hook_
> 为某个钩子添加配置。

**run** _hook_
> 手动运行某个钩子。

**dump**
> 打印合并后的配置。

**version**
> 显示版本信息。

# DESCRIPTION

**lefthook** 是一个用 Go 编写的快速而强大的 Git 钩子管理器。它允许并行运行多个命令，脚本可以使用任何语言，并通过 YAML 文件提供灵活的配置。

lefthook 以速度为目标设计，通过并行执行和智能跳过机制将钩子的运行时间降到最低。

# CONFIGURATION

```yaml
# lefthook.yml
pre-commit:
  parallel: true
  commands:
    lint:
      run: npm run lint
    test:
      run: npm test
```

# CAVEATS

需要在项目根目录下有 lefthook.yml。克隆仓库后必须重新安装钩子。并行执行可能导致输出交错。

# HISTORY

lefthook 由 **Evil Martians** 创建，是 husky 和 pre-commit 的快速多语言替代方案，于 **2019 年**首次发布。

# INSTALL

```brew: brew install lefthook```

```nix: nix profile install nixpkgs#lefthook```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [husky](/man/husky)(1), [pre-commit](/man/pre-commit)(1)
