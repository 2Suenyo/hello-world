print("데이터를 불러오는 중입니다")

import matplotlib.pyplot as plt
import numpy as np

price_list = []
demand_list = []

# 파일 읽기
with open('price_data.csv', 'r') as file1 :
    for Content1 in file1 :
        price_list.append(Content1.strip('\n').split(','))

with open('demand_data.csv', 'r', encoding = 'UTF8') as file2 :
    for Content2 in file2 :
        demand_list.append(Content2.strip('\n').split(','))

print("원하시는 상품을 입력하시면 우리나라에서의 수요량 및 가격 변화율에 기반한 수요의 가격 탄력성을 검색하실 수 있습니다.")

while True :
    price_diff_list = []
    demand_diff_list = []
    elasticity_list = []
    total = 0
    
    search_product = str(input("찾으시려는 상품을 입력해주세요 : "))

    # 가격 변화율 계산
    for i in range(len(price_list)) :
        if price_list[i][0] == search_product :
            
            for j in range(8) :
                try :
                    price_diff = (float(price_list[i][j+2])-float(price_list[i][j+1]))/float(price_list[i][j+1])*100
                except :
                    price_diff = '측정불가'
                price_diff_list.append(price_diff)
        
            # 수요량 변화율 계산
            for k in range(len(demand_list)) :
                if demand_list[k][0] == search_product :
            
                    for l in range(8) :
                        try :
                            demand_diff = (float(demand_list[k][l+2])-float(demand_list[k][l+1]))/float(demand_list[k][l+1])*100
                        except :
                            demand_diff = '측정불가'
                        demand_diff_list.append(demand_diff)
                
                    # 수요의 가격탄력성 계산
                    for m in range(8) :
                        try :
                            elasticity = abs(demand_diff_list[m]/price_diff_list[m])
                        except :
                            elasticity = '측정불가'
                        elasticity_list.append(elasticity)

                    # 평균 가격탄력성 계산
                    for n in elasticity_list :
                        if not n == '측정불가' :
                            total += n

                    elasticity_avg = total/len(elasticity_list)
    
                    # elasticity level 판정
                    if elasticity_avg > 1 :
                        elasticity_level = '탄력적'
                    elif elasticity_avg == 1 :
                        elasticity_level = '단위탄력적'
                    elif elasticity_avg < 1 :
                        elasticity_level = '비탄력적'

                    # 결과 출력
                    print("최근 8년간의 가격탄력성 : " + str(elasticity_list))
                    print("평균 가격탄력성 : " + str(elasticity_avg) + " (" + elasticity_level + ")")

                    # 그래프 개형
                    x = np.arange(0, 100, 0.2)
                    y = - elasticity_avg * (x - 100)
                    plt.xlabel('quantity')
                    plt.ylabel('price')
                    plt.plot(x,y)
                    plt.axis([0, 100, 0, 100])
                    plt.show()

                    break
                
                elif k >= (len(demand_list) - 1) :
                    print("찾으시려는 상품이 없습니다")

            break
        
        elif i >= (len(price_list) - 1) :
            print("찾으시려는 상품이 없습니다")
