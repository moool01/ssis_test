import torch

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

def print_hi(name):
    print(f'Hi, {name}, Hi, {device}')  # 중단점을 전환하려면 Cmd+F8을(를) 누릅니다.


if __name__ == '__main__':
    print_hi('PyCharm')
