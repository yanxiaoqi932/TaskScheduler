# 2024年NBJL实验室推免招生考核：计算任务调度问题
## 需要实现的接口示例
需要基于抽象类Scheduler实现调度器类FinalScheduler，该类包含两个方法 init 和 schedule。如下所示：
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
### 补充
为了方便同学们在优化算法时对算法分数有一个基本的了解，这里给出实验室的算法分数及每次优化幅度作为参考：

算法分数为628.0，优化情况如下：
- 第一阶段优化：-172600.5 -> -609.0
- 第二阶段优化：-609.0 -> 50.5
- 第三阶段优化：50.5 -> 399.5
- 第四阶段优化：399.5 -> 490.0
- 第五阶段优化：490.0 -> 628.0

可见越往后，单位分数提升的难度呈现指数级上升，因此不要求同学们能够达到600分以上，尽力提升分数即可哈。但是不能根据demo数据集人工调度，对此实验室会使用另一个数据集对算法性能进行二次评估。
