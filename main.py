# This entrypoint file to be used in development. Start by reading README.md
from pytest import main
from arithmetic_arranger import arithmetic_arranger


a = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
b = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(a)
print(b)

# x = open('test.txt', 'w')
# x.write(a)
# x.write(b)

# Run unit tests automatically
main()
