class Phone:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

    def set_tel(self, tel):
        self.tel = tel

class PhoneBook:
    def __init__(self):
        self.phone_list_max = None
        self.phone_list = []
    
    def add(self, name, tel):
        self.phone_list.append(Phone(name, tel))

    def input_persons(self):
        while True:
            try:            
                self.phone_list_max  = int(input("인원수 >> "))
                break
            except:
                print("잘못된 입력입니다. 인원수를 숫자로 입력해주세요요")
                continue

    def input_phone(self):
        is_done = False        
        while True:
            try:            
                
                for i in range(self.phone_list_max):
                    tel_name = input("이름과 전화번호 입력(빈 칸은 종료) >> ")
                    tel_name = tel_name.split(" ")
                    self.add(tel_name[0], tel_name[1])                

                is_done = True      
            except:
                print("잘못된 입력입니다. 처음부터 다시 입력해주세요.")
                continue

            if is_done:
                break
            
        print("저장되었습니다...")

    def phone_search(self):
            while True:
                try:
                    name = input("검색할 이름 입력 >> ")
                    
                    if name == "그만":
                        break

                    #리스트 컴프리 헨션을 응용해서 찾기
                    searched_list = [phone for phone in self.phone_list if phone.name == name]
                    
                    if len(searched_list) == 0:
                        print("찾는 이름이 없습니다.")
                    else:
                        for phone in searched_list:
                            print(phone.name, phone.tel)
        
                
                except:
                    print("잘못된 입력입니다. 처음부터 다시 입력해주세요.")
                    continue

    def run(self):        
        self.input_persons()
        self.input_phone()
        self.phone_search()


phone_book = PhoneBook()
phone_book.run()