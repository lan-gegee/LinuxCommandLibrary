# TAGLINE

让调用线程挂起指定的时长

# TLDR

**睡眠 1 秒（C 代码）**

```struct timespec ts = {1, 0}; nanosleep(&ts, NULL);```

**睡眠 500 毫秒**

```struct timespec ts = {0, 500000000L}; nanosleep(&ts, NULL);```

**带剩余时间睡眠**

```nanosleep(&req, &rem);```

# SYNOPSIS

**int nanosleep**(const struct timespec *_req_, struct timespec *_rem_)

# PARAMETERS

**req**
> 请求的睡眠时长（秒和纳秒）。

**rem**
> 被中断时的剩余时间（可为 NULL）。

# DESCRIPTION

**nanosleep** 让调用线程挂起指定的时长。与 sleep() 不同，它提供纳秒级精度并能优雅处理中断。

如果被信号中断，函数会立即返回，并将剩余时间存入 rem。

# EXAMPLE

```c
#include <time.h>

int main() {
    struct timespec req = {0, 100000000L}; // 100ms
    struct timespec rem;

    while (nanosleep(&req, &rem) == -1) {
        req = rem; // Continue sleeping
    }
    return 0;
}
```

# TIMESPEC STRUCTURE

```c
struct timespec {
    time_t tv_sec;   // Seconds
    long   tv_nsec;  // Nanoseconds (0-999999999)
};
```

# CAVEATS

实际精度取决于系统时钟。实际睡眠时间可能略长于请求值。信号送达时返回 EINTR。

# HISTORY

nanosleep 在 **POSIX.1-2001** 中引入，用于提供超出 sleep() 秒级粒度的高分辨率睡眠功能。

# SEE ALSO

[sleep](/man/sleep)(3), [usleep](/man/usleep)(3)
