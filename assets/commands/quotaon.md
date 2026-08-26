# TAGLINE

在文件系统上启用磁盘配额执行

# TLDR

**在文件系统上启用配额**

```sudo quotaon [/home]```

**启用所有配额**

```sudo quotaon -a```

**仅启用用户配额**

```sudo quotaon -u [/home]```

**仅启用组配额**

```sudo quotaon -g [/home]```

**详细输出**

```sudo quotaon -v [/home]```

# SYNOPSIS

**quotaon** [_options_] [_filesystem_...]

# PARAMETERS

**-a**
> 启用 /etc/fstab 中所有文件系统。

**-u**
> 启用用户配额。

**-g**
> 启用组配额。

**-v**
> 详细模式。

**-p**
> 仅打印状态。

**-f**
> 强制启用。

# DESCRIPTION

**quotaon** 在文件系统上启用磁盘配额执行。必须先在 /etc/fstab 中配置配额，并用 quotacheck 创建配额文件。

# EXAMPLES

```bash
# Enable all configured quotas
sudo quotaon -a

# Enable on specific filesystem
sudo quotaon /home

# Enable user quotas only
sudo quotaon -u /home

# Check what would be enabled
sudo quotaon -p /home

# Enable with verbose output
sudo quotaon -vug /home
```

# SETUP WORKFLOW

```bash
# 1. Edit /etc/fstab (add usrquota,grpquota)
# 2. Remount filesystem
mount -o remount /home

# 3. Create quota files
quotacheck -cug /home

# 4. Enable quotas
quotaon /home

# 5. Set user limits
edquota -u username
```

# CAVEATS

需要内核和文件系统支持配额。必须先运行 quotacheck。需要 root 权限。

# HISTORY

磁盘配额起源于 **BSD Unix**，后来被 Linux 采用用于管理磁盘空间分配。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quotacheck](/man/quotacheck)(8), [edquota](/man/edquota)(8), [repquota](/man/repquota)(8)
