# Metric longTask = true

[micrometer-docs/src/docs/concepts/long-task-timers.adoc at main · micrometer-metrics/micrometer-docs · GitHub](https://github.com/micrometer-metrics/micrometer-docs/blob/main/src/docs/concepts/long-task-timers.adoc)

```
The long task timer is a special type of timer that lets you measure time while an event being measured is still running. A normal Timer only records the duration after the task is complete.

Long task timers publish at least the following statistics:

Active task count

Total duration of active tasks

The maximum duration of active tasks
```

  

**Unlike a regular `Timer`, a long task timer does not publish statistics about completed tasks.**

### 현재 실행중인 task의 통계를 제공

### 
