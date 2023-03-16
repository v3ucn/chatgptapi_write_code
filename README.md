# chatgptapi_write_code

```
pip3 install openai==0.27.0
```

## How to use

```
if __name__ == '__main__':
    
    @chatgpt_code
    def bloom(target:str,storage:list):
        """
        Use a Bloom filter to check if the target is in storage , Just use this func , no more class
        """

    print(bloom("你好",["你好","Helloworld"]))
```

```
➜  chatgpt_write_code /opt/homebrew/bin/python3.10 "/Users/liuyue/wodfan/work/chatgpt_write_code/chatgpt_write_code.p
y"
generated code:
```python
def bloom(target, storage):
    # Initialize the Bloom filter with all zeros
    bloom_filter = [0] * len(storage)
    
    # Hash the target and set the corresponding bit in the Bloom filter to 1
    for i in range(len(storage)):
        if target in storage[i]:
            bloom_filter[i] = 1
    
    # Check if all the bits corresponding to the target are set to 1 in the Bloom filter
    for i in range(len(storage)):
        if target in storage[i] and bloom_filter[i] == 0:
            return False
    
    return True
```
```
