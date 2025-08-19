if __name__ == "__main__":

    with open("data/mytext.txt","w",encoding="utf-8") as f:
        print("파일 라인1",file=f)
        f.write("파일 write")
        f.close()

    with open("data/mytext.txt","r",encoding="utf-8") as f:
        data = f.readlines()
        for d in data:
            print(d)
        f.close()

    with open("data/mytext.txt","r",encoding="utf-8") as f:
        data = f.readlines()
        print(data)
        f.close()