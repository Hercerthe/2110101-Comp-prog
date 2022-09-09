# HW02 (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

def get_sum(data) :
    for i in range(len(data)) :
        if len(str(data[i])) == 10 :
            data += [[data[i], data[i + 1]]]
    data = data[i + 1:]

    ram = []

    for i in range(len(data)) :
        if data[i][0] == data[i + 1][0] :
            if ram == [] :
                ram = [data[i][0]]
            ram += [data[i][1]]
        elif ram == [] and data[i][0] != data[i + 1][0] :
            data += [data[i]]
        elif ram != [] and data[i][0] != data[i + 1][0] :
            ram += [data[i][1]]
            data += [ram]
            ram = []
    data = data[i + 1:]

    for i in range(len(data)) :
        if len(data[i][1:]) > 3 :
            data[i] = [data[i][0], sum(data[i][1:]) - min(data[i][1:])]
        else :
            data[i] = [data[i][0], sum(data[i][1:])]

    for i in range(len(data)) :
        data += data[i]
    data = data[i + 1:]

    return data
# -----------------------------
d = [
  6610013121,4,
  6610021021,5, 6610021021,5,
  6610061121,5, 6610061121,5, 6610061121,1,
  6610000121,3, 6610000121,2, 6610000121,2, 6610000121,3,
]
out = get_sum(d)
print(out) # ต้องแสดง [6610013121, 4, 6610021021, 10, 6610061121, 11, 6610000121, 8]
# ข้อแนะนำ: ควรทดสอบ get_sum ด้วยข้อมูลชุดอื่นด้วย (ลิสต์ d ข้างบนอาจมีไม่ครอบคลุมทุกกรณี)