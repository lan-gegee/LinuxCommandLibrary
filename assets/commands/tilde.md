# TAGLINE

Shell 波浪号展开简写

# TLDR

**主目录**

```cd ~```

**其他用户的主目录**

```cd ~[username]```

**上一个目录**

```cd ~-```

**当前目录**

```echo ~+```

**大小写转换（bash 4+）**

```echo ${var~~}```

# SYNOPSIS

**~**
**~**_username_
**~+**
**~-**

# TILDE EXPANSIONS

**~**
> 当前用户的主目录（$HOME）

**~username**
> 指定用户的主目录

**~+**
> 当前工作目录（$PWD）

**~-**
> 上一个工作目录（$OLDPWD）

# 参数展开 (bash 4+)

**${var^}**
> 首字符转大写

**${var^^}**
> 所有字符转大写

**${var,}**
> 首字符转小写

**${var,,}**
> 所有字符转小写

**${var~}**
> 反转首字符大小写

**${var~~}**
> 反转所有字符大小写

# DESCRIPTION

**~**（波浪号）会被 shell 展开为目录路径。它是一种简写，避免了硬编码 /home/user 这类路径。

波浪号展开只出现在词首或 **:** 之后。位于文本中间时，**~** 是字面字符。

```bash
cd ~                    # Go home
cd ~/Documents          # Home subdirectory
cd ~root                # Root's home
PATH=$PATH:~/bin        # After : works
```

**~+** 和 **~-** 形式对应 **pushd/popd** 目录栈，可在最近使用的目录之间快速切换。

# EXAMPLES

```bash
# Copy to home
cp file.txt ~

# Use another user's home
sudo cp config ~www-data/

# Toggle between directories
cd /var/log
cd /etc
cd ~-     # Back to /var/log
cd ~-     # Back to /etc

# Case toggle (bash 4+)
name="Hello"
echo ${name~~}    # hELLO
```

# CAVEATS

波浪号只有在未加引号且位于词首时才会展开。**"~"** 是字面字符，不是主目录。

**~user** 会在密码数据库中查找该用户，而不只是字符串拼接。

如果没有上一个目录（新 shell），**~-** 为空。

# INSTALL

```zypper: sudo zypper install tilde```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cd](/man/cd)(1), [bash](/man/bash)(1), [pwd](/man/pwd)(1), [pushd](/man/pushd)(1)
