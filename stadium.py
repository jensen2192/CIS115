def class_a(value_a):
    revenue_a = value_a * 20
    print('Class A ticket revenue is $', format(revenue_a, ',.2f'),
          sep='')


def class_b(value_b):
    revenue_b = value_b * 15
    print('Class B ticket revenue is $', format(revenue_b, ',.2f'),
          sep='')


def class_c(value_c):
    revenue_c = value_c * 10
    print('Class C ticket revenue is $', format(revenue_c, ',.2f'),
          sep='')


def main():
    value_a = int(input('Number of Class A tickets sold: '))
    value_b = int(input('Number of Class B tickets sold: '))
    value_c = int(input('Number of Class C tickets sold: '))
    class_a(value_a)
    class_b(value_b)
    class_c(value_c)

main()
