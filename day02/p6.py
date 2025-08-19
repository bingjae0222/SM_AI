import pickle

if __name__ == "__main__":
    sts = [
        {"name": "이말숙", "나이": 21, "전공": "sw"},
        {"name": "김말숙", "나이": 22, "전공": "sw"},
        {"name": "홍말숙", "나이": 23, "전공": "mp"},
        {"name": "지말숙", "나이": 24, "전공": "sw"}
    ]

pickle.dump(sts,open("data/sts.pkl","wb"))
result = pickle.load(open("data/sts.pkl","rb"))
print(type(result))
print(result)