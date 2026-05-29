"""
- Cấu trúc: Lưu toàn bộ giỏ hàng bằng 1 chuỗi `cart_data` duy nhất. Các sản phẩm phân cách bằng `;`, thuộc tính (Mã, Tên, SL, Giá) phân cách bằng `,`.
- Xử lý chuỗi: Dùng `.find()` và cắt chuỗi (slicing) để tách dữ liệu. Khi Thêm/Sửa/Xóa, tạo chuỗi `new_cart` để nối lại các phần tử hợp lệ.
- Bẫy lỗi: Chặn số âm/bằng 0 bằng `if <= 0` (Bẫy 1). Bắt lỗi nhập sai menu bằng `case _` (Bẫy 3).
"""

cart_data = "P001,Điện thoại iPhone 15,1,25000000;P002,Ốp lưng Silicon,2,150000;"

while True:
    print("\n========== SHOPEE CART MANAGEMENT SYSTEM ==========")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    
    choice = input("\nMời bạn chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<3} | {'Mã SP':<5} | {'Tên Sản Phẩm':<22} | {'SL':<3} | {'Đơn Giá':<14} | {'Thành Tiền'}")
            print("-" * 75)
            
            total_qty = 0
            total_price = 0
            stt = 1
            
            temp_data = cart_data
            while temp_data != "":
                item_end = temp_data.find(";")
                if item_end == -1:
                    break
                    
                item_str = temp_data[:item_end]
                
                comma1 = item_str.find(",")
                comma2 = item_str.find(",", comma1 + 1)
                comma3 = item_str.find(",", comma2 + 1)
                
                prod_id = item_str[:comma1]
                prod_name = item_str[comma1 + 1:comma2]
                qty = int(item_str[comma2 + 1:comma3])
                price = int(item_str[comma3 + 1:])
                
                subtotal = qty * price
                total_qty += qty
                total_price += subtotal
                
                print(f"{stt:<3} | {prod_id:<5} | {prod_name:<22} | {qty:<3} | {price:>10,}đ   | {subtotal:>10,}đ")
                
                stt += 1
                temp_data = temp_data[item_end + 1:]
                
            print("-" * 75)
            print(f"=> Tổng số lượng sản phẩm trong giỏ: {total_qty}")
            print(f"=> Tổng tiền thanh toán: {total_price:,}đ")
            
        case "2":
            new_id = input("\nNhập mã sản phẩm: ").strip().upper()
            new_name = input("Nhập tên sản phẩm: ").strip()
            new_qty = int(input("Nhập số lượng: "))
            new_price = int(input("Nhập đơn giá: "))
            
            if new_qty <= 0 or new_price <= 0:
                print("Số lượng hoặc đơn giá không hợp lệ!")
            else:
                search_prefix = new_id + ","
                
                if cart_data.startswith(search_prefix) or (";" + search_prefix) in cart_data:
                    temp_data = cart_data
                    new_cart = ""
                    
                    while temp_data != "":
                        item_end = temp_data.find(";")
                        if item_end == -1:
                            break
                        item_str = temp_data[:item_end]
                        
                        comma1 = item_str.find(",")
                        prod_id = item_str[:comma1]
                        
                        if prod_id == new_id:
                            comma2 = item_str.find(",", comma1 + 1)
                            comma3 = item_str.find(",", comma2 + 1)
                            
                            old_qty = int(item_str[comma2 + 1:comma3])
                            updated_qty = old_qty + new_qty
                            
                            updated_item = f"{new_id},{new_name},{updated_qty},{new_price}"
                            new_cart += updated_item + ";"
                        else:
                            new_cart += item_str + ";"
                            
                        temp_data = temp_data[item_end + 1:]
                        
                    cart_data = new_cart
                    print("Sản phẩm đã tồn tại, cộng dồn số lượng thành công!")
                else:
                    cart_data += f"{new_id},{new_name},{new_qty},{new_price};"
                    print("Thêm sản phẩm mới thành công!")
                    
        case "3":
            update_id = input("\nNhập mã sản phẩm cần cập nhật: ").strip().upper()
            search_prefix = update_id + ","
            
            if cart_data.startswith(search_prefix) or (";" + search_prefix) in cart_data:
                new_qty = int(input("Nhập số lượng mới: "))
                
                if new_qty <= 0:
                    print("Số lượng không hợp lệ!")
                else:
                    temp_data = cart_data
                    new_cart = ""
                    
                    while temp_data != "":
                        item_end = temp_data.find(";")
                        if item_end == -1:
                            break
                        item_str = temp_data[:item_end]
                        
                        comma1 = item_str.find(",")
                        prod_id = item_str[:comma1]
                        
                        if prod_id == update_id:
                            comma2 = item_str.find(",", comma1 + 1)
                            comma3 = item_str.find(",", comma2 + 1)
                            
                            prod_name = item_str[comma1 + 1:comma2]
                            price = item_str[comma3 + 1:]
                            
                            updated_item = f"{update_id},{prod_name},{new_qty},{price}"
                            new_cart += updated_item + ";"
                        else:
                            new_cart += item_str + ";"
                            
                        temp_data = temp_data[item_end + 1:]
                        
                    cart_data = new_cart
                    print("Cập nhật số lượng thành công!")
            else:
                print("Mã sản phẩm không tồn tại trong giỏ hàng!")
                
        case "4":
            delete_id = input("\nNhập mã sản phẩm cần xóa: ").strip().upper()
            search_prefix = delete_id + ","
            
            if cart_data.startswith(search_prefix) or (";" + search_prefix) in cart_data:
                temp_data = cart_data
                new_cart = ""
                
                while temp_data != "":
                    item_end = temp_data.find(";")
                    if item_end == -1:
                        break
                    item_str = temp_data[:item_end]
                    
                    comma1 = item_str.find(",")
                    prod_id = item_str[:comma1]
                    
                    if prod_id != delete_id:
                        new_cart += item_str + ";"
                        
                    temp_data = temp_data[item_end + 1:]
                    
                cart_data = new_cart
                print("Xóa sản phẩm thành công!")
            else:
                print("Mã sản phẩm không tồn tại trong giỏ hàng!")
                
        case "5":
            print("\nThoát chương trình. Tạm biệt!")
            break
            
        case _:
            print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")