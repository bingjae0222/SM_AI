if __name__ == "__main__":

    #set
    t1 = {1,2,3,4,5}
    print(type(t1))
    print(t1)
    t1.add(6)
    t1.add(5)
    print(t1)


    #tuple
    print("------------tuple--------------")
    t2 = (1,2,3,4,5)
    print(type(t2))
    print(t2)
    print(t2[1])

    #dic -> key,value
    d1 = {"a":1,"b":2,"c":3}
    print(type(d1))
    print(d1)
    print(d1["a"])

    d2 = {"name":"이말숙","나이":21,"전공":"sw"}
    print(d2["name"])
    print(d2["나이"])
    print(d2["전공"])



    #응용
    sts = [
        {"name": "이말숙", "나이": 21, "전공": "sw"},
        {"name": "김말숙", "나이": 22, "전공": "sw"},
        {"name": "홍말숙", "나이": 23, "전공": "mp"},
        {"name": "지말숙", "나이": 24, "전공": "sw"}
    ]


    #sw학과 학생들의 나이 합과 평균을 출력






