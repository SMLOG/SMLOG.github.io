---
layout: default
---

### top sql

get slow sql:

```sql
SELECT
    *
FROM
    (
        SELECT
            sa.sql_text,
            sa.sql_fulltext,
            sa.executions                                       "执行次数",
            round(sa.elapsed_time / 1000000, 2)                 "总执行时间",
            round(sa.elapsed_time / 1000000 / sa.executions, 2) "平均执行时间",
            sa.command_type,
            sa.parsing_user_id                                  "用户ID",
            u.username                                          "用户名",
            sa.hash_value
        FROM
            v$sqlarea sa
            LEFT JOIN all_users u ON sa.parsing_user_id = u.user_id
        WHERE
            sa.executions > 0
        ORDER BY
            ( sa.elapsed_time / sa.executions ) DESC
    )
WHERE
    ROWNUM <= 50;

```

get most query sql:

```sql
SELECT
    *
FROM
    (
        SELECT
            s.sql_text,
            s.executions      "执行次数",
            s.parsing_user_id "用户名",
            RANK()
            OVER(
                ORDER BY
                    executions DESC
            )                 exec_rank
        FROM
            v$sql     s
            LEFT JOIN all_users u ON u.user_id = s.parsing_user_id
    ) t
WHERE
    exec_rank <= 100;
```

```sql
SELECT
    s.spid,
    t.sql_id,
    t.serial#,
    t.username,
    t.sql_id,
    a.sql_text,
    a.sql_fulltext
FROM
    v$session t,
    v$process s,
    v$sqlarea a
WHERE
        t.paddr = s.addr
    --and s.SPID in ('6960')
    AND a.sql_id = t.sql_id;
```


find the big table:
```sql
SELECT
    *
FROM
    (
        SELECT
            segment_name,
            SUM(bytes) / 1024 / 1024 mb
        FROM
            dba_segments
        WHERE
            tablespace_name = 'SYSTEM'
        GROUP BY
            segment_name
        ORDER BY
            2 DESC
    )
WHERE
    ROWNUM < 10;
```