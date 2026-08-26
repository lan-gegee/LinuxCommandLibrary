# TAGLINE

基于 age 的 Git 透明文件级加密

# TLDR

**初始化**当前 Git 仓库以启用透明加密

```git agecrypt init```

**注册**用于解密的 age 身份（私钥）

```git-agecrypt config add -i [path/to/age.key]```

为一个或多个路径**注册** age 接收方

```git-agecrypt config add -r [age1...] -p [secrets/prod.env]```

**列出**当前的接收方和身份

```git-agecrypt config list```

**移除**之前注册的接收方

```git-agecrypt config remove -r [age1...] -p [secrets/prod.env]```

**显示**哪些被跟踪的文件已加密

```git-agecrypt status```

**拆除**本仓库中的集成

```git-agecrypt deinit```

# SYNOPSIS

**git-agecrypt** _command_ [_options_]
**git agecrypt** _command_ [_options_]

# PARAMETERS

**init**
> 将 **clean**、**smudge** 和 **textconv** 过滤器安装到 _.git/config_，使加密/解密在提交和检出时自动进行。

**deinit**
> 从当前仓库中移除过滤器集成。已被跟踪的加密 blob 不受影响。

**config add -r** _recipient_ **-p** _path..._
> 注册一个 age _接收方_（公钥），使其能够解密所列的 _路径_。可重复执行以授予多个密钥的访问权。同时接受 SSH **ed25519** 公钥和 age **age1...** 密钥。

**config add -i** _identity_
> 注册一个 age _身份_（私钥文件），供本地检出解密文件时使用。存储在 **.git/config** 中，绝不会被提交。

**config remove -r** _recipient_ [**-p** _path..._]
> 撤销一个接收方，可选地仅限于特定路径。

**config remove -i** _identity_
> 忘记一个本地身份。

**config list**
> 打印已配置的接收方（按路径）和已注册的本地身份。

**status**
> 报告哪些被跟踪的路径配置了加密，以及工作副本是否与加密 blob 一致。

**clean**
> 内部过滤器入口：从标准输入读取明文，将密文写到标准输出。由 Git 通过 **filter.agecrypt.clean** 钩子调用。

**smudge**
> 内部过滤器入口：从标准输入读取密文，将明文写到标准输出。由 Git 在检出时调用。

**textconv** _file_
> **git diff** 使用的内部辅助程序，将加密 blob 渲染为明文以便比较差异，同时避免密文泄漏到工作副本中。

**-v**, **--verbose**
> 提高日志详细程度。

**--help**
> 打印所选子命令的帮助。

**--version**
> 打印版本并退出。

# DESCRIPTION

**git-agecrypt** 是一个 Git 集成工具，让仓库中的机密在静态存储时保持加密状态，而在工作树中以明文呈现。它是 **git-crypt** 的替代方案，用 **age** 取代了 **GPG**，密钥材料更小，并支持 **SSH** 密钥和 age 插件存根（例如 **age-plugin-yubikey**）。

运行 **git-agecrypt init** 之后，仓库的 _.git/config_ 中会出现指向该二进制文件的 **clean**、**smudge** 和 **textconv** 过滤器条目。_.gitattributes_ 中被路径模式匹配到的每个文件（通常为 **filter=agecrypt diff=agecrypt**）都会在进入对象库时被加密、在离开时被解密。接收方及按路径划分的作用范围保存在一个会被提交的 _git-agecrypt.toml_ 中，而本地私有身份则保存在 _.git/config_ 里，因此永远不会离开开发者的机器。

由于 age 加密是非确定性的，git-agecrypt 会在 _.git/git-agecrypt/_ 下记录每个明文的 **BLAKE3** 哈希；如果明文未变，就复用先前存储的密文，从而避免提交产生无意义的变动。

# CONFIGURATION

**git-agecrypt.toml**（会被提交）声明接收方及其可解密的路径：

```
[[recipient]]
key = "age1abc..."
paths = ["secrets/*.env", "deploy/*.yaml"]

[[recipient]]
key = "ssh-ed25519 AAAA... user@host"
paths = ["secrets/*.env"]
```

**.gitattributes** 标记哪些文件需要加密：

```
secrets/*.env  filter=agecrypt diff=agecrypt
deploy/*.yaml  filter=agecrypt diff=agecrypt
```

**.git/config**（每个检出各一份，绝不会被提交）存储身份位置以及由 **init** 写入的过滤器接线：

```
[filter "agecrypt"]
        clean = git-agecrypt clean %f
        smudge = git-agecrypt smudge %f
        required = true
[diff "agecrypt"]
        textconv = git-agecrypt textconv
[agecrypt]
        identity = /home/user/.config/age/keys.txt
```

# CAVEATS

**git-crypt** 和 **git-agecrypt** 都依赖 Git 过滤器，这意味着除非在没有身份的检出上运行相关工具，否则 **git log -p**、**git blame** 等工具可能通过 **textconv** 泄漏明文。**age** 是一种认证流密码而非确定性格式，因此除非保留 git-agecrypt 的哈希缓存，每次加密产生的密文都不同——清空 _.git/git-agecrypt/_ 后即使明文未变也会产生 diff。撤销一个已泄漏的接收方需要重写历史；与所有 Git 层面的加密工具一样，**git-agecrypt** 无法撤回已经离开仓库的密文。

# HISTORY

**git-agecrypt** 由 **vlaci** 创建，作为开源项目在 GitHub 上维护。它构建于 **Filippo Valsorda** 开发的现代文件加密工具 **age** 之上，定位为 **git-crypt** 更轻量、更灵活的后继者，适合已经在使用 age 或 SSH 密钥管理机密的团队。

# INSTALL

```nix: nix profile install nixpkgs#git-agecrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-crypt](/man/git-crypt)(1), [age](/man/age)(1), [sops](/man/sops)(1), [git](/man/git)(1)
