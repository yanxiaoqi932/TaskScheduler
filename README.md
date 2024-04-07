# 2024年NBJL实验室推免招生考核：计算任务调度问题
## 需要实现的接口示例
选手需要基于抽象类Scheduler实现调度器类FinalScheduler，该类包含两个方法 init 和 schedule。如下所示：
```python3
class FinalScheduler(Scheduler):
    def __init__(self):
        pass
        
    def init(self, driver_num: int) -> None:
        pass
        
    def schedule(self, logical_clock: int, request_list: List, driver_statues: List) -> List:
        pass
```
具体要求请查看文档，存在疑问请在issues及时沟通。
## 运行评分程序
```python3
python3 runner.py
```