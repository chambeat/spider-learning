# 多进程
import multiprocessing


def process(index):
    print(f"Process: '{index}'")


if __name__ == '__main__':  # 不可省略此行
    for i in range(5):
        """
            注意: 
                此处 args 必须要是一个元组，即使只有一个参数，也要在元组第一个元素后面加一个 ',' (逗号)。
                如果没有逗号则和单个元素本身没有区别，无法构成元组，导致参数传递出现问题。
        """
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
