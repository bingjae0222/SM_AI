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

    sum = 0
    count = 0

    for data in sts:
        if data["전공"] == 'sw':
            sum += data["나이"]
            count += 1




    #전체학생 나이 합 평균
    for st in sts:
        sum += st["나이"]
    print(f"합 {sum} 평균{sum/len(sts)}")


    #sw 학생들 나이 합 평균

    sum = 0
    count = 0
    for data in sts:
        if data["전공"] == 'sw':
            sum += data["나이"]
            count += 1




