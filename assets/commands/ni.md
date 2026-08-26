# TAGLINE

自动使用正确的包管理器

# TLDR

为当前项目**安装**全部依赖

```ni```

**添加软件包**（作为开发依赖）

```ni [package-name] -D```

**全局添加软件包**

```ni -g [package-name]```

依据锁文件执行**全新安装**（等价于 npm ci / pnpm install --frozen-lockfile）

```nci```

**运行脚本**，并透传参数

```nr [script] [args...]```

无需安装即**执行软件包**（等价于 npx / pnpm dlx）

```nlx [package] [args...]```

**卸载**软件包

```nun [package-name]```

以交互方式**升级**依赖

```nup -i```

# SYNOPSIS

**ni** [_options_] [_packages..._]

**nr** [_script_] [_args..._]

**nlx** _package_ [_args..._]

**nun** _package..._

**nup** [_options_]

**nci**

**na** _args..._

# DESCRIPTION

**ni** 是 **Anthony Fu** 开发的一款小型命令行工具，它会把包管理器命令分派给当前项目实际使用的那个包管理器：**npm**、**yarn**、**pnpm**、**bun** 或 **deno**。检测方法是查看项目根目录中的锁文件（_package-lock.json_、_yarn.lock_、_pnpm-lock.yaml_、_bun.lock_、_bun.lockb_、_deno.json_），或 _package.json_ 里的 **packageManager** 字段。

不管面对哪个项目，用户输入的都是同一组简短命令。**ni** 安装依赖，**nr** 运行脚本，**nlx** 执行一次性的软件包，**nun** 移除软件包，**nup** 升级软件包，**nci** 执行全新安装，**na** 则把任意参数原样透传给检测到的 agent。

当 _fzf_ 位于 PATH 中时还可以使用交互式菜单：不带参数的 **nr** 会列出脚本，**ni -i** 可以挑选软件包，**nr -** 会重新运行上一个脚本。

# PARAMETERS

**-D**
> 添加为开发依赖（对应 --save-dev / -D）。

**-P**
> 仅按生产环境安装（剔除开发依赖）。

**-g**
> 操作全局安装的软件包。

**-i**
> 交互模式（通过 fzf 选择软件包或脚本）。

**--frozen**
> 使用冻结的锁文件安装（不做更新）。

**-C** _DIR_
> 如同从 _DIR_ 目录中调用一样运行。

**?**
> 显示针对检测到的 agent 转换后的命令，但不实际执行。

**-v**, **--version**
> 打印 **ni** 的版本号。

**-h**, **--help**
> 显示帮助。

# CONFIGURATION

用户配置保存在 **~/.nirc**：

```
defaultAgent=npm
globalAgent=npm
```

- **defaultAgent** 在未检测到锁文件时选择使用的包管理器（设为 _prompt_ 可改为交互式询问）。
- **globalAgent** 选择用于全局安装的包管理器。

环境变量 **NI_DEFAULT_AGENT**、**NI_GLOBAL_AGENT**、**NI_CONFIG_FILE** 和 **NI_AUTO_INSTALL** 可在每个 Shell 中覆盖这些设置。

# CAVEATS

在 Windows **PowerShell** 中，内置的 New-Item 别名 _ni_ 会与本工具冲突；使用前先用 **Remove-Item Alias:ni -Force** 移除该别名。为避免与其他工具冲突，一些旧别名已改名：_nx_/_nix_ 现为 **nlx**，_nu_ 现为 **nup**。由于 **ni** 依赖锁文件检测，完全没有锁文件的项目会回退到 **defaultAgent** 设置。

# HISTORY

由 **Anthony Fu**（antfu）创建，于 **2021 年**首次以 **@antfu/ni** 之名发布到 npm。项目后来迁移到 GitHub 的 **antfu-collective** 组织下，通过 npm（_@antfu/ni_）和 **Homebrew**（_brew install ni_）分发。项目使用 TypeScript 编写。

# INSTALL

```brew: brew install ni```

```nix: nix profile install nixpkgs#ni```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1), [bun](/man/bun)(1), [deno](/man/deno)(1)
