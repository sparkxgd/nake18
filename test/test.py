snake_list = [{"key1":1,"key2":"xiao1"},{"key1":2,"key2":"xiao2"},{"key1":3,"key2":"xiao3"},{"key1":4,"key2":"xiao4"}]
temp_0 = snake_list[0]
for i in range(1, len(snake_list)):
    # print("%d :(%s，%s)" %(i,snake_list[i-1].get("x"),snake_list[i-1].get("y")))
    temp = snake_list[i]
    snake_list[i] = temp_0
    temp_0 = temp
print(snake_list)

